"""MCP tools for the user's account / identity."""
from typing import Any

from fastmcp import FastMCP

from app.mcp.context import current_session


def register(mcp: FastMCP) -> None:
    @mcp.tool
    async def get_my_account() -> Any:
        """Get the current user's identity and site info (user ID, name, username).

        Use this first to discover the student's own numeric user ID, which other
        tools need — e.g. it's the `useridto` for list_popup_notifications. Also
        returns full name, username, profile picture, and basic site details.
        """
        session = await current_session()
        # REST-only function (not exposed via the AJAX service).
        return await session.call_rest("core_webservice_get_site_info", {})
