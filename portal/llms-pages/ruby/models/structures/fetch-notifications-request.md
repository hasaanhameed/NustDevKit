# Fetch Notifications Request

Source: /#/ruby/x-redirect/JTI0bSUyRkZldGNoTm90aWZpY2F0aW9uc1JlcXVlc3Q

Request parameters for fetching site-level notifications.

*This model accepts additional fields of type Object.*


# Class Name

`FetchNotificationsRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `contextid` | `Integer` | Required | Moodle context ID for which to fetch notifications. The user context ID can be found in the user profile image URL path segment. |
| `additional_properties` | `Hash[String, Object]` | Optional | - |


# Example

```ruby
fetch_notifications_request = FetchNotificationsRequest.new(
  contextid: 1583361,
  additional_properties: {
    'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
  }
)
```



