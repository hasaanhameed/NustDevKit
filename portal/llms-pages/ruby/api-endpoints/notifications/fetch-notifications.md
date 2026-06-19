# Fetch Notifications

Source: /#/ruby/x-redirect/JTI0ZSUyRk5vdGlmaWNhdGlvbnMlMkZmZXRjaE5vdGlmaWNhdGlvbnM

Returns pending site-level notifications for the given Moodle context. Returns an empty array when there are no pending notifications.
Moodle method: `core_fetch_notifications`

```ruby
def fetch_notifications(body)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/ruby/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`FetchNotificationsRequest`](/llms-pages/ruby/models/structures/fetch-notifications-request.md) | Body, Required | Parameters specifying the context to fetch notifications for. |


# Response Type

**200**: Array of site notifications (empty array when none are pending).

This method returns an [`ApiResponse`](/llms-pages/ruby/sdk-infrastructure/utilities/apiresponse.md) instance. The `data` property of this instance returns the response data which is of type [`Array[SiteNotification]`](/llms-pages/ruby/models/structures/site-notification.md).


# Example Usage

```ruby
body = FetchNotificationsRequest.new(
  contextid: 1583361
)

result = notifications_api.fetch_notifications(body)

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



