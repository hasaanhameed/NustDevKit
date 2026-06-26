"""In-memory session store with a sliding idle TTL.

Maps an opaque session id -> live LMSSession. A session is evicted (and its httpx
client closed) once idle longer than the configured timeout, so abandoned logins don't
leak memory or open connections. No database — sessions live only for the process.

Eviction is intentionally simple: the TTL slides on each access, and we sweep idle
sessions on every login (the only moment the store grows). A session is kept alive only
by `get()`, which runs only with a still-valid JWT — so the sliding idle TTL bounds the
store on its own, with no background task or separate absolute cap.
"""
import asyncio
import secrets
import time

from app.core.config import settings
from app.services.lms_session import LMSSession


class InMemorySessionStore:
    def __init__(self) -> None:
        # session id -> (session, last-access time in monotonic seconds)
        self._sessions: dict[str, tuple[LMSSession, float]] = {}
        self._lock = asyncio.Lock()

    def _ttl_seconds(self) -> float:
        return settings.session_idle_minutes * 60

    async def create(self, session: LMSSession) -> str:
        session_id = secrets.token_urlsafe(32)
        now = time.monotonic()
        ttl = self._ttl_seconds()
        async with self._lock:
            self._sessions[session_id] = (session, now)
            stale = [
                self._sessions.pop(sid)[0]
                for sid, (_, ts) in list(self._sessions.items())
                if now - ts > ttl
            ]
        for old in stale:
            await old.close()
        return session_id

    async def get(self, session_id: str) -> LMSSession | None:
        now = time.monotonic()
        async with self._lock:
            entry = self._sessions.get(session_id)
            if entry is None:
                return None
            session, ts = entry
            if now - ts > self._ttl_seconds():
                del self._sessions[session_id]
            else:
                self._sessions[session_id] = (session, now)  # slide on access
                return session
        await session.close()  # idle past TTL — free its client
        return None

    async def pop(self, session_id: str) -> LMSSession | None:
        async with self._lock:
            entry = self._sessions.pop(session_id, None)
        return entry[0] if entry else None


# Single process-wide store instance.
_store = InMemorySessionStore()


def get_session_store() -> InMemorySessionStore:
    return _store
