"""MCP tools for notifications."""
from typing import Any

from fastmcp import FastMCP

from app.mcp.context import current_session


def register(mcp: FastMCP) -> None:
    @mcp.tool
    async def get_site_notifications(contextid: int) -> Any:
        """Fetch pending site-level notifications for a Moodle context.

        Returns an empty list when there are none. `contextid` is the Moodle context
        ID (the user context id appears in the profile image URL path).
        """
        session = await current_session()
        return await session.call_ajax(
            "core_fetch_notifications", {"contextid": contextid}
        )

    @mcp.tool
    async def list_popup_notifications(
        useridto: str, limit: int = 20, offset: int = 0
    ) -> Any:
        """List the student's recent popup notifications and unread count.

        `useridto` is the recipient user id (as a string). Use for "do I have any new
        notifications?" or "what did I miss on the LMS?". Supports pagination via
        `limit`/`offset`.
        """
        session = await current_session()
        return await session.call_ajax(
            "message_popup_get_popup_notifications",
            {"useridto": useridto, "limit": limit, "offset": offset},
        )
