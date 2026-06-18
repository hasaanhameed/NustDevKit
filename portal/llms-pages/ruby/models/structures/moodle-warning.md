# Moodle Warning

Source: /#/ruby/x-redirect/JTI0bSUyRk1vb2RsZVdhcm5pbmc

A non-fatal warning returned alongside a successful response.

*This model accepts additional fields of type Object.*


# Class Name

`MoodleWarning`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item` | `String` | Optional | Item identifier related to the warning; empty string if not applicable. |
| `itemid` | `Integer` | Optional | Numeric item ID related to the warning; 0 if not applicable. |
| `warningcode` | `String` | Optional | Machine-readable warning code; empty string if no code. |
| `message` | `String` | Optional | Human-readable warning description. |
| `additional_properties` | `Hash[String, Object]` | Optional | - |


# Example

```ruby
moodle_warning = MoodleWarning.new(
  item: 'item0',
  itemid: 0,
  warningcode: 'warningcode2',
  message: 'message8',
  additional_properties: {
    'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
  }
)
```



