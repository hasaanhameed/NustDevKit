# Get Calendar Events by Timesort

Source: /#/http/x-redirect/JTI0ZSUyRkNhbGVuZGFyJTJGZ2V0Q2FsZW5kYXJFdmVudHNCeVRpbWVzb3J0

Returns action events across all enrolled courses, ordered by their sort timestamp. Use `timesortfrom` to filter to upcoming events only.
Moodle method: `core_calendar_get_action_events_by_timesort`

```http
POST /service/core_calendar_get_action_events_by_timesort
```


# Authentication

This endpoint requires [SessKey](/llms-pages/http/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Get Calendar Events by Timesort Request`](/llms-pages/http/models/structures/get-calendar-events-by-timesort-request.md) | Body, Required | Parameters for the time-sorted calendar events request. |


# Response Type

**200**: Calendar events sorted by timesort.

[`Calendar Events Response`](/llms-pages/http/models/structures/calendar-events-response.md)


# Example Usage

```bash
curl -X POST \
  --url 'https://lms.nust.edu.pk/portal/service/core_calendar_get_action_events_by_timesort?sesskey=sesskey'  \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  --data-raw '{
  "limitnum": 20,
  "timesortfrom": 0
}'
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleError_ErrorException`](/llms-pages/http/models/exceptions/moodle-error-error.md) |



