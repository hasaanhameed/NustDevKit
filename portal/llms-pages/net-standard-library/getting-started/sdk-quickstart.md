# SDK Quickstart

Source: /#/net-standard-library/x-redirect/JTI0aCUyRl9fZ2V0dGluZ19zdGFydGVk


# Introduction

NUST Learning Management System API for developer integrations (Moodle AJAX wrapper).
Authenticate with your NUST LMS credentials via `POST /auth/login` to receive a bearer token, then call any operation with `Authorization: Bearer <token>`. The NustDevKit gateway logs into the LMS on your behalf and manages the underlying session (cookie + sesskey) server-side, so you never handle the ephemeral sesskey.


# Building

The generated code uses the Newtonsoft Json.NET NuGet Package. If the automatic NuGet package restore is enabled, these dependencies will be installed automatically. Therefore, you will need internet access for build.

* Open the solution (NustLmsApi.sln) file.

Invoke the build process using Ctrl + Shift + B shortcut key or using the Build menu as shown below.

The build process generates a portable class library, which can be used like a normal class library. More information on how to use can be found at the MSDN Portable Class Libraries documentation.

The supported version is **.NET Standard 2.0**. For checking compatibility of your .NET implementation with the generated library, [click here](https://dotnet.microsoft.com/en-us/platform/dotnet-standard#versions).


# Installation

The following section explains how to use the NustLmsApi.Standard library in a new project.

## 1. Starting a new project

For starting a new project, right click on the current solution from the solution explorer and choose `Add -> New Project`.

![Add a new project in Visual Studio](https://apidocs.io/illustration/cs?workspaceFolder=NUST%20LMS%20API-CSharp&workspaceName=NustLmsApi&projectName=NustLmsApi.Standard&rootNamespace=NustLmsApi.Standard&step=addProject)

Next, choose `Console Application`, provide `TestConsoleProject` as the project name and click OK.

![Create a new Console Application in Visual Studio](https://apidocs.io/illustration/cs?workspaceFolder=NUST%20LMS%20API-CSharp&workspaceName=NustLmsApi&projectName=NustLmsApi.Standard&rootNamespace=NustLmsApi.Standard&step=createProject)

## 2. Set as startup project

The new console project is the entry point for the eventual execution. This requires us to set the `TestConsoleProject` as the start-up project. To do this, right-click on the `TestConsoleProject` and choose `Set as StartUp Project` form the context menu.

![Adding a project reference](https://apidocs.io/illustration/cs?workspaceFolder=NUST%20LMS%20API-CSharp&workspaceName=NustLmsApi&projectName=NustLmsApi.Standard&rootNamespace=NustLmsApi.Standard&step=setStartup)

## 3. Add reference of the library project

In order to use the `NustLmsApi.Standard` library in the new project, first we must add a project reference to the `TestConsoleProject`. First, right click on the `References` node in the solution explorer and click `Add Reference...`

![Adding a project reference](https://apidocs.io/illustration/cs?workspaceFolder=NUST%20LMS%20API-CSharp&workspaceName=NustLmsApi&projectName=NustLmsApi.Standard&rootNamespace=NustLmsApi.Standard&step=addReference)

Next, a window will be displayed where we must set the `checkbox` on `NustLmsApi.Standard` and click `OK`. By doing this, we have added a reference of the `NustLmsApi.Standard` project into the new `TestConsoleProject`.

![Creating a project reference](https://apidocs.io/illustration/cs?workspaceFolder=NUST%20LMS%20API-CSharp&workspaceName=NustLmsApi&projectName=NustLmsApi.Standard&rootNamespace=NustLmsApi.Standard&step=createReference)

## 4. Write sample code

Once the `TestConsoleProject` is created, a file named `Program.cs` will be visible in the solution explorer with an empty `Main` method. This is the entry point for the execution of the entire solution. Here, you can add code to initialize the client library and acquire the instance of a Api class. Sample code to initialize the client library and using Api methods is given in the subsequent sections.

![Adding a project reference](https://apidocs.io/illustration/cs?workspaceFolder=NUST%20LMS%20API-CSharp&workspaceName=NustLmsApi&projectName=NustLmsApi.Standard&rootNamespace=NustLmsApi.Standard&step=addCode)


# Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

## Fields

| Name | Description |
|  --- | --- |
| Production | **Default** NustDevKit Gateway (local development) |
| Environment2 | NustDevKit Gateway (production — replace with your deployed gateway URL) |


# Initialize the API Client

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| Environment | [`Environment`](/llms-pages/net-standard-library/getting-started/sdk-quickstart/environments.md) | The API environment. <br> **Default: `Environment.Production`** |
| Timeout | `TimeSpan` | Http client timeout.<br>*Default*: `TimeSpan.FromSeconds(30)` |
| HttpClientConfiguration | [`Action<HttpClientConfiguration.Builder>`](/llms-pages/net-standard-library/sdk-infrastructure/configuration/httpclientconfigurationbuilder.md) | Action delegate that configures the HTTP client by using the HttpClientConfiguration.Builder for customizing API call settings.<br>*Default*: `new HttpClient()` |
| LogBuilder | [`LogBuilder`](/llms-pages/net-standard-library/sdk-infrastructure/configuration/logbuilder.md) | Represents the logging configuration builder for API calls |
| BearerAuthCredentials | [`BearerAuthCredentials`](/llms-pages/net-standard-library/getting-started/sdk-quickstart/authorization.md) | The Credentials Setter for OAuth 2 Bearer token |

The API client can be initialized as follows:

## Code-Based Initialization

```csharp
using Microsoft.Extensions.Logging;
using NustLmsApi.Standard;
using NustLmsApi.Standard.Authentication;

namespace ConsoleApp;

NustLmsApiClient client = new NustLmsApiClient.Builder()
    .BearerAuthCredentials(
        new BearerAuthModel.Builder(
            "AccessToken"
        )
        .Build())
    .HttpClientConfig(httpClientConfig =>
        httpClientConfig.Timeout(TimeSpan.FromSeconds(100)))
    .Environment(NustLmsApi.Standard.Environment.Production)
    .LoggingConfig(config => config
        .LogLevel(LogLevel.Information)
        .RequestConfig(reqConfig => reqConfig.Body(true))
        .ResponseConfig(respConfig => respConfig.Headers(true))
    )
    .Build();
```

## Configuration-Based Initialization

```csharp
using NustLmsApi.Standard;
using Microsoft.Extensions.Configuration;

namespace ConsoleApp;

// Build the IConfiguration using .NET conventions (JSON, environment, etc.)
var configuration = new ConfigurationBuilder()
    .AddJsonFile("config.json")
    .AddEnvironmentVariables() // [optional] read environment variables
    .Build();

// Instantiate your SDK and configure it from IConfiguration
var client = NustLmsApiClient
    .FromConfiguration(configuration.GetSection("NustLmsApi"));
```

See the [Configuration-Based Initialization](/llms-pages/net-standard-library/sdk-infrastructure/configuration/configuration-based-initialization.md) section for details.


# Authorization

This API uses the following authentication schemes.

* [`BearerAuth (OAuth 2 Bearer token)`](/llms-pages/net-standard-library/getting-started/sdk-quickstart/authorization.md)

## BearerAuth (OAuth 2 Bearer token)



Documentation for accessing and setting credentials for BearerAuth.

### Auth Credentials

| Name | Type | Description | Setter | Getter |
|  --- | --- | --- | --- | --- |
| AccessToken | `string` | The OAuth 2.0 Access Token to use for API requests. | `AccessToken` | `AccessToken` |



**Note:** Auth credentials can be set using `BearerAuthCredentials` in the client builder and accessed through `BearerAuthCredentials` method in the client instance.

### Usage Example

#### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```csharp
using NustLmsApi.Standard;
using NustLmsApi.Standard.Authentication;

namespace ConsoleApp;

NustLmsApiClient client = new NustLmsApiClient.Builder()
    .BearerAuthCredentials(
        new BearerAuthModel.Builder(
            "AccessToken"
        )
        .Build())
    .Build();
```




