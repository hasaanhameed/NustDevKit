"""LMSSession — an authenticated session against the NUST LMS (Moodle) portal.

PORT TARGET
-----------
Drop your existing NustPulse `LMSSession` (and any crypto/helper code it needs)
into this module. The rest of the gateway depends ONLY on the small interface
below — keep these method names/signatures (or adjust the call sites in
app/routes/ and app/dependencies.py to match your implementation):

    await login(email, password) -> bool        # authenticate; capture cookie + sesskey
    await get_user_full_name()   -> str          # optional, used for nicer responses
    await call_ajax(method, args) -> Any         # forward a Moodle AJAX service call
    await close()                -> None          # release the underlying HTTP client

`call_ajax` is what the proxy routes use: given a Moodle method name
(e.g. "core_course_get_recent_courses") and its args dict, it should issue the
authenticated request to Moodle's AJAX service (lib/ajax/service.php) using the
stored session cookie + sesskey and return the parsed result.
"""
from typing import Any

import httpx

from app.core.config import settings


class LMSAuthError(Exception):
    """Raised when authentication against the LMS fails unexpectedly."""


class LMSSession:
    def __init__(self) -> None:
        # A cookie-aware client; Moodle auth is session-cookie based.
        self._client = httpx.AsyncClient(
            base_url=settings.lms_base_url,
            follow_redirects=True,
            timeout=30.0,
        )
        self._sesskey: str | None = None

    async def login(self, email: str, password: str) -> bool:
        """Authenticate against the portal and capture the session cookie + sesskey.

        PORT: paste your NustPulse login flow here. Return True on success,
        False on invalid credentials. Store the scraped sesskey on self._sesskey.
        """
        raise NotImplementedError(
            "Port your NustPulse LMSSession.login() implementation here."
        )

    async def get_user_full_name(self) -> str:
        """Return the authenticated user's display name (optional convenience)."""
        raise NotImplementedError(
            "Port your NustPulse LMSSession.get_user_full_name() implementation here."
        )

    async def call_ajax(self, method: str, args: dict[str, Any]) -> Any:
        """Invoke a Moodle AJAX service method with the authenticated session.

        PORT/implement using self._client + self._sesskey against Moodle's
        lib/ajax/service.php convention (POST a JSON array of
        {index, methodname, args} with ?sesskey=... &info=method).
        """
        raise NotImplementedError(
            "Implement Moodle AJAX call forwarding here (uses self._sesskey)."
        )

    async def close(self) -> None:
        await self._client.aclose()
