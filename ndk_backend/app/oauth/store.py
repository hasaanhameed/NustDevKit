import secrets
import time
from dataclasses import dataclass, field


@dataclass
class AuthCode:
    code: str
    client_id: str
    redirect_uri: str
    session_id: str
    code_challenge: str
    code_challenge_method: str
    expires_at: float = field(default_factory=lambda: time.monotonic() + 300)

    def is_expired(self) -> bool:
        return time.monotonic() > self.expires_at


@dataclass
class RefreshToken:
    token: str
    client_id: str
    session_id: str
    created_at: float = field(default_factory=time.monotonic)


class OAuthStore:
    def __init__(self) -> None:
        self._codes: dict[str, AuthCode] = {}
        self._refresh_tokens: dict[str, RefreshToken] = {}

    def create_auth_code(
        self,
        client_id: str,
        redirect_uri: str,
        session_id: str,
        code_challenge: str,
        code_challenge_method: str,
    ) -> str:
        code = secrets.token_urlsafe(32)
        self._codes[code] = AuthCode(
            code=code,
            client_id=client_id,
            redirect_uri=redirect_uri,
            session_id=session_id,
            code_challenge=code_challenge,
            code_challenge_method=code_challenge_method,
        )
        return code

    def consume_auth_code(self, code: str) -> AuthCode | None:
        entry = self._codes.pop(code, None)
        if entry is None or entry.is_expired():
            return None
        return entry

    def create_refresh_token(self, client_id: str, session_id: str) -> str:
        token = secrets.token_urlsafe(40)
        self._refresh_tokens[token] = RefreshToken(
            token=token,
            client_id=client_id,
            session_id=session_id,
        )
        return token

    def consume_refresh_token(self, token: str) -> RefreshToken | None:
        entry = self._refresh_tokens.pop(token, None)
        return entry


_store = OAuthStore()


def get_oauth_store() -> OAuthStore:
    return _store
