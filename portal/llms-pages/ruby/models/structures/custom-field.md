# Custom Field

Source: /#/ruby/x-redirect/JTI0bSUyRkN1c3RvbUZpZWxk

A custom profile field value attached to a user.

*This model accepts additional fields of type Object.*


# Class Name

`CustomField`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `type` | `String` | Required | Data type of the custom field (e.g., 'text', 'select'). |
| `value` | `String` | Required | Value stored in the custom field. |
| `name` | `String` | Required | Display label of the custom field. |
| `shortname` | `String` | Required | Machine-readable shortname identifier for the custom field. |
| `additional_properties` | `Hash[String, Object]` | Optional | - |


# Example

```ruby
custom_field = CustomField.new(
  type: 'text',
  value: 'SEECS',
  name: 'Institute',
  shortname: 'institution',
  additional_properties: {
    'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
  }
)
```



