# Get Calendar Events by Course Request

Source: /#/python/x-redirect/JTI0bSUyRkdldENhbGVuZGFyRXZlbnRzQnlDb3Vyc2VSZXF1ZXN0

Request parameters for retrieving calendar action events for a specific course.

*This model accepts additional fields of type Any.*


# Class Name

`GetCalendarEventsByCourseRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `courseid` | `int` | Required | ID of the course to fetch events for. |
| `timesortfrom` | `int` | Optional | Only return events with timesort >= this Unix timestamp. Optional. |
| `timesortto` | `int` | Optional | Only return events with timesort <= this Unix timestamp. Optional. |
| `aftereventid` | `int` | Optional | Cursor-based pagination — return events after this event ID. Optional. |
| `limitnum` | `int` | Optional | Maximum number of events to return. Optional. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |


# Example

```python
import jsonpickle

from nustlmsapi.models.get_calendar_events_by_course_request import GetCalendarEventsByCourseRequest

get_calendar_events_by_course_request = GetCalendarEventsByCourseRequest(
    courseid=49906,
    timesortfrom=188,
    timesortto=184,
    aftereventid=182,
    limitnum=94,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```



