# Get Calendar Events by Course

Source: /#/http/x-redirect/JTI0ZSUyRkNhbGVuZGFyJTJGZ2V0Q2FsZW5kYXJFdmVudHNCeUNvdXJzZQ

Returns all action events (deadlines) for a single course — assignment, lab, and quiz submission due dates, and other dated activities.
Moodle method: `core_calendar_get_action_events_by_course`

```http
GET /service/core_calendar_get_action_events_by_course
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/http/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `courseid` | `Number` | Query, Required | ID of the course to fetch events for. |
| `timesortfrom` | `Number` | Query, Optional | Only return events with timesort >= this Unix timestamp. |
| `timesortto` | `Number` | Query, Optional | Only return events with timesort <= this Unix timestamp. |
| `aftereventid` | `Number` | Query, Optional | Cursor-based pagination — return events after this event ID. |
| `limitnum` | `Number` | Query, Optional | Maximum number of events to return. |


# Response Type

**200**: Calendar events for the specified course.

[`Calendar Events Response`](/llms-pages/http/models/structures/calendar-events-response.md)


# Example Usage

```bash
curl -X GET -G \
  --url 'https://api.nustdevkit.com/service/core_calendar_get_action_events_by_course'  \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer AccessToken' \
  -d 'courseid=74'
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleError_ErrorException`](/llms-pages/http/models/exceptions/moodle-error-error.md) |



