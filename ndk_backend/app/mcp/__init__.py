"""MCP (Model Context Protocol) server for the NUST LMS gateway.

Exposes the read endpoints as MCP tools so AI assistants (Claude Desktop, Cursor,
ChatGPT connectors, etc.) can call the LMS on a student's behalf. Mounted into the
FastAPI app at /mcp (see main.py).

Auth: there is deliberately no login tool — the LLM never sees credentials. The
student logs in once via POST /auth/login, gets a JWT, and configures it in their
MCP client; each tool resolves that token to the caller's live LMS session.
"""
from app.mcp.server import mcp

__all__ = ["mcp"]
