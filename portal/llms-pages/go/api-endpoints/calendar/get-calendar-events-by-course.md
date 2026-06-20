# Get Calendar Events by Course

Source: /#/go/x-redirect/JTI0ZSUyRkNhbGVuZGFyJTJGZ2V0Q2FsZW5kYXJFdmVudHNCeUNvdXJzZQ

Returns all action events (deadlines) for a single course — assignment, lab, and quiz submission due dates, and other dated activities.
Moodle method: `core_calendar_get_action_events_by_course`

```go
GetCalendarEventsByCourse(
    ctx context.Context,
    body models.GetCalendarEventsByCourseRequest) (
    models.ApiResponse[models.CalendarEventsResponse],
    error)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/go/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`models.GetCalendarEventsByCourseRequest`](/llms-pages/go/models/structures/get-calendar-events-by-course-request.md) | Body, Required | Parameters for the course-specific calendar events request. |


# Response Type

**200**: Calendar events for the specified course.

This method returns an [`ApiResponse`](/llms-pages/go/sdk-infrastructure/utilities/apiresponse.md) instance. The `Data` property of this instance returns the response data which is of type [models.CalendarEventsResponse](/llms-pages/go/models/structures/calendar-events-response.md).


# Example Usage

```go
ctx := context.Background()

body := models.GetCalendarEventsByCourseRequest{
    Courseid:              49906,
}

apiResponse, err := calendarApi.GetCalendarEventsByCourse(ctx, body)
if err != nil {
    switch typedErr := err.(type) {
        case *errors.MoodleError:
            log.Fatalln("MoodleErrorException: ", typedErr)
        default:
            log.Fatalln(err)
    }
} else {
    // Printing the result and response
    fmt.Println(apiResponse.Data)
    fmt.Println(apiResponse.Response.StatusCode)
}
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleErrorException`](/llms-pages/go/models/exceptions/moodle-error.md) |



