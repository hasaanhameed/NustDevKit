# Get Calendar Events by Timesort

Source: /#/ruby/x-redirect/JTI0ZSUyRkNhbGVuZGFyJTJGZ2V0Q2FsZW5kYXJFdmVudHNCeVRpbWVzb3J0

Returns action events (deadlines) across all enrolled courses, ordered by their sort timestamp. On NUST LMS these are submission due dates for assignments, labs, quizzes, and similar dated activities. Use `timesortfrom` to filter to upcoming deadlines only.
Moodle method: `core_calendar_get_action_events_by_timesort`

```ruby
def get_calendar_events_by_timesort(limitnum,
                                    timesortfrom,
                                    timesortto: nil,
                                    aftereventid: nil)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/ruby/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limitnum` | `Integer` | Query, Required | Maximum number of events to return (e.g. 20 for one page of results). |
| `timesortfrom` | `Integer` | Query, Required | Unix timestamp (seconds since epoch). Only events with a sort time at or after this value are returned. Pass `0` for no lower bound (all upcoming and past events). To see only upcoming deadlines, pass the current epoch time (e.g. the output of `Date.now() / 1000 \| 0` in JS or `int(time.time())` in Python). |
| `timesortto` | `Integer` | Query, Optional | Only return events with timesort <= this Unix timestamp. |
| `aftereventid` | `Integer` | Query, Optional | Return events whose ID is greater than this value (cursor pagination). |


# Response Type

**200**: Calendar events sorted by timesort.

This method returns an [`ApiResponse`](/llms-pages/ruby/sdk-infrastructure/utilities/apiresponse.md) instance. The `data` property of this instance returns the response data which is of type [`CalendarEventsResponse`](/llms-pages/ruby/models/structures/calendar-events-response.md).


# Example Usage

```ruby
limitnum = 20

timesortfrom = 0

result = calendar_api.get_calendar_events_by_timesort(
  limitnum,
  timesortfrom
)

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



