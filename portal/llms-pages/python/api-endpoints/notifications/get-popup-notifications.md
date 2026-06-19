# Get Popup Notifications

Source: /#/python/x-redirect/JTI0ZSUyRk5vdGlmaWNhdGlvbnMlMkZnZXRQb3B1cE5vdGlmaWNhdGlvbnM

Returns the most recent popup notifications sent to a user, with support for pagination. Also returns the total count of unread notifications.
Moodle method: `message_popup_get_popup_notifications`

```python
def get_popup_notifications(self,
                           body)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/python/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetPopupNotificationsRequest`](/llms-pages/python/models/structures/get-popup-notifications-request.md) | Body, Required | Parameters for the popup notifications request. |


# Response Type

**200**: Popup notifications and total unread count.

This method returns an [`ApiResponse`](/llms-pages/python/sdk-infrastructure/utilities/apiresponse.md) instance. The `body` property of this instance returns the response data which is of type [`PopupNotificationsResponse`](/llms-pages/python/models/structures/popup-notifications-response.md).


# Example Usage

```python
body = GetPopupNotificationsRequest(
    useridto='162154',
    limit=20,
    offset=0
)

result = notifications_api.get_popup_notifications(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleErrorException`](/llms-pages/python/models/exceptions/moodle-error.md) |



