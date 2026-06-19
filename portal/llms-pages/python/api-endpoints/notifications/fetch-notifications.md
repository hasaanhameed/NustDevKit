# Fetch Notifications

Source: /#/python/x-redirect/JTI0ZSUyRk5vdGlmaWNhdGlvbnMlMkZmZXRjaE5vdGlmaWNhdGlvbnM

Returns pending site-level notifications for the given Moodle context. Returns an empty array when there are no pending notifications.
Moodle method: `core_fetch_notifications`

```python
def fetch_notifications(self,
                       body)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/python/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`FetchNotificationsRequest`](/llms-pages/python/models/structures/fetch-notifications-request.md) | Body, Required | Parameters specifying the context to fetch notifications for. |


# Response Type

**200**: Array of site notifications (empty array when none are pending).

This method returns an [`ApiResponse`](/llms-pages/python/sdk-infrastructure/utilities/apiresponse.md) instance. The `body` property of this instance returns the response data which is of type [`List[SiteNotification]`](/llms-pages/python/models/structures/site-notification.md).


# Example Usage

```python
body = FetchNotificationsRequest(
    contextid=1583361
)

result = notifications_api.fetch_notifications(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleErrorException`](/llms-pages/python/models/exceptions/moodle-error.md) |



