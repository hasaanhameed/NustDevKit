# SDK Quickstart

Source: /#/go/x-redirect/JTI0aCUyRl9fZ2V0dGluZ19zdGFydGVk


# Introduction

NUST Learning Management System API for developer integrations (Moodle AJAX wrapper).
Authenticate with your NUST LMS credentials via `POST /auth/login` to receive a bearer token, then call any operation with `Authorization: Bearer <token>`. The NustDevKit gateway logs into the LMS on your behalf and manages the underlying session (cookie + sesskey) server-side, so you never handle the ephemeral sesskey.

## Requirements

The SDK requires **Go version 1.18 or above**.


# Building

## Install Dependencies

Resolve all the SDK dependencies, using the `go get` command.


# Installation

The following section explains how to use the nustLmsApi library in a new project.

## 1. Add SDK as a Dependency to the Application

- Add the following lines to your application's `go.mod` file:

```go
replace nustLmsApi => ".\\Random Directory" // local path to the SDK

require nustLmsApi v0.0.0
```

- Resolve the dependencies in the updated `go.mod` file, using the `go get` command.



# Initialize the API Client

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| httpConfiguration | [`HttpConfiguration`](/llms-pages/go/sdk-infrastructure/configuration/httpconfiguration.md) | Configurable http client options like timeout and retries. |
| loggerConfiguration | [`LoggerConfiguration`](/llms-pages/go/sdk-infrastructure/configuration/loggerconfiguration.md) | Represents the logger configurations for API calls |
| bearerAuthCredentials | [`BearerAuthCredentials`](/llms-pages/go/getting-started/sdk-quickstart/authorization.md) | The Credentials Setter for OAuth 2 Bearer token |

The API client can be initialized as follows:

```go
package main

import (
    "nustLmsApi"
)

func main() {
    client := nustLmsApi.NewClient(
    nustLmsApi.CreateConfiguration(
            nustLmsApi.WithHttpConfiguration(
                nustLmsApi.CreateHttpConfiguration(
                    nustLmsApi.WithTimeout(30),
                ),
            ),
            nustLmsApi.WithBearerAuthCredentials(
                nustLmsApi.NewBearerAuthCredentials("AccessToken"),
            ),
            nustLmsApi.WithLoggerConfiguration(
                nustLmsApi.WithLevel("info"),
                nustLmsApi.WithRequestConfiguration(
                    nustLmsApi.WithRequestBody(true),
                ),
                nustLmsApi.WithResponseConfiguration(
                    nustLmsApi.WithResponseHeaders(true),
                ),
            ),
        ),
    )
}
```


# Authorization

This API uses the following authentication schemes.

* [`BearerAuth (OAuth 2 Bearer token)`](/llms-pages/go/getting-started/sdk-quickstart/authorization.md)

## BearerAuth (OAuth 2 Bearer token)



Documentation for accessing and setting credentials for BearerAuth.

### Auth Credentials

| Name | Type | Description | Setter | Getter |
|  --- | --- | --- | --- | --- |
| accessToken | `string` | The OAuth 2.0 Access Token to use for API requests. | `WithAccessToken` | `AccessToken()` |



**Note:** Required auth credentials can be set using `WithBearerAuthCredentials()` by providing a credentials instance with `NewBearerAuthCredentials()` in the configuration initialization and accessed using the `BearerAuthCredentials()` method in the configuration instance.

### Usage Example

#### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```go
package main

import (
    "nustLmsApi"
)

func main() {
    client := nustLmsApi.NewClient(
    nustLmsApi.CreateConfiguration(
            nustLmsApi.WithBearerAuthCredentials(
                nustLmsApi.NewBearerAuthCredentials("AccessToken"),
            ),
        ),
    )
}
```




