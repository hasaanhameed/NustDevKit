# User Preference

Source: /#/ruby/x-redirect/JTI0bSUyRlVzZXJQcmVmZXJlbmNl

A single user preference setting.

*This model accepts additional fields of type Object.*


# Class Name

`UserPreference`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `String` | Required | Unique key identifying the preference. |
| `value` | `String` | Required | Preference value as a string. Note that the internal _lastloaded preference is returned as an integer by the LMS. |
| `additional_properties` | `Hash[String, Object]` | Optional | - |


# Example

```ruby
user_preference = UserPreference.new(
  name: 'block_myoverview_user_sort_preference',
  value: 'title',
  additional_properties: {
    'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
  }
)
```



