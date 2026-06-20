# SDK Quickstart

Source: /#/http/x-redirect/JTI0aCUyRl9fZ2V0dGluZ19zdGFydGVk


# Introduction

NUST Learning Management System API for developer integrations (Moodle AJAX wrapper).
Authenticate with your NUST LMS credentials via `POST /auth/login` to receive a bearer token, then call any operation with `Authorization: Bearer <token>`. The NustDevKit gateway logs into the LMS on your behalf and manages the underlying session (cookie + sesskey) server-side, so you never handle the ephemeral sesskey.

## Base URI

The API uses the following base URI:

```bash
http://127.0.0.1:8000
```



# Authorization

This API uses the following authentication schemes.

* [`BearerAuth (OAuth 2 Bearer token)`](/llms-pages/http/getting-started/sdk-quickstart/authorization.md)

## BearerAuth (OAuth 2 Bearer token)



The bearer token is sent in the request like this:

```bash
curl http://127.0.0.1:8000 -H 'Authorization: Bearer {OAUTH_TOKEN}'
```

```http
GET / HTTP/1.1
Host: {HOST}
Authorization: Bearer {OAUTH_TOKEN}
```




