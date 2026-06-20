# Login

Source: /#/http/x-redirect/JTI0ZSUyRkF1dGhlbnRpY2F0aW9uJTJGbG9naW4

Authenticates against NUST LMS on your behalf and returns a gateway JWT. The LMS session (cookie + sesskey) is created and held server-side; use the returned token as `Authorization: Bearer <token>` for every other operation.

:information_source: **Note** This endpoint does not require authentication.

```http
POST /auth/login
```


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Login Request`](/llms-pages/http/models/structures/login-request.md) | Body, Required | NUST LMS credentials. |


# Response Type

**200**: Authentication succeeded; bearer token issued.

[`Token Response`](/llms-pages/http/models/structures/token-response.md)


# Example Usage

```bash
curl -X POST \
  --url 'http://127.0.0.1:8000/auth/login'  \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  --data-raw '{
  "username": "johndoe.bscs23seecs",
  "password": "password0"
}'
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Invalid LMS credentials. | [`Auth Login 401 ErrorException`](/llms-pages/http/models/exceptions/auth-login-401-error.md) |



