# SDK Quickstart

Source: /#/http/x-redirect/JTI0aCUyRl9fZ2V0dGluZ19zdGFydGVk


# Introduction

NUST Learning Management System API for developer integrations (Moodle AJAX wrapper).
Authenticate with your NUST LMS credentials via `POST /auth/login` to receive a bearer token, then call any operation with `Authorization: Bearer <token>`. The NustDevKit gateway logs into the LMS on your behalf and manages the underlying session (cookie + sesskey) server-side, so you never handle the ephemeral sesskey.


# Environments

This API has support for the following environment(s). Each environment has one or more base URIs defined.

## Production

NustDevKit Gateway (local development)

| Server | Base URI |
|  --- | --- |
| default | `http://127.0.0.1:8000` |

## Environment2

NustDevKit Gateway (production — replace with your deployed gateway URL)

| Server | Base URI |
|  --- | --- |
| default | `https://gateway.nustdevkit.example` |

The default environment is **production** and the default server is **default**.


# Authorization

This API uses the following authentication schemes.

* [`BearerAuth (OAuth 2 Bearer token)`](/llms-pages/http/getting-started/sdk-quickstart/authorization.md)

## BearerAuth (OAuth 2 Bearer token)



The bearer token is sent in the request like this:

```bash
curl {BASEURI} -H 'Authorization: Bearer {OAUTH_TOKEN}'
```

```http
GET / HTTP/1.1
Host: {HOST}
Authorization: Bearer {OAUTH_TOKEN}
```




