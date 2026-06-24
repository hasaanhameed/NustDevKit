# Get Calendar Events by Timesort

Source: /#/go/x-redirect/JTI0ZSUyRkNhbGVuZGFyJTJGZ2V0Q2FsZW5kYXJFdmVudHNCeVRpbWVzb3J0

Returns action events (deadlines) across all enrolled courses, ordered by their sort timestamp. On NUST LMS these are submission due dates for assignments, labs, quizzes, and similar dated activities. Use `timesortfrom` to filter to upcoming deadlines only.
Moodle method: `core_calendar_get_action_events_by_timesort`

```go
GetCalendarEventsByTimesort(
    ctx context.Context,
    limitnum int,
    timesortfrom int,
    timesortto *int,
    aftereventid *int) (
    models.ApiResponse[models.CalendarEventsResponse],
    error)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/go/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limitnum` | `int` | Query, Required | Maximum number of events to return (e.g. 20 for one page of results). |
| `timesortfrom` | `int` | Query, Required | Unix timestamp (seconds since epoch). Only events with a sort time at or after this value are returned. Pass `0` for no lower bound (all upcoming and past events). To see only upcoming deadlines, pass the current epoch time (e.g. the output of `Date.now() / 1000 \| 0` in JS or `int(time.time())` in Python). |
| `timesortto` | `*int` | Query, Optional | Only return events with timesort <= this Unix timestamp. |
| `aftereventid` | `*int` | Query, Optional | Return events whose ID is greater than this value (cursor pagination). |


# Response Type

**200**: Calendar events sorted by timesort.

This method returns an [`ApiResponse`](/llms-pages/go/sdk-infrastructure/utilities/apiresponse.md) instance. The `Data` property of this instance returns the response data which is of type [models.CalendarEventsResponse](/llms-pages/go/models/structures/calendar-events-response.md).


# Example Usage

```go
ctx := context.Background()

limitnum := 20

timesortfrom := 0

apiResponse, err := calendarApi.GetCalendarEventsByTimesort(ctx, limitnum, timesortfrom, nil, nil)
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



