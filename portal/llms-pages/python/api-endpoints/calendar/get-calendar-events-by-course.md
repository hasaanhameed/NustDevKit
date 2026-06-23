# Get Calendar Events by Course

Source: /#/python/x-redirect/JTI0ZSUyRkNhbGVuZGFyJTJGZ2V0Q2FsZW5kYXJFdmVudHNCeUNvdXJzZQ

Returns all action events (deadlines) for a single course — assignment, lab, and quiz submission due dates, and other dated activities.
Moodle method: `core_calendar_get_action_events_by_course`

```python
def get_calendar_events_by_course(self,
                                 courseid,
                                 timesortfrom=None,
                                 timesortto=None,
                                 aftereventid=None,
                                 limitnum=None)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/python/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `courseid` | `int` | Query, Required | ID of the course to fetch events for. |
| `timesortfrom` | `int` | Query, Optional | Only return events with timesort >= this Unix timestamp. |
| `timesortto` | `int` | Query, Optional | Only return events with timesort <= this Unix timestamp. |
| `aftereventid` | `int` | Query, Optional | Cursor-based pagination — return events after this event ID. |
| `limitnum` | `int` | Query, Optional | Maximum number of events to return. |


# Response Type

**200**: Calendar events for the specified course.

This method returns an [`ApiResponse`](/llms-pages/python/sdk-infrastructure/utilities/apiresponse.md) instance. The `body` property of this instance returns the response data which is of type [`CalendarEventsResponse`](/llms-pages/python/models/structures/calendar-events-response.md).


# Example Usage

```python
courseid = 74

result = calendar_api.get_calendar_events_by_course(courseid)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleErrorException`](/llms-pages/python/models/exceptions/moodle-error.md) |



