# Login

Source: /#/python/x-redirect/JTI0ZSUyRkF1dGhlbnRpY2F0aW9uJTJGbG9naW4

Authenticates against NUST LMS on your behalf and returns a gateway JWT. The LMS session (cookie + sesskey) is created and held server-side; use the returned token as `Authorization: Bearer <token>` for every other operation.

:information_source: **Note** This endpoint does not require authentication.

```python
def login(self,
         body)
```


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LoginRequest`](/llms-pages/python/models/structures/login-request.md) | Body, Required | NUST LMS credentials. |


# Response Type

**200**: Authentication succeeded; bearer token issued.

This method returns an [`ApiResponse`](/llms-pages/python/sdk-infrastructure/utilities/apiresponse.md) instance. The `body` property of this instance returns the response data which is of type [`TokenResponse`](/llms-pages/python/models/structures/token-response.md).


# Example Usage

```python
body = LoginRequest(
    email='john.doe@student.nust.edu.pk',
    password='password0'
)

result = authentication_api.login(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Invalid LMS credentials. | [`AuthLogin401ErrorException`](/llms-pages/python/models/exceptions/auth-login-401-error.md) |



