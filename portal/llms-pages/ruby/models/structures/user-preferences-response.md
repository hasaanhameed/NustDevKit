# User Preferences Response

Source: /#/ruby/x-redirect/JTI0bSUyRlVzZXJQcmVmZXJlbmNlc1Jlc3BvbnNl

Response envelope for the user-preferences endpoint.

*This model accepts additional fields of type Object.*


# Class Name

`UserPreferencesResponse`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `preferences` | [`Array[UserPreference]`](/llms-pages/ruby/models/structures/user-preference.md) | Required | List of user preference key/value pairs. |
| `warnings` | [`Array[MoodleWarning]`](/llms-pages/ruby/models/structures/moodle-warning.md) | Required | Array of warning objects. Empty when no warnings are present. |
| `additional_properties` | `Hash[String, Object]` | Optional | - |


# Example

```ruby
user_preferences_response = UserPreferencesResponse.new(
  preferences: [
    UserPreference.new(
      name: 'block_myoverview_user_sort_preference',
      value: 'title',
      additional_properties: {
        'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
      }
    )
  ],
  warnings: [
    MoodleWarning.new(
      item: 'item6',
      itemid: 0,
      warningcode: 'warningcode4',
      message: 'message4',
      additional_properties: {
        'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
      }
    )
  ],
  additional_properties: {
    'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
  }
)
```



