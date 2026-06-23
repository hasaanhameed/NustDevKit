# Get Calendar Events by Course

Source: /#/go/x-redirect/JTI0ZSUyRkNhbGVuZGFyJTJGZ2V0Q2FsZW5kYXJFdmVudHNCeUNvdXJzZQ

Returns all action events (deadlines) for a single course — assignment, lab, and quiz submission due dates, and other dated activities.
Moodle method: `core_calendar_get_action_events_by_course`

```go
GetCalendarEventsByCourse(
    ctx context.Context,
    courseid int,
    timesortfrom *int,
    timesortto *int,
    aftereventid *int,
    limitnum *int) (
    models.ApiResponse[models.CalendarEventsResponse],
    error)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/go/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `courseid` | `int` | Query, Required | ID of the course to fetch events for. |
| `timesortfrom` | `*int` | Query, Optional | Only return events with timesort >= this Unix timestamp. |
| `timesortto` | `*int` | Query, Optional | Only return events with timesort <= this Unix timestamp. |
| `aftereventid` | `*int` | Query, Optional | Cursor-based pagination — return events after this event ID. |
| `limitnum` | `*int` | Query, Optional | Maximum number of events to return. |


# Response Type

**200**: Calendar events for the specified course.

This method returns an [`ApiResponse`](/llms-pages/go/sdk-infrastructure/utilities/apiresponse.md) instance. The `Data` property of this instance returns the response data which is of type [models.CalendarEventsResponse](/llms-pages/go/models/structures/calendar-events-response.md).


# Example Usage

```go
ctx := context.Background()

courseid := 74

apiResponse, err := calendarApi.GetCalendarEventsByCourse(ctx, courseid, nil, nil, nil, nil)
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



