# SDK Quickstart

Source: /#/ruby/x-redirect/JTI0aCUyRl9fZ2V0dGluZ19zdGFydGVk


# Introduction

NUST Learning Management System API for developer integrations (Moodle AJAX wrapper).
Authenticate with your NUST LMS credentials via `POST /auth/login` to receive a bearer token, then call any operation with `Authorization: Bearer <token>`. The NustDevKit gateway logs into the LMS on your behalf and manages the underlying session (cookie + sesskey) server-side, so you never handle the ephemeral sesskey.


# Building

The generated code depends on a few Ruby gems. The references to these gems are added in the gemspec file. The easiest way to resolve the dependencies, build the gem and install it is through Rake:

1. Install Rake if not already installed: `gem install rake`
2. Install Bundler if not already installed: `gem install bundler`
3. From terminal/cmd navigate to the root directory of the SDK.
4. Invoke: `rake install`

Alternatively, you can build and install the gem manually:

1. From terminal/cmd navigate to the root directory of the SDK.
2. Run the build command: `gem build nust_lms_api.gemspec`
3. Run the install command: `gem install nust_lms_api-1.0.0.gem`

![Installing Gem](https://apidocs.io/illustration/ruby?workspaceFolder=NustLmsApi&gemVer=1.0.0&gemName=nust_lms_api&step=buildSDK)


# Installation

The following section explains how to use the nust_lms_api ruby gem in a new Rails project using RubyMine&trade;. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

## 1. Starting a new project

Close any existing projects in RubyMine&trade; by selecting `File -> Close Project`. Next, click on `Create New Project` to create a new project from scratch.

![Create a new project in RubyMine - Step 1](https://apidocs.io/illustration/ruby?workspaceFolder=NustLmsApi&step=createNewProject0)

Next, provide `TestApp` as the project name, choose `Rails Application` as the project type, and click `OK`.

![Create a new Rails Application in RubyMine - Step 2](https://apidocs.io/illustration/ruby?workspaceFolder=NustLmsApi&step=createNewProject1)

In the next dialog make sure that the correct Ruby SDK is being used (>= 2.6 and <= 3.2) and click `OK`.

![Create a new Rails Application in RubyMine - Step 3](https://apidocs.io/illustration/ruby?workspaceFolder=NustLmsApi&step=createNewProject2)

## 2. Add reference of the gem

In order to use the `nust_lms_api` gem in the new project we must add a gem reference. Locate the `Gemfile` in the Project Explorer window under the `TestApp` project node. The file contains references to all gems being used in the project. Here, add the reference to the library gem by adding the following line: `gem 'nust_lms_api', '1.0.0'`

![Add new reference to the Gemfile](https://apidocs.io/illustration/ruby?workspaceFolder=NustLmsApi&gemVer=1.0.0&gemName=nust_lms_api&step=addReference)

## 3. Adding a new Rails Controller

Once the `TestApp` project is created, a folder named `controllers` will be visible in the *Project Explorer* under the following path: `TestApp > app > controllers`. Right click on this folder and select `New -> Run Rails Generator...`.

![Run Rails Generator on Controllers Folder](https://apidocs.io/illustration/ruby?workspaceFolder=NustLmsApi&gemVer=1.0.0&gemName=nust_lms_api&step=addCode0)

Selecting the said option will popup a small window where the generator names are displayed. Here, select the `controller` template.

![Create a new Controller](https://apidocs.io/illustration/ruby?workspaceFolder=NustLmsApi&step=addCode1)

Next, a popup window will ask you for a Controller name and included Actions. For controller name provide `Hello` and include an action named `Index` and click `OK`.

![Add a new Controller](https://apidocs.io/illustration/ruby?workspaceFolder=NustLmsApi&gemVer=1.0.0&gemName=nust_lms_api&step=addCode2)

A new controller class named `HelloController` will be created in a file named `hello_controller.rb` containing a method named `Index`.

1. Add the `require 'nust_lms_api'` statement to require the gem in the controller file.
2. Add the `include NustLmsApi` statement to include the sdk module in the controller file.
3. In the `Index` method, add code for initialization and a sample for its usage.

![Initialize the library](https://apidocs.io/illustration/ruby?workspaceFolder=NustLmsApi&gemName=nust_lms_api&step=addCode3)


# Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

## Fields

| Name | Description |
|  --- | --- |
| PRODUCTION | **Default** NustDevKit Gateway (local development) |
| ENVIRONMENT2 | NustDevKit Gateway (production — replace with your deployed gateway URL) |


# Initialize the API Client

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| environment | [`Environment`](/llms-pages/ruby/getting-started/sdk-quickstart/environments.md) | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| connection | `Faraday::Connection` | The Faraday connection object passed by the SDK user for making requests |
| adapter | `Faraday::Adapter` | The Faraday adapter object passed by the SDK user for performing http requests |
| timeout | `Float` | The value to use for connection timeout. <br> **Default: 30** |
| max_retries | `Integer` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| retry_interval | `Float` | Pause in seconds between retries. <br> **Default: 1** |
| backoff_factor | `Float` | The amount to multiply each successive retry's interval amount by in order to provide backoff. <br> **Default: 2** |
| retry_statuses | `Array` | A list of HTTP statuses to retry. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524, 408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array` | A list of HTTP methods to retry. <br> **Default: %i[get put get put]** |
| http_callback | `HttpCallBack` | The Http CallBack allows defining callables for pre and post API calls. |
| proxy_settings | [`ProxySettings`](/llms-pages/ruby/sdk-infrastructure/configuration/proxysettings.md) | Optional proxy configuration to route HTTP requests through a proxy server. |
| logging_configuration | [`LoggingConfiguration`](/llms-pages/ruby/sdk-infrastructure/configuration/loggingconfiguration.md) | The SDK logging configuration for API calls |
| bearer_auth_credentials | [`BearerAuthCredentials`](/llms-pages/ruby/getting-started/sdk-quickstart/authorization.md) | The credential object for OAuth 2 Bearer token |

The API client can be initialized as follows:

## Code-Based Client Initialization

```ruby
require 'nust_lms_api'
include NustLmsApi

client = Client.new(
  bearer_auth_credentials: BearerAuthCredentials.new(
    access_token: 'AccessToken'
  ),
  environment: Environment::PRODUCTION,
  logging_configuration: LoggingConfiguration.new(
    log_level: Logger::INFO,
    request_logging_config: RequestLoggingConfiguration.new(
      log_body: true
    ),
    response_logging_config: ResponseLoggingConfiguration.new(
      log_headers: true
    )
  )
)
```

## Environment-Based Client Initialization

```ruby
require 'nust_lms_api'
include NustLmsApi

# Create client from environment
client = Client.from_env
```

See the [`Environment-Based Client Initialization`](/llms-pages/ruby/sdk-infrastructure/configuration/environment-based-client-initialization.md) section for details.


# Authorization

This API uses the following authentication schemes.

* [`BearerAuth (OAuth 2 Bearer token)`](/llms-pages/ruby/getting-started/sdk-quickstart/authorization.md)

## BearerAuth (OAuth 2 Bearer token)



Documentation for accessing and setting credentials for BearerAuth.

### Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| AccessToken | `String` | The OAuth 2.0 Access Token to use for API requests. | `access_token` |



**Note:** Auth credentials can be set using named parameter for any of the above credentials (e.g. `access_token`) in the client initialization.

### Usage Example

#### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```ruby
require 'nust_lms_api'
include NustLmsApi

client = Client.new(
  bearer_auth_credentials: BearerAuthCredentials.new(
    access_token: 'AccessToken'
  )
)
```




