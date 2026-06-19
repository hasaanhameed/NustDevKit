# Get Calendar Events by Timesort

Source: /#/python/x-redirect/JTI0ZSUyRkNhbGVuZGFyJTJGZ2V0Q2FsZW5kYXJFdmVudHNCeVRpbWVzb3J0

Returns action events across all enrolled courses, ordered by their sort timestamp. Use `timesortfrom` to filter to upcoming events only.
Moodle method: `core_calendar_get_action_events_by_timesort`

```python
def get_calendar_events_by_timesort(self,
                                   body)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/python/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetCalendarEventsByTimesortRequest`](/llms-pages/python/models/structures/get-calendar-events-by-timesort-request.md) | Body, Required | Parameters for the time-sorted calendar events request. |


# Response Type

**200**: Calendar events sorted by timesort.

This method returns an [`ApiResponse`](/llms-pages/python/sdk-infrastructure/utilities/apiresponse.md) instance. The `body` property of this instance returns the response data which is of type [`CalendarEventsResponse`](/llms-pages/python/models/structures/calendar-events-response.md).


# Example Usage

```python
body = GetCalendarEventsByTimesortRequest(
    limitnum=20,
    timesortfrom=0
)

result = calendar_api.get_calendar_events_by_timesort(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleErrorException`](/llms-pages/python/models/exceptions/moodle-error.md) |



