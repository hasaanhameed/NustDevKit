# Login Request

Source: /#/ruby/x-redirect/JTI0bSUyRkxvZ2luUmVxdWVzdA

NUST LMS credentials used to obtain a gateway bearer token.

*This model accepts additional fields of type Object.*


# Class Name

`LoginRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `String` | Required | NUST LMS username or email. |
| `password` | `String` | Required | NUST LMS password. |
| `additional_properties` | `Hash[String, Object]` | Optional | - |


# Example

```ruby
login_request = LoginRequest.new(
  email: 'john.doe@student.nust.edu.pk',
  password: 'password6',
  additional_properties: {
    'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
  }
)
```



