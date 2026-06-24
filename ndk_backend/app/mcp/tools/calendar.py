"""MCP tools for calendar / deadlines."""
from typing import Any

from fastmcp import FastMCP

from app.mcp.context import current_session


def register(mcp: FastMCP) -> None:
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
        session = await current_session()
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
        session = await current_session()
        return await session.call_ajax(
            "core_calendar_get_action_events_by_course", args
        )
