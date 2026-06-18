# Event Icon

Source: /#/ruby/x-redirect/JTI0bSUyRkV2ZW50SWNvbg

Icon metadata for a calendar event.

*This model accepts additional fields of type Object.*


# Class Name

`EventIcon`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `String` | Required | Icon key name used to locate the icon asset. |
| `component` | `String` | Required | Moodle component that owns the icon (e.g., 'assign'). |
| `alttext` | `String` | Required | Accessible alt text for the icon image. |
| `additional_properties` | `Hash[String, Object]` | Optional | - |


# Example

```ruby
event_icon = EventIcon.new(
  key: 'icon',
  component: 'assign',
  alttext: 'Activity event',
  additional_properties: {
    'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
  }
)
```



