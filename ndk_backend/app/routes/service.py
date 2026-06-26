"""Proxied LMS read endpoints (GET), each backed by an LMSSession transport call."""
from typing import Annotated, Any

from fastapi import APIRouter, Depends, Query

from app.dependencies import get_current_session
from app.schemas.service import (
    GetCalendarEventsByCourseRequest,
    GetCalendarEventsByTimesortRequest,
    GetCourseContentsRequest,
    GetEnrolledCoursesByTimelineRequest,
    GetPopupNotificationsRequest,
    GetRecentCoursesRequest,
)
from app.services.lms_session import LMSSession

router = APIRouter(prefix="/service", tags=["LMS"])


@router.get("/core_course_get_recent_courses")
async def get_recent_courses(
    params: Annotated[GetRecentCoursesRequest, Query()],
    session: LMSSession = Depends(get_current_session),
) -> Any:
    return await session.call_ajax(
        "core_course_get_recent_courses", params.model_dump(exclude_none=True)
    )


@router.get("/core_course_get_enrolled_courses_by_timeline_classification")
async def get_enrolled_courses_by_timeline(
    params: Annotated[GetEnrolledCoursesByTimelineRequest, Query()],
    session: LMSSession = Depends(get_current_session),
) -> Any:
    return await session.call_ajax(
        "core_course_get_enrolled_courses_by_timeline_classification",
        params.model_dump(exclude_none=True),
    )


@router.get("/core_course_get_contents")
async def get_course_contents(
    params: Annotated[GetCourseContentsRequest, Query()],
    session: LMSSession = Depends(get_current_session),
) -> Any:
    # REST transport — this function isn't exposed via the AJAX service.
    return await session.call_rest(
        "core_course_get_contents", params.model_dump(exclude_none=True)
    )


@router.get("/core_webservice_get_site_info")
async def get_site_info(
    session: LMSSession = Depends(get_current_session),
) -> Any:
    # REST-only function (not on the AJAX service).
    return await session.call_rest("core_webservice_get_site_info", {})


@router.get("/core_calendar_get_action_events_by_timesort")
async def get_calendar_events_by_timesort(
    params: Annotated[GetCalendarEventsByTimesortRequest, Query()],
    session: LMSSession = Depends(get_current_session),
) -> Any:
    return await session.call_ajax(
        "core_calendar_get_action_events_by_timesort",
        params.model_dump(exclude_none=True),
    )


@router.get("/core_calendar_get_action_events_by_course")
async def get_calendar_events_by_course(
    params: Annotated[GetCalendarEventsByCourseRequest, Query()],
    session: LMSSession = Depends(get_current_session),
) -> Any:
    return await session.call_ajax(
        "core_calendar_get_action_events_by_course",
        params.model_dump(exclude_none=True),
    )


@router.get("/message_popup_get_popup_notifications")
async def get_popup_notifications(
    params: Annotated[GetPopupNotificationsRequest, Query()],
    session: LMSSession = Depends(get_current_session),
) -> Any:
    return await session.call_ajax(
        "message_popup_get_popup_notifications", params.model_dump(exclude_none=True)
    )
