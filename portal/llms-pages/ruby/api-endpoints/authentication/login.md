# Login

Source: /#/ruby/x-redirect/JTI0ZSUyRkF1dGhlbnRpY2F0aW9uJTJGbG9naW4

Authenticates against NUST LMS on your behalf and returns a gateway JWT. The LMS session (cookie + sesskey) is created and held server-side; use the returned token as `Authorization: Bearer <token>` for every other operation.

:information_source: **Note** This endpoint does not require authentication.

```ruby
def login(body)
```


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LoginRequest`](/llms-pages/ruby/models/structures/login-request.md) | Body, Required | NUST LMS credentials. |


# Response Type

**200**: Authentication succeeded; bearer token issued.

This method returns an [`ApiResponse`](/llms-pages/ruby/sdk-infrastructure/utilities/apiresponse.md) instance. The `data` property of this instance returns the response data which is of type [`TokenResponse`](/llms-pages/ruby/models/structures/token-response.md).


# Example Usage

```ruby
body = LoginRequest.new(
  email: 'john.doe@student.nust.edu.pk',
  password: 'password0'
)

result = authentication_api.login(body)

if result.success?
  puts result.data
elsif result.error?
  warn result.errors
end
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Invalid LMS credentials. | [`AuthLogin401ErrorException`](/llms-pages/ruby/models/exceptions/auth-login-401-error.md) |



