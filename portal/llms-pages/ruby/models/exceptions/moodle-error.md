# Moodle Error

Source: /#/ruby/x-redirect/JTI0bSUyRk1vb2RsZUVycm9y

Error returned by the LMS on a failed operation.

*This model accepts additional fields of type Object.*


# Class Name

`MoodleErrorException`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errorcode` | `String` | Optional | Machine-readable error code identifier. |
| `message` | `String` | Optional | Human-readable error description. |
| `link` | `String` | Optional | Redirect URL for the user; empty string if not applicable. |
| `moreinfourl` | `String` | Optional | URL to additional error documentation; empty string if not available. |
| `debuginfo` | `String` | Optional | Additional debug information; empty string when not in debug mode. |
| `additional_properties` | `Hash[String, Object]` | Optional | - |


# Example

```ruby
begin
  # make the API call
rescue MoodleErrorException => e
  puts "Caught MoodleErrorException: #{e.message}"
end
```



