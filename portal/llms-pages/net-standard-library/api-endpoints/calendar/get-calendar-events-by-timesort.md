# Get Calendar Events by Timesort

Source: /#/net-standard-library/x-redirect/JTI0ZSUyRkNhbGVuZGFyJTJGZ2V0Q2FsZW5kYXJFdmVudHNCeVRpbWVzb3J0

Returns action events (deadlines) across all enrolled courses, ordered by their sort timestamp. On NUST LMS these are submission due dates for assignments, labs, quizzes, and similar dated activities. Use `timesortfrom` to filter to upcoming deadlines only.
Moodle method: `core_calendar_get_action_events_by_timesort`

```csharp
GetCalendarEventsByTimesortAsync(
    int limitnum,
    int timesortfrom,
    int? timesortto = null,
    int? aftereventid = null)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/net-standard-library/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limitnum` | `int` | Query, Required | Maximum number of events to return. |
| `timesortfrom` | `int` | Query, Required | Only return events with timesort >= this Unix timestamp. Pass 0 for no lower bound. |
| `timesortto` | `int?` | Query, Optional | Only return events with timesort <= this Unix timestamp. |
| `aftereventid` | `int?` | Query, Optional | Return events whose ID is greater than this value (cursor pagination). |


# Response Type

**200**: Calendar events sorted by timesort.

This method returns an [`ApiResponse`](/llms-pages/net-standard-library/sdk-infrastructure/utilities/apiresponse.md) instance. The `Data` property of this instance returns the response data which is of type [Models.CalendarEventsResponse](/llms-pages/net-standard-library/models/structures/calendar-events-response.md).


# Example Usage

```csharp
int limitnum = 32;
int timesortfrom = 58;
try
{
    ApiResponse<CalendarEventsResponse> result = await calendarApi.GetCalendarEventsByTimesortAsync(
        limitnum,
        timesortfrom
    );
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



