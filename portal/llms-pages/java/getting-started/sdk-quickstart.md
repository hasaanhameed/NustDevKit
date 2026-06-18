# SDK Quickstart

Source: /#/java/x-redirect/JTI0aCUyRl9fZ2V0dGluZ19zdGFydGVk


# Introduction

NUST Learning Management System API for developer integrations (Moodle AJAX wrapper). Each path is virtual for clean SDK generation; NustDevKit resolves them to the underlying Moodle AJAX service endpoint transparently.


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
| customQueryAuthenticationCredentials | [`CustomQueryAuthenticationCredentials`](/llms-pages/java/getting-started/sdk-quickstart/authorization.md) | The Credentials Setter for Custom Query Parameter |

The API client can be initialized as follows:

```java
import org.slf4j.event.Level;
import pk.edu.nust.lms.NustLmsApiClient;
import pk.edu.nust.lms.authentication.CustomQueryAuthenticationModel;
import pk.edu.nust.lms.exceptions.ApiException;
import pk.edu.nust.lms.http.response.ApiResponse;

public class Program {
    public static void main(String[] args) {
        NustLmsApiClient client = new NustLmsApiClient.Builder()
            .loggingConfig(builder -> builder
                    .level(Level.DEBUG)
                    .requestConfig(logConfigBuilder -> logConfigBuilder.body(true))
                    .responseConfig(logConfigBuilder -> logConfigBuilder.headers(true)))
            .httpClientConfig(configBuilder -> configBuilder
                    .timeout(0))
            .customQueryAuthenticationCredentials(new CustomQueryAuthenticationModel.Builder(
                    "sesskey"
                )
                .build())
            .build();

    }
}
```


# Authorization

This API uses the following authentication schemes.

* [`SessKey (Custom Query Parameter)`](/llms-pages/java/getting-started/sdk-quickstart/authorization.md)

## SessKey (Custom Query Parameter)



Documentation for accessing and setting credentials for SessKey.

### Auth Credentials

| Name | Type | Description | Setter | Getter |
|  --- | --- | --- | --- | --- |
| sesskey | `String` | Session key obtained after authenticating with the LMS portal. | `sesskey` | `getSesskey()` |



**Note:** Auth credentials can be set using `customQueryAuthenticationCredentials` in the client builder and accessed through `getCustomQueryAuthenticationCredentials` method in the client instance.

### Usage Example

#### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```java
import pk.edu.nust.lms.NustLmsApiClient;
import pk.edu.nust.lms.authentication.CustomQueryAuthenticationModel;

public class Program {
    public static void main(String[] args) {
        NustLmsApiClient client = new NustLmsApiClient.Builder()
            .customQueryAuthenticationCredentials(new CustomQueryAuthenticationModel.Builder(
                    "sesskey"
                )
                .build())
            .build();
    }
}
```




