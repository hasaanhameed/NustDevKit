# Get Users by Field Request

Source: /#/ruby/x-redirect/JTI0bSUyRkdldFVzZXJzQnlGaWVsZFJlcXVlc3Q

Request parameters for retrieving user profiles by a profile field value.

*This model accepts additional fields of type Object.*


# Class Name

`GetUsersByFieldRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field` | [`UserProfileField`](/llms-pages/ruby/models/enumerations/user-profile-field.md) | Required | User profile field to match against when searching for users. |
| `values` | `Array[String]` | Required | List of field values to look up. All values must be provided as strings even when the field is numeric (e.g., "162154" for an integer ID). |
| `additional_properties` | `Hash[String, Object]` | Optional | - |


# Example

```ruby
get_users_by_field_request = GetUsersByFieldRequest.new(
  field: UserProfileField::ID,
  values: [
    '162154'
  ],
  additional_properties: {
    'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
  }
)
```



