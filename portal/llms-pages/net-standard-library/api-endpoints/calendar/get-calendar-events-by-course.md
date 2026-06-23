# Get Calendar Events by Course

Source: /#/net-standard-library/x-redirect/JTI0ZSUyRkNhbGVuZGFyJTJGZ2V0Q2FsZW5kYXJFdmVudHNCeUNvdXJzZQ

Returns all action events (deadlines) for a single course — assignment, lab, and quiz submission due dates, and other dated activities.
Moodle method: `core_calendar_get_action_events_by_course`

```csharp
GetCalendarEventsByCourseAsync(
    int courseid,
    int? timesortfrom = null,
    int? timesortto = null,
    int? aftereventid = null,
    int? limitnum = null)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/net-standard-library/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `courseid` | `int` | Query, Required | ID of the course to fetch events for. |
| `timesortfrom` | `int?` | Query, Optional | Only return events with timesort >= this Unix timestamp. |
| `timesortto` | `int?` | Query, Optional | Only return events with timesort <= this Unix timestamp. |
| `aftereventid` | `int?` | Query, Optional | Cursor-based pagination — return events after this event ID. |
| `limitnum` | `int?` | Query, Optional | Maximum number of events to return. |


# Response Type

**200**: Calendar events for the specified course.

This method returns an [`ApiResponse`](/llms-pages/net-standard-library/sdk-infrastructure/utilities/apiresponse.md) instance. The `Data` property of this instance returns the response data which is of type [Models.CalendarEventsResponse](/llms-pages/net-standard-library/models/structures/calendar-events-response.md).


# Example Usage

```csharp
int courseid = 74;
try
{
    ApiResponse<CalendarEventsResponse> result = await calendarApi.GetCalendarEventsByCourseAsync(courseid);
}
catch (ApiException e)
{
    Console.WriteLine(e.Message);
    if (e is MoodleErrorException)
    {
       // TODO: Handle MoodleErrorException exception here
    }
}
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleErrorException`](/llms-pages/net-standard-library/models/exceptions/moodle-error.md) |



