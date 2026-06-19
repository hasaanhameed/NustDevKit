# Fetch Notifications

Source: /#/http/x-redirect/JTI0ZSUyRk5vdGlmaWNhdGlvbnMlMkZmZXRjaE5vdGlmaWNhdGlvbnM

Returns pending site-level notifications for the given Moodle context. Returns an empty array when there are no pending notifications.
Moodle method: `core_fetch_notifications`

```http
POST /service/core_fetch_notifications
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/http/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Fetch Notifications Request`](/llms-pages/http/models/structures/fetch-notifications-request.md) | Body, Required | Parameters specifying the context to fetch notifications for. |


# Response Type

**200**: Array of site notifications (empty array when none are pending).

[`array<Site Notification>`](/llms-pages/http/models/structures/site-notification.md)


# Example Usage

```bash
curl -X POST \
  --url 'http://127.0.0.1:8000/service/core_fetch_notifications'  \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer AccessToken' \
  --data-raw '{
  "contextid": 1583361
}'
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleError_ErrorException`](/llms-pages/http/models/exceptions/moodle-error-error.md) |



