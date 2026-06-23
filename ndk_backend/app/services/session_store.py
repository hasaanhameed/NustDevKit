"""In-memory session store: maps an opaque session id -> live LMSSession.

This is the deliberately-simple, no-database approach. Sessions live only for
the lifetime of the process; on restart (or sesskey expiry) the SDK user simply
logs in again. Swap this out for a SQLite/Redis-backed store later if you need
persistence or auto-refresh — the rest of the app only depends on this interface.
"""
import asyncio
import secrets

from app.services.lms_session import LMSSession


class InMemorySessionStore:
    def __init__(self) -> None:
        self._sessions: dict[str, LMSSession] = {}
        self._lock = asyncio.Lock()

    async def create(self, session: LMSSession) -> str:
        session_id = secrets.token_urlsafe(32)
        async with self._lock:
            self._sessions[session_id] = session
        return session_id

    async def get(self, session_id: str) -> LMSSession | None:
        async with self._lock:
            return self._sessions.get(session_id)

    async def pop(self, session_id: str) -> LMSSession | None:
        async with self._lock:
            return self._sessions.pop(session_id, None)


# Single process-wide store instance.
_store = InMemorySessionStore()


def get_session_store() -> InMemorySessionStore:
    return _store
