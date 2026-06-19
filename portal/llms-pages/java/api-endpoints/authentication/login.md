# Login

Source: /#/java/x-redirect/JTI0ZSUyRkF1dGhlbnRpY2F0aW9uJTJGbG9naW4

Authenticates against NUST LMS on your behalf and returns a gateway JWT. The LMS session (cookie + sesskey) is created and held server-side; use the returned token as `Authorization: Bearer <token>` for every other operation.

:information_source: **Note** This endpoint does not require authentication.

```java
CompletableFuture<ApiResponse<TokenResponse>> loginAsync(
    final LoginRequest body)
```


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LoginRequest`](/llms-pages/java/models/structures/login-request.md) | Body, Required | NUST LMS credentials. |


# Response Type

**200**: Authentication succeeded; bearer token issued.

This method returns an [`ApiResponse`](/llms-pages/java/sdk-infrastructure/utilities/apiresponse.md) instance. The `getResult()` getter of this instance returns the response data which is of type [`TokenResponse`](/llms-pages/java/models/structures/token-response.md).


# Example Usage

```java
LoginRequest body = new LoginRequest.Builder(
    "john.doe@student.nust.edu.pk",
    "password0"
)
.build();

authenticationApi.loginAsync(body).thenAccept(result -> {
    // TODO success callback handler
    System.out.println(result);
}).exceptionally(exception -> {
    Throwable cause = exception.getCause();

    if (cause instanceof AuthLogin401ErrorException) {
        AuthLogin401ErrorException authLogin401ErrorException = (AuthLogin401ErrorException) cause;
        authLogin401ErrorException.printStackTrace();
    } else {
        // fallback for unexpected errors
        exception.printStackTrace();
    }

    return null;
});
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Invalid LMS credentials. | [`AuthLogin401ErrorException`](/llms-pages/java/models/exceptions/auth-login-401-error.md) |



