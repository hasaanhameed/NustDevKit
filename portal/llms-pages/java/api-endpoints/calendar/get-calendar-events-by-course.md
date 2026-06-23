# Get Calendar Events by Course

Source: /#/java/x-redirect/JTI0ZSUyRkNhbGVuZGFyJTJGZ2V0Q2FsZW5kYXJFdmVudHNCeUNvdXJzZQ

Returns all action events (deadlines) for a single course — assignment, lab, and quiz submission due dates, and other dated activities.
Moodle method: `core_calendar_get_action_events_by_course`

```java
CompletableFuture<ApiResponse<CalendarEventsResponse>> getCalendarEventsByCourseAsync(
    final int courseid,
    final Integer timesortfrom,
    final Integer timesortto,
    final Integer aftereventid,
    final Integer limitnum)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/java/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `courseid` | `int` | Query, Required | ID of the course to fetch events for. |
| `timesortfrom` | `Integer` | Query, Optional | Only return events with timesort >= this Unix timestamp. |
| `timesortto` | `Integer` | Query, Optional | Only return events with timesort <= this Unix timestamp. |
| `aftereventid` | `Integer` | Query, Optional | Cursor-based pagination — return events after this event ID. |
| `limitnum` | `Integer` | Query, Optional | Maximum number of events to return. |


# Response Type

**200**: Calendar events for the specified course.

This method returns an [`ApiResponse`](/llms-pages/java/sdk-infrastructure/utilities/apiresponse.md) instance. The `getResult()` getter of this instance returns the response data which is of type [`CalendarEventsResponse`](/llms-pages/java/models/structures/calendar-events-response.md).


# Example Usage

```java
int courseid = 74;

calendarApi.getCalendarEventsByCourseAsync(courseid, null, null, null, null).thenAccept(result -> {
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



