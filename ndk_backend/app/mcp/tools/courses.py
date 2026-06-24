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

    @mcp.tool
    async def list_course_contents(courseid: int) -> Any:
        """List everything posted in a course — sections, activities, and uploaded files.

        Returns the course's weeks/topics and the items in each (files, pages, URLs,
        assignments, ...), with file names and download URLs. Get `courseid` from
        list_recent_courses or list_courses_by_timeline. Use for "what readings are
        posted in my OS course?" or "what files are in week 3?".

        (File URLs need the session/token to actually download; names and metadata
        come back directly.)
        """
        session = await current_session()
        # Not an AJAX-enabled Moodle function — goes through the token-based REST
        # transport, same as the REST route.
        return await session.call_rest("core_course_get_contents", {"courseid": courseid})
