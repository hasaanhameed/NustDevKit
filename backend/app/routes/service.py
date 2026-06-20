"""Proxied LMS service routes.

These are reads, so they're exposed as GET with query parameters. The gateway
translates each into the underlying Moodle AJAX call — which Moodle requires to be
a POST — via `LMSSession.call_ajax`. Each endpoint requires a valid bearer token
(resolved to a server-side LMS session).
"""
from typing import Annotated, Any

from fastapi import APIRouter, Depends, Query

from app.dependencies import get_current_session
from app.schemas.service import (
    FetchNotificationsRequest,
    GetCalendarEventsByCourseRequest,
    GetCalendarEventsByTimesortRequest,
    GetEnrolledCoursesByTimelineRequest,
    GetPopupNotificationsRequest,
    GetRecentCoursesRequest,
    GetUserPreferencesRequest,
    GetUsersByFieldRequest,
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


@router.get("/core_fetch_notifications")
async def fetch_notifications(
    params: Annotated[FetchNotificationsRequest, Query()],
    session: LMSSession = Depends(get_current_session),
) -> Any:
    return await session.call_ajax(
        "core_fetch_notifications", params.model_dump(exclude_none=True)
    )


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


@router.get("/core_user_get_users_by_field")
async def get_users_by_field(
    params: Annotated[GetUsersByFieldRequest, Query()],
    session: LMSSession = Depends(get_current_session),
) -> Any:
    return await session.call_ajax(
        "core_user_get_users_by_field", params.model_dump(exclude_none=True)
    )


@router.get("/core_user_get_user_preferences")
async def get_user_preferences(
    params: Annotated[GetUserPreferencesRequest, Query()],
    session: LMSSession = Depends(get_current_session),
) -> Any:
    return await session.call_ajax(
        "core_user_get_user_preferences", params.model_dump(exclude_none=True)
    )


@router.get("/message_popup_get_popup_notifications")
async def get_popup_notifications(
    params: Annotated[GetPopupNotificationsRequest, Query()],
    session: LMSSession = Depends(get_current_session),
) -> Any:
    return await session.call_ajax(
        "message_popup_get_popup_notifications", params.model_dump(exclude_none=True)
    )
