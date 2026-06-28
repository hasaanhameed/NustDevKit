# SDK Quickstart

Source: /#/java/x-redirect/JTI0aCUyRl9fZ2V0dGluZ19zdGFydGVk


# Introduction

NUST Learning Management System API for developer integrations (Moodle AJAX wrapper).
Authenticate with your NUST LMS credentials via `POST /auth/login` to receive a bearer token, then call any operation with `Authorization: Bearer <token>`. The NustDevKit gateway logs into the LMS on your behalf and manages the underlying session (cookie + sesskey) server-side, so you never handle the ephemeral sesskey.


# Install the Package

Install the SDK by adding the following dependency in your project's pom.xml file:

```xml
<dependency>
  <groupId>com.apimatic</groupId>
  <artifactId>sample-sdk-artifact-id</artifactId>
  <version>1.0.0</version>
</dependency>
```

You can also view the package at:
https://central.sonatype.com/artifact/com.apimatic/sample-sdk-artifact-id/1.0.0



# Initialize the API Client

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| httpClientConfig | [`Consumer<HttpClientConfiguration.Builder>`](/llms-pages/java/sdk-infrastructure/configuration/httpclientconfiguration-builder.md) | Set up Http Client Configuration instance. |
| loggingConfig | [`Consumer<ApiLoggingConfiguration.Builder>`](/llms-pages/java/sdk-infrastructure/configuration/apiloggingconfiguration-builder.md) | Set up Logging Configuration instance. |
| bearerAuthCredentials | [`BearerAuthCredentials`](/llms-pages/java/getting-started/sdk-quickstart/authorization.md) | The Credentials Setter for OAuth 2 Bearer token |

The API client can be initialized as follows:

```java
import com.nustdevkit.api.NustLmsApiClient;
import com.nustdevkit.api.authentication.BearerAuthModel;
import com.nustdevkit.api.exceptions.ApiException;
import com.nustdevkit.api.http.response.ApiResponse;
import org.slf4j.event.Level;

public class Program {
    public static void main(String[] args) {
        NustLmsApiClient client = new NustLmsApiClient.Builder()
            .loggingConfig(builder -> builder
                    .level(Level.DEBUG)
                    .requestConfig(logConfigBuilder -> logConfigBuilder.body(true))
                    .responseConfig(logConfigBuilder -> logConfigBuilder.headers(true)))
            .httpClientConfig(configBuilder -> configBuilder
                    .timeout(0))
            .bearerAuthCredentials(new BearerAuthModel.Builder(
                    "AccessToken"
                )
                .build())
            .build();

    }
}
```


# Authorization

This API uses the following authentication schemes.

* [`BearerAuth (OAuth 2 Bearer token)`](/llms-pages/java/getting-started/sdk-quickstart/authorization.md)

## BearerAuth (OAuth 2 Bearer token)



Documentation for accessing and setting credentials for BearerAuth.

### Auth Credentials

| Name | Type | Description | Setter | Getter |
|  --- | --- | --- | --- | --- |
| AccessToken | `String` | The OAuth 2.0 Access Token to use for API requests. | `accessToken` | `getAccessToken()` |



**Note:** Auth credentials can be set using `bearerAuthCredentials` in the client builder and accessed through `getBearerAuthCredentials` method in the client instance.

### Usage Example

#### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```java
import com.nustdevkit.api.NustLmsApiClient;
import com.nustdevkit.api.authentication.BearerAuthModel;

public class Program {
    public static void main(String[] args) {
        NustLmsApiClient client = new NustLmsApiClient.Builder()
            .bearerAuthCredentials(new BearerAuthModel.Builder(
                    "AccessToken"
                )
                .build())
            .build();
    }
}
```




