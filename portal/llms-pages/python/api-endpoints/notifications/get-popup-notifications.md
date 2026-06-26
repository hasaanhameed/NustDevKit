# Get Popup Notifications

Source: /#/python/x-redirect/JTI0ZSUyRk5vdGlmaWNhdGlvbnMlMkZnZXRQb3B1cE5vdGlmaWNhdGlvbnM

Returns the most recent popup notifications sent to a user, with support for pagination. Also returns the total count of unread notifications.
Moodle method: `message_popup_get_popup_notifications`

```python
def get_popup_notifications(self,
                           useridto,
                           limit,
                           offset)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/python/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `useridto` | `str` | Query, Required | ID of the recipient user (yourself), passed as a string. Get your numeric user ID from `GET /service/core_webservice_get_site_info`. |
| `limit` | `int` | Query, Required | Maximum number of notifications to return. |
| `offset` | `int` | Query, Required | Pagination offset. |


# Response Type

**200**: Popup notifications and total unread count.

This method returns an [`ApiResponse`](/llms-pages/python/sdk-infrastructure/utilities/apiresponse.md) instance. The `body` property of this instance returns the response data which is of type [`PopupNotificationsResponse`](/llms-pages/python/models/structures/popup-notifications-response.md).


# Example Usage

```python
useridto = 'useridto2'

limit = 172

offset = 0

result = notifications_api.get_popup_notifications(
    useridto,
    limit,
    offset
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleErrorException`](/llms-pages/python/models/exceptions/moodle-error.md) |



