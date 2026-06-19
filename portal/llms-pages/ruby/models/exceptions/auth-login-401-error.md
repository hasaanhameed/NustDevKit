# Auth Login 401 Error

Source: /#/ruby/x-redirect/JTI0bSUyRkF1dGglMjUyMExvZ2luJTI1MjA0MDElMjUyMEVycm9y

*This model accepts additional fields of type Object.*


# Class Name

`AuthLogin401ErrorException`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `detail` | `String` | Optional | - |
| `additional_properties` | `Hash[String, Object]` | Optional | - |


# Example

```ruby
begin
  # make the API call
rescue AuthLogin401ErrorException => e
  puts "Caught AuthLogin401ErrorException: #{e.message}"
end
```



