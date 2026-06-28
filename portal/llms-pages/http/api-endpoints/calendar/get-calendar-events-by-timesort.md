# Get Calendar Events by Timesort

Source: /#/http/x-redirect/JTI0ZSUyRkNhbGVuZGFyJTJGZ2V0Q2FsZW5kYXJFdmVudHNCeVRpbWVzb3J0

Returns action events (deadlines) across all enrolled courses, ordered by their sort timestamp. On NUST LMS these are submission due dates for assignments, labs, quizzes, and similar dated activities. Use `timesortfrom` to filter to upcoming deadlines only.
Moodle method: `core_calendar_get_action_events_by_timesort`

```http
GET /service/core_calendar_get_action_events_by_timesort
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/http/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limitnum` | `Number` | Query, Required | Maximum number of events to return (e.g. 20 for one page of results). |
| `timesortfrom` | `Number` | Query, Required | Unix timestamp (seconds since epoch). Only events with a sort time at or after this value are returned. Pass `0` for no lower bound (all upcoming and past events). To see only upcoming deadlines, pass the current epoch time (e.g. the output of `Date.now() / 1000 \| 0` in JS or `int(time.time())` in Python). |
| `timesortto` | `Number` | Query, Optional | Only return events with timesort <= this Unix timestamp. |
| `aftereventid` | `Number` | Query, Optional | Return events whose ID is greater than this value (cursor pagination). |


# Response Type

**200**: Calendar events sorted by timesort.

[`Calendar Events Response`](/llms-pages/http/models/structures/calendar-events-response.md)


# Example Usage

```bash
curl -X GET -G \
  --url 'https://api.nustdevkit.com/service/core_calendar_get_action_events_by_timesort'  \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer AccessToken' \
  -d 'limitnum=20' \
  -d 'timesortfrom=0'
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleError_ErrorException`](/llms-pages/http/models/exceptions/moodle-error-error.md) |



