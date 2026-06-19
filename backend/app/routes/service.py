"""Proxied LMS service routes.

Each endpoint mirrors a path in the canonical OpenAPI spec, requires a valid
bearer token (resolved to a server-side LMS session), and forwards the call to
the corresponding Moodle AJAX method via `LMSSession.call_ajax`.
"""
from typing import Any

from fastapi import APIRouter, Depends

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


@router.post("/core_course_get_recent_courses")
async def get_recent_courses(
    body: GetRecentCoursesRequest,
    session: LMSSession = Depends(get_current_session),
) -> Any:
    return await session.call_ajax(
        "core_course_get_recent_courses", body.model_dump(exclude_none=True)
    )


@router.post("/core_course_get_enrolled_courses_by_timeline_classification")
async def get_enrolled_courses_by_timeline(
    body: GetEnrolledCoursesByTimelineRequest,
    session: LMSSession = Depends(get_current_session),
) -> Any:
    return await session.call_ajax(
        "core_course_get_enrolled_courses_by_timeline_classification",
        body.model_dump(exclude_none=True),
    )


@router.post("/core_fetch_notifications")
async def fetch_notifications(
    body: FetchNotificationsRequest,
    session: LMSSession = Depends(get_current_session),
) -> Any:
    return await session.call_ajax(
        "core_fetch_notifications", body.model_dump(exclude_none=True)
    )


@router.post("/core_calendar_get_action_events_by_timesort")
async def get_calendar_events_by_timesort(
    body: GetCalendarEventsByTimesortRequest,
    session: LMSSession = Depends(get_current_session),
) -> Any:
    return await session.call_ajax(
        "core_calendar_get_action_events_by_timesort",
        body.model_dump(exclude_none=True),
    )


@router.post("/core_calendar_get_action_events_by_course")
async def get_calendar_events_by_course(
    body: GetCalendarEventsByCourseRequest,
    session: LMSSession = Depends(get_current_session),
) -> Any:
    return await session.call_ajax(
        "core_calendar_get_action_events_by_course",
        body.model_dump(exclude_none=True),
    )


@router.post("/core_user_get_users_by_field")
async def get_users_by_field(
    body: GetUsersByFieldRequest,
    session: LMSSession = Depends(get_current_session),
) -> Any:
    return await session.call_ajax(
        "core_user_get_users_by_field", body.model_dump(exclude_none=True)
    )


@router.post("/core_user_get_user_preferences")
async def get_user_preferences(
    body: GetUserPreferencesRequest,
    session: LMSSession = Depends(get_current_session),
) -> Any:
    return await session.call_ajax(
        "core_user_get_user_preferences", body.model_dump(exclude_none=True)
    )


@router.post("/message_popup_get_popup_notifications")
async def get_popup_notifications(
    body: GetPopupNotificationsRequest,
    session: LMSSession = Depends(get_current_session),
) -> Any:
    return await session.call_ajax(
        "message_popup_get_popup_notifications", body.model_dump(exclude_none=True)
    )
