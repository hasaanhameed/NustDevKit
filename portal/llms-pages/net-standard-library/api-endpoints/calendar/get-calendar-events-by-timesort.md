# Get Calendar Events by Timesort

Source: /#/net-standard-library/x-redirect/JTI0ZSUyRkNhbGVuZGFyJTJGZ2V0Q2FsZW5kYXJFdmVudHNCeVRpbWVzb3J0

Returns action events across all enrolled courses, ordered by their sort timestamp. Use `timesortfrom` to filter to upcoming events only.
Moodle method: `core_calendar_get_action_events_by_timesort`

```csharp
GetCalendarEventsByTimesortAsync(
    Models.GetCalendarEventsByTimesortRequest body)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/net-standard-library/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetCalendarEventsByTimesortRequest`](/llms-pages/net-standard-library/models/structures/get-calendar-events-by-timesort-request.md) | Body, Required | Parameters for the time-sorted calendar events request. |


# Response Type

**200**: Calendar events sorted by timesort.

This method returns an [`ApiResponse`](/llms-pages/net-standard-library/sdk-infrastructure/utilities/apiresponse.md) instance. The `Data` property of this instance returns the response data which is of type [Models.CalendarEventsResponse](/llms-pages/net-standard-library/models/structures/calendar-events-response.md).


# Example Usage

```csharp
GetCalendarEventsByTimesortRequest body = new GetCalendarEventsByTimesortRequest
{
    Limitnum = 20,
    Timesortfrom = 0,
};

try
{
    ApiResponse<CalendarEventsResponse> result = await calendarApi.GetCalendarEventsByTimesortAsync(body);
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



