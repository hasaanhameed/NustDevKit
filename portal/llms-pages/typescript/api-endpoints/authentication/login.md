# Login

Source: /#/typescript/x-redirect/JTI0ZSUyRkF1dGhlbnRpY2F0aW9uJTJGbG9naW4

Authenticates against NUST LMS on your behalf and returns a gateway JWT. The LMS session (cookie + sesskey) is created and held server-side; use the returned token as `Authorization: Bearer <token>` for every other operation.

:information_source: **Note** This endpoint does not require authentication.

```ts
async login(
  body: LoginRequest,
  requestOptions?: RequestOptions
): Promise<ApiResponse<TokenResponse>>
```


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LoginRequest`](/llms-pages/typescript/models/structures/login-request.md) | Body, Required | NUST LMS credentials. |
| `requestOptions` | `RequestOptions \| undefined` | Optional | Pass additional request options. |


# Response Type

**200**: Authentication succeeded; bearer token issued.

This method returns an [`ApiResponse`](/llms-pages/typescript/sdk-infrastructure/utilities/apiresponse.md) instance. The `result` property of this instance returns the response data which is of type [`TokenResponse`](/llms-pages/typescript/models/structures/token-response.md).


# Example Usage

```ts
const body: LoginRequest = {
  email: 'john.doe@student.nust.edu.pk',
  password: 'password0',
};

try {
  const response = await authenticationApi.login(body);

  // Extracting fully parsed response body.
  console.log(response.result);

  // Extracting response status code.
  console.log(response.statusCode);
  // Extracting response headers.
  console.log(response.headers);
  // Extracting response body of type `string | Stream`
  console.log(response.body);
} catch (error) {
  if (error instanceof ApiError) {
    // Extracting response error status code.
    console.log(error.statusCode);
    // Extracting response error headers.
    console.log(error.headers);
    // Extracting response error body of type `string | Stream`.
    console.log(error.body);
    if (error instanceof AuthLogin401Error) {
      console.log(error.result);
    }
  }
}
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Invalid LMS credentials. | [`AuthLogin401Error`](/llms-pages/typescript/models/exceptions/auth-login-401-error.md) |



