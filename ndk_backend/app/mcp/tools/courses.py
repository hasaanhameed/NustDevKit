"""MCP tools for courses."""
from typing import Any

from fastmcp import FastMCP

from app.mcp.context import current_session
from app.schemas.service import CourseTimelineClassification, CourseTimelineSortField


def register(mcp: FastMCP) -> None:
    @mcp.tool
    async def list_recent_courses(limit: int = 10) -> Any:
        """List the student's most recently accessed courses, newest first.

        Use this to answer questions like "what courses am I taking?" or "what did
        I open last." `limit` caps how many courses are returned.
        """
        session = await current_session()
        return await session.call_ajax(
            "core_course_get_recent_courses", {"limit": limit}
        )

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
        session = await current_session()
        return await session.call_ajax(
            "core_course_get_enrolled_courses_by_timeline_classification",
            {
                "classification": classification.value,
                "sort": sort.value,
                "offset": offset,
                "limit": limit,
            },
        )
