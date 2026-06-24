"""MCP tools for notifications."""
from typing import Any

from fastmcp import FastMCP

from app.mcp.context import current_session


def register(mcp: FastMCP) -> None:
    @mcp.tool
    async def list_popup_notifications(
        useridto: str, limit: int = 20, offset: int = 0
    ) -> Any:
        """List the student's recent popup (bell) notifications and unread count.

        These are real notifications — assignment graded, forum reply, deadline
        reminders. `useridto` is the student's own user id (as a string); get it from
        the get_my_account tool if you don't have it. Use for "do I have any new
        notifications?" or "what did I miss on the LMS?". Supports `limit`/`offset`.
        """
        session = await current_session()
        return await session.call_ajax(
            "message_popup_get_popup_notifications",
            {"useridto": useridto, "limit": limit, "offset": offset},
        )
