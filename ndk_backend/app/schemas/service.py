"""Request schemas for the proxied LMS service endpoints.

These mirror the request bodies in the canonical OpenAPI spec
(src/spec/openapi.yaml). Each maps 1:1 to a Moodle AJAX method; the route layer
forwards `model_dump(exclude_none=True)` as the method args.
"""
from enum import Enum

from pydantic import BaseModel, Field


class CourseTimelineClassification(str, Enum):
    all = "all"
    inprogress = "inprogress"
    past = "past"
    future = "future"
    favourites = "favourites"
    hidden = "hidden"
    allincludinghidden = "allincludinghidden"


class CourseTimelineSortField(str, Enum):
    fullname = "fullname"
    shortname = "shortname"
    id = "id"
    idnumber = "idnumber"
    timeaccess = "timeaccess"


class GetRecentCoursesRequest(BaseModel):
    limit: int = Field(default=10, description="Maximum number of courses to return.")


class GetEnrolledCoursesByTimelineRequest(BaseModel):
    offset: int = Field(default=0, description="Zero-based pagination offset.")
    limit: int = Field(default=50, description="Maximum number of courses to return.")
    classification: CourseTimelineClassification
    sort: CourseTimelineSortField


class GetCourseContentsRequest(BaseModel):
    courseid: int = Field(..., description="ID of the course whose contents to retrieve.")


class GetCalendarEventsByTimesortRequest(BaseModel):
    limitnum: int = Field(..., description="Maximum number of events to return.")
    timesortfrom: int = Field(..., description="Only events with timesort >= this Unix timestamp.")
    timesortto: int | None = Field(default=None, description="Only events with timesort <= this timestamp.")
    aftereventid: int | None = Field(default=None, description="Cursor: events with ID greater than this.")


class GetCalendarEventsByCourseRequest(BaseModel):
    courseid: int = Field(..., description="ID of the course to fetch events for.")
    timesortfrom: int | None = None
    timesortto: int | None = None
    aftereventid: int | None = None
    limitnum: int | None = None


class GetPopupNotificationsRequest(BaseModel):
    useridto: str = Field(..., description="ID of the recipient user, as a string.")
    limit: int
    offset: int
