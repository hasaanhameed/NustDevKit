# Get Calendar Events by Timesort

Source: /#/java/x-redirect/JTI0ZSUyRkNhbGVuZGFyJTJGZ2V0Q2FsZW5kYXJFdmVudHNCeVRpbWVzb3J0

Returns action events (deadlines) across all enrolled courses, ordered by their sort timestamp. On NUST LMS these are submission due dates for assignments, labs, quizzes, and similar dated activities. Use `timesortfrom` to filter to upcoming deadlines only.
Moodle method: `core_calendar_get_action_events_by_timesort`

```java
CompletableFuture<ApiResponse<CalendarEventsResponse>> getCalendarEventsByTimesortAsync(
    final int limitnum,
    final int timesortfrom,
    final Integer timesortto,
    final Integer aftereventid)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/java/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limitnum` | `int` | Query, Required | Maximum number of events to return (e.g. 20 for one page of results). |
| `timesortfrom` | `int` | Query, Required | Unix timestamp (seconds since epoch). Only events with a sort time at or after this value are returned. Pass `0` for no lower bound (all upcoming and past events). To see only upcoming deadlines, pass the current epoch time (e.g. the output of `Date.now() / 1000 \| 0` in JS or `int(time.time())` in Python). |
| `timesortto` | `Integer` | Query, Optional | Only return events with timesort <= this Unix timestamp. |
| `aftereventid` | `Integer` | Query, Optional | Return events whose ID is greater than this value (cursor pagination). |


# Response Type

**200**: Calendar events sorted by timesort.

This method returns an [`ApiResponse`](/llms-pages/java/sdk-infrastructure/utilities/apiresponse.md) instance. The `getResult()` getter of this instance returns the response data which is of type [`CalendarEventsResponse`](/llms-pages/java/models/structures/calendar-events-response.md).


# Example Usage

```java
int limitnum = 20;
int timesortfrom = 0;

calendarApi.getCalendarEventsByTimesortAsync(limitnum, timesortfrom, null, null).thenAccept(result -> {
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



