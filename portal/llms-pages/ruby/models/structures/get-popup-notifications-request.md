# Get Popup Notifications Request

Source: /#/ruby/x-redirect/JTI0bSUyRkdldFBvcHVwTm90aWZpY2F0aW9uc1JlcXVlc3Q

Request parameters for retrieving popup notifications for a user.

*This model accepts additional fields of type Object.*


# Class Name

`GetPopupNotificationsRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `useridto` | `String` | Required | ID of the recipient user, passed as a string. |
| `limit` | `Integer` | Required | Maximum number of notifications to return. |
| `offset` | `Integer` | Required | Pagination offset.<br><br>**Default**: `0` |
| `additional_properties` | `Hash[String, Object]` | Optional | - |


# Example

```ruby
get_popup_notifications_request = GetPopupNotificationsRequest.new(
  useridto: '162154',
  limit: 20,
  offset: 0,
  additional_properties: {
    'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
  }
)
```



