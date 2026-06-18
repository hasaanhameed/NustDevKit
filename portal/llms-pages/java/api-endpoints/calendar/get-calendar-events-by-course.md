# Get Calendar Events by Course

Source: /#/java/x-redirect/JTI0ZSUyRkNhbGVuZGFyJTJGZ2V0Q2FsZW5kYXJFdmVudHNCeUNvdXJzZQ

Returns all action events (assignments, quizzes, etc.) for a single course.
Moodle method: `core_calendar_get_action_events_by_course`

```java
CompletableFuture<ApiResponse<CalendarEventsResponse>> getCalendarEventsByCourseAsync(
    final GetCalendarEventsByCourseRequest body)
```


# Authentication

This endpoint requires [SessKey](/llms-pages/java/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetCalendarEventsByCourseRequest`](/llms-pages/java/models/structures/get-calendar-events-by-course-request.md) | Body, Required | Parameters for the course-specific calendar events request. |


# Response Type

**200**: Calendar events for the specified course.

This method returns an [`ApiResponse`](/llms-pages/java/sdk-infrastructure/utilities/apiresponse.md) instance. The `getResult()` getter of this instance returns the response data which is of type [`CalendarEventsResponse`](/llms-pages/java/models/structures/calendar-events-response.md).


# Example Usage

```java
GetCalendarEventsByCourseRequest body = new GetCalendarEventsByCourseRequest.Builder(
    49906
)
.build();

calendarApi.getCalendarEventsByCourseAsync(body).thenAccept(result -> {
    // TODO success callback handler
    System.out.println(result);
}).exceptionally(exception -> {
    Throwable cause = exception.getCause();

    if (cause instanceof MoodleErrorException) {
        MoodleErrorException moodleErrorException = (MoodleErrorException) cause;
        moodleErrorException.printStackTrace();
    } else {
        // fallback for unexpected errors
        exception.printStackTrace();
    }

    return null;
});
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleErrorException`](/llms-pages/java/models/exceptions/moodle-error.md) |



