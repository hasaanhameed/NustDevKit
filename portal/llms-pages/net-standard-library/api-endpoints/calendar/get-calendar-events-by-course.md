# Get Calendar Events by Course

Source: /#/net-standard-library/x-redirect/JTI0ZSUyRkNhbGVuZGFyJTJGZ2V0Q2FsZW5kYXJFdmVudHNCeUNvdXJzZQ

Returns all action events (assignments, quizzes, etc.) for a single course.
Moodle method: `core_calendar_get_action_events_by_course`

```csharp
GetCalendarEventsByCourseAsync(
    Models.GetCalendarEventsByCourseRequest body)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/net-standard-library/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetCalendarEventsByCourseRequest`](/llms-pages/net-standard-library/models/structures/get-calendar-events-by-course-request.md) | Body, Required | Parameters for the course-specific calendar events request. |


# Response Type

**200**: Calendar events for the specified course.

This method returns an [`ApiResponse`](/llms-pages/net-standard-library/sdk-infrastructure/utilities/apiresponse.md) instance. The `Data` property of this instance returns the response data which is of type [Models.CalendarEventsResponse](/llms-pages/net-standard-library/models/structures/calendar-events-response.md).


# Example Usage

```csharp
GetCalendarEventsByCourseRequest body = new GetCalendarEventsByCourseRequest
{
    Courseid = 49906,
};

try
{
    ApiResponse<CalendarEventsResponse> result = await calendarApi.GetCalendarEventsByCourseAsync(body);
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



