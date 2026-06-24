"""MCP (Model Context Protocol) server for the NUST LMS gateway.

Exposes the read endpoints as MCP tools so AI assistants (Claude Desktop, Cursor,
etc.) can call the LMS on a student's behalf — e.g. "what are my deadlines this
week?". This module is mounted into the FastAPI app at /mcp (see main.py), so it
runs in the same process and shares the same in-memory LMS sessions.

Auth: we deliberately do NOT expose a login tool — the LLM never sees credentials.
The student logs in once via POST /auth/login, gets a JWT, and configures it in
their MCP client. Each tool reads that JWT from the incoming Authorization header
and resolves it to the live LMSSession using the same rule as the REST routes.
"""
from typing import Any

from fastmcp import FastMCP
from fastmcp.server.dependencies import get_http_headers

from app.dependencies import resolve_session_from_token
from app.schemas.service import (
    CourseTimelineClassification,
    CourseTimelineSortField,
)
from app.services.lms_session import LMSSession
from app.services.session_store import get_session_store

mcp = FastMCP("NUST LMS")


async def _session() -> LMSSession:
    """Resolve the current MCP caller's bearer token to their live LMS session.

    The token arrives as `Authorization: Bearer <JWT>` on the MCP HTTP request;
    we reuse the gateway's shared resolver so MCP and REST enforce auth identically.
    Note: get_http_headers() strips `authorization` by default, so we must opt it
    back in via `include`.
    """
    headers = get_http_headers(include={"authorization"})
    token = (headers.get("authorization") or "").removeprefix("Bearer ").strip()
    return await resolve_session_from_token(token, get_session_store())


@mcp.tool
async def list_recent_courses(limit: int = 10) -> Any:
    """List the student's most recently accessed courses, newest first.

    Use this to answer questions like "what courses am I taking?" or "what did I
    open last." `limit` caps how many courses are returned.
    """
    session = await _session()
    return await session.call_ajax("core_course_get_recent_courses", {"limit": limit})


@mcp.tool
async def list_courses_by_timeline(
    classification: CourseTimelineClassification = CourseTimelineClassification.inprogress,
    sort: CourseTimelineSortField = CourseTimelineSortField.fullname,
    offset: int = 0,
    limit: int = 50,
) -> Any:
    """List the student's enrolled courses filtered by timeline status.

    `classification` selects which courses: `inprogress` (current), `past`,
    `future`, `favourites`, `hidden`, `all`, or `allincludinghidden`. `sort`
    orders them (e.g. by `fullname` or `timeaccess`). Use this for "what courses
    am I currently enrolled in?" or "show my favourite courses."
    """
    session = await _session()
    return await session.call_ajax(
        "core_course_get_enrolled_courses_by_timeline_classification",
        {
            "classification": classification.value,
            "sort": sort.value,
            "offset": offset,
            "limit": limit,
        },
    )


@mcp.tool
async def list_upcoming_deadlines(
    limitnum: int = 20,
    timesortfrom: int = 0,
    timesortto: int | None = None,
    aftereventid: int | None = None,
) -> Any:
    """List deadlines (assignment/quiz/lab due dates) across all courses, by time.

    On NUST LMS these are calendar "action events". Pass `timesortfrom` as a Unix
    timestamp to only see events at or after that time (e.g. the current epoch for
    upcoming-only); pass 0 for no lower bound. `limitnum` caps the count. Use this
    for "what's due this week?" or "what are my upcoming deadlines?".
    """
    args: dict[str, Any] = {"limitnum": limitnum, "timesortfrom": timesortfrom}
    if timesortto is not None:
        args["timesortto"] = timesortto
    if aftereventid is not None:
        args["aftereventid"] = aftereventid
    session = await _session()
    return await session.call_ajax(
        "core_calendar_get_action_events_by_timesort", args
    )


@mcp.tool
async def list_course_deadlines(
    courseid: int,
    timesortfrom: int | None = None,
    timesortto: int | None = None,
    aftereventid: int | None = None,
    limitnum: int | None = None,
) -> Any:
    """List deadlines/action events for one specific course.

    Same as upcoming deadlines but scoped to a single `courseid` (get the id from
    list_recent_courses or list_courses_by_timeline). Use for "what's due in my
    Operating Systems course?".
    """
    args: dict[str, Any] = {"courseid": courseid}
    for key, value in (
        ("timesortfrom", timesortfrom),
        ("timesortto", timesortto),
        ("aftereventid", aftereventid),
        ("limitnum", limitnum),
    ):
        if value is not None:
            args[key] = value
    session = await _session()
    return await session.call_ajax(
        "core_calendar_get_action_events_by_course", args
    )


@mcp.tool
async def get_site_notifications(contextid: int) -> Any:
    """Fetch pending site-level notifications for a Moodle context.

    Returns an empty list when there are none. `contextid` is the Moodle context
    ID (the user context id appears in the profile image URL path).
    """
    session = await _session()
    return await session.call_ajax("core_fetch_notifications", {"contextid": contextid})


@mcp.tool
async def list_popup_notifications(useridto: str, limit: int = 20, offset: int = 0) -> Any:
    """List the student's recent popup notifications and unread count.

    `useridto` is the recipient user id (as a string). Use for "do I have any new
    notifications?" or "what did I miss on the LMS?". Supports pagination via
    `limit`/`offset`.
    """
    session = await _session()
    return await session.call_ajax(
        "message_popup_get_popup_notifications",
        {"useridto": useridto, "limit": limit, "offset": offset},
    )
