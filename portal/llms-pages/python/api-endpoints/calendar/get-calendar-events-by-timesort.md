# Get Calendar Events by Timesort

Source: /#/python/x-redirect/JTI0ZSUyRkNhbGVuZGFyJTJGZ2V0Q2FsZW5kYXJFdmVudHNCeVRpbWVzb3J0

Returns action events (deadlines) across all enrolled courses, ordered by their sort timestamp. On NUST LMS these are submission due dates for assignments, labs, quizzes, and similar dated activities. Use `timesortfrom` to filter to upcoming deadlines only.
Moodle method: `core_calendar_get_action_events_by_timesort`

```python
def get_calendar_events_by_timesort(self,
                                   limitnum,
                                   timesortfrom,
                                   timesortto=None,
                                   aftereventid=None)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/python/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limitnum` | `int` | Query, Required | Maximum number of events to return. |
| `timesortfrom` | `int` | Query, Required | Only return events with timesort >= this Unix timestamp. Pass 0 for no lower bound. |
| `timesortto` | `int` | Query, Optional | Only return events with timesort <= this Unix timestamp. |
| `aftereventid` | `int` | Query, Optional | Return events whose ID is greater than this value (cursor pagination). |


# Response Type

**200**: Calendar events sorted by timesort.

This method returns an [`ApiResponse`](/llms-pages/python/sdk-infrastructure/utilities/apiresponse.md) instance. The `body` property of this instance returns the response data which is of type [`CalendarEventsResponse`](/llms-pages/python/models/structures/calendar-events-response.md).


# Example Usage

```python
limitnum = 32

timesortfrom = 58

result = calendar_api.get_calendar_events_by_timesort(
    limitnum,
    timesortfrom
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleErrorException`](/llms-pages/python/models/exceptions/moodle-error.md) |



