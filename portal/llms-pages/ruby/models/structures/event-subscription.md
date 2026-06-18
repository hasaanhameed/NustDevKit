# Event Subscription

Source: /#/ruby/x-redirect/JTI0bSUyRkV2ZW50U3Vic2NyaXB0aW9u

Subscription display settings for a calendar event.

*This model accepts additional fields of type Object.*


# Class Name

`EventSubscription`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `displayeventsource` | `TrueClass \| FalseClass` | Required | Whether to display the event source label on the calendar. |
| `additional_properties` | `Hash[String, Object]` | Optional | - |


# Example

```ruby
event_subscription = EventSubscription.new(
  displayeventsource: false,
  additional_properties: {
    'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
  }
)
```



