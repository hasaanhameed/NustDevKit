# Get User Preferences Request

Source: /#/ruby/x-redirect/JTI0bSUyRkdldFVzZXJQcmVmZXJlbmNlc1JlcXVlc3Q

Request parameters for retrieving user preferences.

*This model accepts additional fields of type Object.*


# Class Name

`GetUserPreferencesRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `userid` | `Integer` | Required | ID of the user whose preferences to retrieve. |
| `name` | `String` | Optional | Specific preference name to retrieve. Omit to retrieve all preferences. |
| `additional_properties` | `Hash[String, Object]` | Optional | - |


# Example

```ruby
get_user_preferences_request = GetUserPreferencesRequest.new(
  userid: 123456,
  name: 'name2',
  additional_properties: {
    'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
  }
)
```



