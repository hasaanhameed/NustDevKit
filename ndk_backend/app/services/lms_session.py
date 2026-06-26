"""LMSSession — an authenticated session against the NUST LMS (Moodle) portal.

Adapted from the NustPulse `LMSSession`. Each instance owns one httpx client and
represents a single logged-in user. The gateway creates one per `/auth/login` and
keeps it alive in the in-memory session store for the life of the bearer token —
so login happens once (fresh client → logintoken → authenticated cookies) and the
same session is reused for every proxied AJAX call.
"""
import logging
from typing import Any

import httpx
from bs4 import BeautifulSoup

from app.core.config import settings

logger = logging.getLogger(__name__)


def _flatten_params(args: dict[str, Any]) -> dict[str, Any]:
    """Encode (possibly nested) args into Moodle REST's bracketed form-field convention.

    Moodle's REST endpoint expects parameters as form fields, with arrays/objects
    flattened like `options[0][name]=excludecontents`. Scalars pass through as-is;
    booleans become 0/1.
    """
    out: dict[str, Any] = {}

    def walk(prefix: str, value: Any) -> None:
        if isinstance(value, dict):
            for key, val in value.items():
                walk(f"{prefix}[{key}]" if prefix else str(key), val)
        elif isinstance(value, (list, tuple)):
            for i, val in enumerate(value):
                walk(f"{prefix}[{i}]", val)
        else:
            out[prefix] = int(value) if isinstance(value, bool) else value

    walk("", args)
    return out


class LMSAuthError(Exception):
    """Authentication/session against the LMS failed (e.g. expired session)."""


class LMSUpstreamError(Exception):
    """The NUST LMS is unreachable or returned an unusable response (vs. bad creds)."""


class LMSAjaxError(Exception):
    """A Moodle AJAX method returned an error/exception."""

    def __init__(self, detail: Any) -> None:
        self.detail = detail
        super().__init__(str(detail))


class LMSSession:
    def __init__(self) -> None:
        base = settings.lms_base_url.rstrip("/")
        self.login_url = f"{base}/login/index.php"
        self.ajax_url = f"{base}/lib/ajax/service.php"
        self.dashboard_url = f"{base}/my/"
        self.token_url = f"{base}/login/token.php"
        self.rest_url = f"{base}/webservice/rest/server.php"
        self._sesskey: str | None = None
        self._token: str | None = None
        self.client = httpx.AsyncClient(
            follow_redirects=True,
            verify=settings.lms_verify_ssl,
            timeout=30.0,
            headers={"User-Agent": settings.lms_user_agent},
        )

    async def login(self, username: str, password: str) -> bool:
        """Authenticate against NUST LMS.

        Returns True on success, False on *rejected credentials*. Raises
        LMSUpstreamError when the LMS is unreachable or returns an unusable response,
        so the caller can answer 502 (LMS down) instead of 401 (wrong password).
        """
        try:
            response = await self.client.get(self.login_url)
        except httpx.HTTPError as exc:
            raise LMSUpstreamError(f"Could not reach NUST LMS login page: {exc}") from exc

        token_element = BeautifulSoup(response.text, "html.parser").find(
            "input", {"name": "logintoken"}
        )
        if not token_element:
            raise LMSUpstreamError(
                f"NUST LMS login page returned no login token (status {response.status_code})."
            )

        payload = {
            "username": username,
            "password": password,
            "logintoken": token_element["value"],
        }
        try:
            login_response = await self.client.post(self.login_url, data=payload)
        except httpx.HTTPError as exc:
            raise LMSUpstreamError(f"NUST LMS login request failed: {exc}") from exc

        if login_response.status_code >= 500:
            raise LMSUpstreamError(
                f"NUST LMS returned {login_response.status_code} during login."
            )

        final_url = str(login_response.url)
        # Genuine credential rejection: back on the login page with an error.
        if "login/index.php" in final_url and (
            "error=" in login_response.text or "Invalid login" in login_response.text
        ):
            logger.warning("LMS login rejected credentials for %s", username)
            return False

        # Success: redirected away from login, or a session cookie was set.
        if login_response.status_code in (200, 302, 303) and (
            "login/index.php" not in final_url
            or "MoodleSession" in str(self.client.cookies)
        ):
            logger.info("Authenticated %s with NUST LMS", username)
            await self._fetch_ws_token(username, password)  # best-effort; never raises
            return True

        logger.warning(
            "Login for %s ended in an unexpected state (url=%s, status=%s)",
            username, final_url, login_response.status_code,
        )
        return False

    async def _fetch_ws_token(self, username: str, password: str) -> None:
        """Best-effort: obtain a Moodle Web Service token for the mobile service.

        The token unlocks the token-based REST endpoint (webservice/rest/server.php),
        which exposes functions not available through lib/ajax/service.php — e.g.
        `core_course_get_contents`. If the LMS has web services disabled, this is a
        no-op and only the AJAX-backed endpoints remain available.
        """
        try:
            resp = await self.client.get(
                self.token_url,
                params={
                    "username": username,
                    "password": password,
                    "service": "moodle_mobile_app",
                },
            )
            data = resp.json()
            self._token = data.get("token")
            if not self._token:
                logger.warning(
                    "No WS token returned; REST endpoints unavailable: %s",
                    data.get("error"),
                )
        except Exception as exc:  # noqa: BLE001 — REST simply stays unavailable
            logger.warning("WS token fetch failed; REST endpoints unavailable: %s", exc)

    async def call_rest(self, method: str, args: dict[str, Any]) -> Any:
        """Invoke a Moodle external function via the token-based REST endpoint.

        Used for functions not exposed through the AJAX service. Returns the parsed
        JSON result; raises LMSAjaxError on a Moodle exception, or LMSAuthError if no
        token was obtained at login.
        """
        if not self._token:
            raise LMSAuthError(
                "No web service token for this session; REST functions are unavailable."
            )
        params = {
            "wstoken": self._token,
            "wsfunction": method,
            "moodlewsrestformat": "json",
        }
        resp = await self.client.post(
            self.rest_url, params=params, data=_flatten_params(args)
        )
        resp.raise_for_status()
        result = resp.json()
        # REST errors arrive as HTTP 200 with an {exception, errorcode, message} body.
        if isinstance(result, dict) and result.get("exception"):
            raise LMSAjaxError(result)
        return result

    async def get_sesskey(self) -> str | None:
        """Extract the sesskey for AJAX calls from the dashboard HTML."""
        try:
            response = await self.client.get(self.dashboard_url)
            if '"sesskey":"' in response.text:
                return response.text.split('"sesskey":"')[1].split('"')[0]
            return None
        except Exception:  # noqa: BLE001
            return None

    async def _ensure_sesskey(self) -> str:
        if not self._sesskey:
            self._sesskey = await self.get_sesskey()
        if not self._sesskey:
            raise LMSAuthError("Could not obtain sesskey; the LMS session may have expired.")
        return self._sesskey

    async def call_ajax(self, method: str, args: dict[str, Any]) -> Any:
        """Invoke a Moodle AJAX service method with the authenticated session.

        Mirrors Moodle's lib/ajax/service.php convention: POST a single-item array
        of {index, methodname, args} with ?sesskey=...&info=method. Refreshes the
        sesskey and retries once if Moodle reports it stale.
        """
        return await self._call_ajax(method, args, retry=True)

    async def _call_ajax(self, method: str, args: dict[str, Any], retry: bool) -> Any:
        sesskey = await self._ensure_sesskey()
        params = {"sesskey": sesskey, "info": method}
        payload = [{"index": 0, "methodname": method, "args": args}]

        resp = await self.client.post(self.ajax_url, params=params, json=payload)
        resp.raise_for_status()
        item = resp.json()[0]

        if item.get("error"):
            exception = item.get("exception") or item
            if retry and isinstance(exception, dict) and exception.get("errorcode") == "invalidsesskey":
                self._sesskey = None  # force a refresh and retry once
                return await self._call_ajax(method, args, retry=False)
            raise LMSAjaxError(exception)

        return item.get("data")

    async def get_user_full_name(self) -> str:
        """Best-effort display name: Moodle AJAX first, then HTML scrape."""
        try:
            data = await self.call_ajax("core_webservice_get_site_info", {})
            fullname = (data or {}).get("fullname", "")
            if fullname:
                return fullname.strip()
        except Exception as exc:  # noqa: BLE001
            logger.warning("Name via Moodle API failed, falling back to scrape: %s", exc)

        try:
            response = await self.client.get(self.dashboard_url)
            soup = BeautifulSoup(response.text, "html.parser")
            selectors = [
                ("span", {"class": "usertext"}),
                ("div", {"class": "usertext"}),
                ("span", {"class": "username"}),
                ("div", {"class": "page-header-headings"}),
            ]
            for tag, attrs in selectors:
                el = soup.find(tag, attrs)
                if el and el.text.strip():
                    return el.text.strip()
        except Exception as exc:  # noqa: BLE001
            logger.warning("HTML name scrape failed: %s", exc)

        return "NUST Student"

    async def close(self) -> None:
        await self.client.aclose()
