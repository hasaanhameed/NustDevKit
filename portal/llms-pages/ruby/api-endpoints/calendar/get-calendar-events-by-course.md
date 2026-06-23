# Get Calendar Events by Course

Source: /#/ruby/x-redirect/JTI0ZSUyRkNhbGVuZGFyJTJGZ2V0Q2FsZW5kYXJFdmVudHNCeUNvdXJzZQ

Returns all action events (deadlines) for a single course — assignment, lab, and quiz submission due dates, and other dated activities.
Moodle method: `core_calendar_get_action_events_by_course`

```ruby
def get_calendar_events_by_course(courseid,
                                  timesortfrom: nil,
                                  timesortto: nil,
                                  aftereventid: nil,
                                  limitnum: nil)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/ruby/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `courseid` | `Integer` | Query, Required | ID of the course to fetch events for. |
| `timesortfrom` | `Integer` | Query, Optional | Only return events with timesort >= this Unix timestamp. |
| `timesortto` | `Integer` | Query, Optional | Only return events with timesort <= this Unix timestamp. |
| `aftereventid` | `Integer` | Query, Optional | Cursor-based pagination — return events after this event ID. |
| `limitnum` | `Integer` | Query, Optional | Maximum number of events to return. |


# Response Type

**200**: Calendar events for the specified course.

This method returns an [`ApiResponse`](/llms-pages/ruby/sdk-infrastructure/utilities/apiresponse.md) instance. The `data` property of this instance returns the response data which is of type [`CalendarEventsResponse`](/llms-pages/ruby/models/structures/calendar-events-response.md).


# Example Usage

```ruby
courseid = 74

result = calendar_api.get_calendar_events_by_course(courseid)

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



