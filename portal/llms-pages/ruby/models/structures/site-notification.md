# Site Notification

Source: /#/ruby/x-redirect/JTI0bSUyRlNpdGVOb3RpZmljYXRpb24

A site-level notification (structure varies by type).

*This model accepts additional fields of type Object.*


# Class Name

`SiteNotification`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `Integer` | Optional | Unique identifier for the site notification. |
| `message` | `String` | Optional | Notification message content. |
| `type` | `String` | Optional | Notification type identifier. |
| `additional_properties` | `Hash[String, Object]` | Optional | - |


# Example

```ruby
site_notification = SiteNotification.new(
  id: 238,
  message: 'message6',
  type: 'type6',
  additional_properties: {
    'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
  }
)
```



