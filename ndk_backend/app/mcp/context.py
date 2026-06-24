"""Per-request context for MCP tools.

`current_session()` resolves the caller's bearer token (carried on the incoming
MCP HTTP request) to their live, server-side LMS session — reusing the gateway's
shared resolver so MCP and the REST routes enforce auth identically.
"""
from fastmcp.server.dependencies import get_http_headers

from app.dependencies import resolve_session_from_token
from app.services.lms_session import LMSSession
from app.services.session_store import get_session_store


async def current_session() -> LMSSession:
    """Resolve the current MCP caller's bearer token to their live LMS session.

    The token arrives as `Authorization: Bearer <JWT>`. get_http_headers() strips
    `authorization` by default, so we must opt it back in via `include`.
    """
    headers = get_http_headers(include={"authorization"})
    token = (headers.get("authorization") or "").removeprefix("Bearer ").strip()
    return await resolve_session_from_token(token, get_session_store())
