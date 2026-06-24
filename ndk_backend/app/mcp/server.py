"""MCP server assembly.

Creates the FastMCP instance and registers each domain's tools onto it. Tools are
grouped by domain (mirroring the REST routes) and wired in via each module's
`register(mcp)` function — the MCP analog of including routers.
"""
from fastmcp import FastMCP

from app.mcp.tools import account, calendar, courses, notifications

mcp = FastMCP("NUST LMS")

account.register(mcp)
courses.register(mcp)
calendar.register(mcp)
notifications.register(mcp)
