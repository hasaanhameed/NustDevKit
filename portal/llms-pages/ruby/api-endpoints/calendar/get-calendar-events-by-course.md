# Get Calendar Events by Course

Source: /#/ruby/x-redirect/JTI0ZSUyRkNhbGVuZGFyJTJGZ2V0Q2FsZW5kYXJFdmVudHNCeUNvdXJzZQ

Returns all action events (assignments, quizzes, etc.) for a single course.
Moodle method: `core_calendar_get_action_events_by_course`

```ruby
def get_calendar_events_by_course(body)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/ruby/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetCalendarEventsByCourseRequest`](/llms-pages/ruby/models/structures/get-calendar-events-by-course-request.md) | Body, Required | Parameters for the course-specific calendar events request. |


# Response Type

**200**: Calendar events for the specified course.

This method returns an [`ApiResponse`](/llms-pages/ruby/sdk-infrastructure/utilities/apiresponse.md) instance. The `data` property of this instance returns the response data which is of type [`CalendarEventsResponse`](/llms-pages/ruby/models/structures/calendar-events-response.md).


# Example Usage

```ruby
body = GetCalendarEventsByCourseRequest.new(
  courseid: 49906
)

result = calendar_api.get_calendar_events_by_course(body)

if result.success?
  puts result.data
elsif result.error?
  warn result.errors
end
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleErrorException`](/llms-pages/ruby/models/exceptions/moodle-error.md) |



