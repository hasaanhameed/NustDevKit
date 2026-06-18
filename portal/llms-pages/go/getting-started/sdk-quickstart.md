# SDK Quickstart

Source: /#/go/x-redirect/JTI0aCUyRl9fZ2V0dGluZ19zdGFydGVk


# Introduction

NUST Learning Management System API for developer integrations (Moodle AJAX wrapper). Each path is virtual for clean SDK generation; NustDevKit resolves them to the underlying Moodle AJAX service endpoint transparently.

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
| customQueryAuthenticationCredentials | [`CustomQueryAuthenticationCredentials`](/llms-pages/go/getting-started/sdk-quickstart/authorization.md) | The Credentials Setter for Custom Query Parameter |

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
            nustLmsApi.WithCustomQueryAuthenticationCredentials(
                nustLmsApi.NewCustomQueryAuthenticationCredentials("sesskey"),
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

* [`SessKey (Custom Query Parameter)`](/llms-pages/go/getting-started/sdk-quickstart/authorization.md)

## SessKey (Custom Query Parameter)



Documentation for accessing and setting credentials for SessKey.

### Auth Credentials

| Name | Type | Description | Setter | Getter |
|  --- | --- | --- | --- | --- |
| sesskey | `string` | Session key obtained after authenticating with the LMS portal. | `WithSesskey` | `Sesskey()` |



**Note:** Required auth credentials can be set using `WithCustomQueryAuthenticationCredentials()` by providing a credentials instance with `NewCustomQueryAuthenticationCredentials()` in the configuration initialization and accessed using the `CustomQueryAuthenticationCredentials()` method in the configuration instance.

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
            nustLmsApi.WithCustomQueryAuthenticationCredentials(
                nustLmsApi.NewCustomQueryAuthenticationCredentials("sesskey"),
            ),
        ),
    )
}
```




