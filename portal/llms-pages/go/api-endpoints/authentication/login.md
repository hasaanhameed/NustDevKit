# Login

Source: /#/go/x-redirect/JTI0ZSUyRkF1dGhlbnRpY2F0aW9uJTJGbG9naW4

Authenticates against NUST LMS on your behalf and returns a gateway JWT. The LMS session (cookie + sesskey) is created and held server-side; use the returned token as `Authorization: Bearer <token>` for every other operation.

:information_source: **Note** This endpoint does not require authentication.

```go
Login(
    ctx context.Context,
    body models.LoginRequest) (
    models.ApiResponse[models.TokenResponse],
    error)
```


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`models.LoginRequest`](/llms-pages/go/models/structures/login-request.md) | Body, Required | NUST LMS credentials. |


# Response Type

**200**: Authentication succeeded; bearer token issued.

This method returns an [`ApiResponse`](/llms-pages/go/sdk-infrastructure/utilities/apiresponse.md) instance. The `Data` property of this instance returns the response data which is of type [models.TokenResponse](/llms-pages/go/models/structures/token-response.md).


# Example Usage

```go
ctx := context.Background()

body := models.LoginRequest{
    Username:              "johndoe.bscs23seecs",
    Password:              "password0",
}

apiResponse, err := authenticationApi.Login(ctx, body)
if err != nil {
    switch typedErr := err.(type) {
        case *errors.AuthLogin401Error:
            log.Fatalln("AuthLogin401ErrorException: ", typedErr)
        default:
            log.Fatalln(err)
    }
} else {
    // Printing the result and response
    fmt.Println(apiResponse.Data)
    fmt.Println(apiResponse.Response.StatusCode)
}
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Invalid LMS credentials. | [`AuthLogin401ErrorException`](/llms-pages/go/models/exceptions/auth-login-401-error.md) |



