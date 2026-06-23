# Get Popup Notifications

Source: /#/ruby/x-redirect/JTI0ZSUyRk5vdGlmaWNhdGlvbnMlMkZnZXRQb3B1cE5vdGlmaWNhdGlvbnM

Returns the most recent popup notifications sent to a user, with support for pagination. Also returns the total count of unread notifications.
Moodle method: `message_popup_get_popup_notifications`

```ruby
def get_popup_notifications(useridto,
                            limit,
                            offset)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/ruby/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `useridto` | `String` | Query, Required | ID of the recipient user, passed as a string. |
| `limit` | `Integer` | Query, Required | Maximum number of notifications to return. |
| `offset` | `Integer` | Query, Required | Pagination offset. |


# Response Type

**200**: Popup notifications and total unread count.

This method returns an [`ApiResponse`](/llms-pages/ruby/sdk-infrastructure/utilities/apiresponse.md) instance. The `data` property of this instance returns the response data which is of type [`PopupNotificationsResponse`](/llms-pages/ruby/models/structures/popup-notifications-response.md).


# Example Usage

```ruby
useridto = 'useridto2'

limit = 172

offset = 0

result = notifications_api.get_popup_notifications(
  useridto,
  limit,
  offset
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



