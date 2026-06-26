# Get Popup Notifications

Source: /#/http/x-redirect/JTI0ZSUyRk5vdGlmaWNhdGlvbnMlMkZnZXRQb3B1cE5vdGlmaWNhdGlvbnM

Returns the most recent popup notifications sent to a user, with support for pagination. Also returns the total count of unread notifications.
Moodle method: `message_popup_get_popup_notifications`

```http
GET /service/message_popup_get_popup_notifications
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/http/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `useridto` | `String` | Query, Required | ID of the recipient user (yourself), passed as a string. Get your numeric user ID from `GET /service/core_webservice_get_site_info`. |
| `limit` | `Number` | Query, Required | Maximum number of notifications to return. |
| `offset` | `Number` | Query, Required | Pagination offset. |


# Response Type

**200**: Popup notifications and total unread count.

[`Popup Notifications Response`](/llms-pages/http/models/structures/popup-notifications-response.md)


# Example Usage

```bash
curl -X GET -G \
  --url 'http://127.0.0.1:8000/service/message_popup_get_popup_notifications'  \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer AccessToken' \
  -d 'useridto=useridto2' \
  -d 'limit=172' \
  -d 'offset=0'
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleError_ErrorException`](/llms-pages/http/models/exceptions/moodle-error-error.md) |



