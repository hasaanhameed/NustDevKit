# Login

Source: /#/net-standard-library/x-redirect/JTI0ZSUyRkF1dGhlbnRpY2F0aW9uJTJGbG9naW4

Authenticates against NUST LMS on your behalf and returns a gateway JWT. The LMS session (cookie + sesskey) is created and held server-side; use the returned token as `Authorization: Bearer <token>` for every other operation.

:information_source: **Note** This endpoint does not require authentication.

```csharp
LoginAsync(
    Models.LoginRequest body)
```


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LoginRequest`](/llms-pages/net-standard-library/models/structures/login-request.md) | Body, Required | NUST LMS credentials. |


# Response Type

**200**: Authentication succeeded; bearer token issued.

This method returns an [`ApiResponse`](/llms-pages/net-standard-library/sdk-infrastructure/utilities/apiresponse.md) instance. The `Data` property of this instance returns the response data which is of type [Models.TokenResponse](/llms-pages/net-standard-library/models/structures/token-response.md).


# Example Usage

```csharp
LoginRequest body = new LoginRequest
{
    Email = "john.doe@student.nust.edu.pk",
    Password = "password0",
};

try
{
    ApiResponse<TokenResponse> result = await authenticationApi.LoginAsync(body);
}
catch (ApiException e)
{
    Console.WriteLine(e.Message);
    if (e is AuthLogin401ErrorException)
    {
       // TODO: Handle AuthLogin401ErrorException exception here
    }
}
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Invalid LMS credentials. | [`AuthLogin401ErrorException`](/llms-pages/net-standard-library/models/exceptions/auth-login-401-error.md) |



