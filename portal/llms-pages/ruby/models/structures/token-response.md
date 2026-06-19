# Token Response

Source: /#/ruby/x-redirect/JTI0bSUyRlRva2VuUmVzcG9uc2U

Bearer token issued by the gateway after a successful login.

*This model accepts additional fields of type Object.*


# Class Name

`TokenResponse`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `access_token` | `String` | Required | JWT to send as `Authorization: Bearer <token>` on subsequent requests. |
| `token_type` | `String` | Required | **Default**: `'bearer'` |
| `additional_properties` | `Hash[String, Object]` | Optional | - |


# Example

```ruby
token_response = TokenResponse.new(
  access_token: 'access_token0',
  token_type: 'bearer',
  additional_properties: {
    'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
  }
)
```



