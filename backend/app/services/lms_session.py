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


class LMSAuthError(Exception):
    """Authentication/session against the LMS failed (e.g. expired session)."""


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
        self._sesskey: str | None = None
        self.client = httpx.AsyncClient(
            follow_redirects=True,
            verify=settings.lms_verify_ssl,
            timeout=30.0,
            headers={"User-Agent": settings.lms_user_agent},
        )

    async def login(self, username: str, password: str) -> bool:
        """Log into NUST LMS; returns True on success, False on bad credentials."""
        try:
            # 1. Fetch fresh login page to obtain the CSRF logintoken.
            response = await self.client.get(self.login_url)
            soup = BeautifulSoup(response.text, "html.parser")
            token_element = soup.find("input", {"name": "logintoken"})
            if not token_element:
                logger.error(
                    "Could not find login token on NUST LMS page (status %s)",
                    response.status_code,
                )
                return False
            login_token = token_element["value"]

            # 2. Submit credentials.
            payload = {
                "username": username,
                "password": password,
                "logintoken": login_token,
            }
            login_response = await self.client.post(self.login_url, data=payload)

            # Explicit rejection: still on the login page with an error.
            final_url = str(login_response.url)
            if "login/index.php" in final_url and (
                "error=" in login_response.text or "Invalid login" in login_response.text
            ):
                logger.warning("LMS login rejected credentials for %s", username)
                return False

            # Success: redirected away from login, or a session cookie is set.
            if login_response.status_code in (200, 302, 303):
                if "login/index.php" not in final_url or "MoodleSession" in str(
                    self.client.cookies
                ):
                    logger.info("Authenticated %s with NUST LMS", username)
                    return True

            logger.warning(
                "Login failed for %s — final URL %s, status %s",
                username, login_response.url, login_response.status_code,
            )
            return False
        except Exception as exc:  # noqa: BLE001 — surface as auth failure to caller
            logger.error("Critical error during LMS login: %s", exc)
            return False

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
