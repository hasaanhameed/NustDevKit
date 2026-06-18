# SDK Quickstart

Source: /#/php/x-redirect/JTI0aCUyRl9fZ2V0dGluZ19zdGFydGVk


# Introduction

NUST Learning Management System API for developer integrations (Moodle AJAX wrapper). Each path is virtual for clean SDK generation; NustDevKit resolves them to the underlying Moodle AJAX service endpoint transparently.


# Building

The generated code has dependencies over external libraries like UniRest and JsonMapper. JsonMapper requires docblock annotations like `@var`, `@maps`, and `@factory` to map JSON responses with our class definitions. Hence the docblocks in generated code cannot be disabled by deactivating the PHP configurations like `opcache.save_comments`. These dependencies are defined in the `composer.json` file that comes with the SDK. To resolve these dependencies, we use the Composer package manager which requires PHP greater than or equal to 7.2 installed in your system. Visit [https://getcomposer.org/download/](https://getcomposer.org/download/) to download the installer file for Composer and run it in your system. Open command prompt and type `composer --version`. This should display the current version of the Composer installed if the installation was successful.

* Using command line, navigate to the directory containing the generated files (including `composer.json`) for the SDK.
* Run the command `composer install`. This should install all the required dependencies and create the `vendor` directory in your project directory.

![Building SDK - Step 1](https://apidocs.io/illustration/php?workspaceFolder=NustLmsApi&step=installDependencies)

## Configuring CURL Certificate Path in php.ini

:information_source: **Note** This is for Windows users only.

CURL used to include a list of accepted CAs, but no longer bundles ANY CA certs. So by default it will reject all SSL certificates as unverifiable. You will have to get your CA's cert and point curl at it. The steps are as follows:

1. Download the certificate bundle (.pem file) from [https://curl.haxx.se/docs/caextract.html](https://curl.haxx.se/docs/caextract.html) on to your system.
2. Add curl.cainfo = "PATH_TO/cacert.pem" to your php.ini file located in your php installation. “PATH_TO” must be an absolute path containing the .pem file.

```
[curl]; A default value for the CURLOPT_CAINFO option. This is required to be an
; absolute path.
curl.cainfo = PATH_TO/cacert.pem
```


# Installation

The following section explains how to use the NustLmsApiLib library in a new project.

## 1. Open Project in an IDE

Open an IDE for PHP like PhpStorm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PHPStorm - Step 1](https://apidocs.io/illustration/php?workspaceFolder=NustLmsApi&step=openIDE)

Click on `Open` in PhpStorm to browse to your generated SDK directory and then click `OK`.

![Open project in PHPStorm - Step 2](https://apidocs.io/illustration/php?workspaceFolder=NustLmsApi&step=openProject0)

## 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PHPStorm - Step 1](https://apidocs.io/illustration/php?workspaceFolder=NustLmsApi&step=createDirectory)

Name the directory as "test".

![Add a new project in PHPStorm - Step 2](https://apidocs.io/illustration/php?workspaceFolder=NustLmsApi&step=nameDirectory)

Add a PHP file to this project.

![Add a new project in PHPStorm - Step 3](https://apidocs.io/illustration/php?workspaceFolder=NustLmsApi&step=createFile)

Name it "testSDK".

![Add a new project in PHPStorm - Step 4](https://apidocs.io/illustration/php?workspaceFolder=NustLmsApi&step=nameFile)

Depending on your project setup, you might need to include composer's autoloader in your PHP code to enable auto loading of classes.

```php
require_once "vendor/autoload.php";
```

It is important that the path inside require_once correctly points to the file `autoload.php` inside the vendor directory created during dependency installations.

![Add a new project in PHPStorm - Step 5](https://apidocs.io/illustration/php?workspaceFolder=NustLmsApi&step=projectFiles)

After this you can add code to initialize the client library and acquire the instance of a Api class. Sample code to initialize the client library and use the Api methods is given in the subsequent sections.

## 3. Run the Test Project

To run your project you must set the Interpreter for your project. Interpreter is the PHP engine installed on your computer.

Open `Settings` from `File` menu.

![Run Test Project - Step 1](https://apidocs.io/illustration/php?workspaceFolder=NustLmsApi&step=openSettings)

Select `PHP` from within `Languages & Frameworks`.

![Run Test Project - Step 2](https://apidocs.io/illustration/php?workspaceFolder=NustLmsApi&step=setInterpreter0)

Browse for Interpreters near the `Interpreter` option and choose your interpreter.

![Run Test Project - Step 3](https://apidocs.io/illustration/php?workspaceFolder=NustLmsApi&step=setInterpreter1)

Once the interpreter is selected, click `OK`.

![Run Test Project - Step 4](https://apidocs.io/illustration/php?workspaceFolder=NustLmsApi&step=setInterpreter2)

To run your project, right click on your PHP file inside your Test project and click on `Run`.

![Run Test Project - Step 5](https://apidocs.io/illustration/php?workspaceFolder=NustLmsApi&step=runProject)



# Initialize the API Client

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| timeout | `int` | Timeout for API calls in seconds.<br>*Default*: `30` |
| enableRetries | `bool` | Whether to enable retries and backoff feature.<br>*Default*: `false` |
| numberOfRetries | `int` | The number of retries to make.<br>*Default*: `0` |
| retryInterval | `float` | The retry time interval between the endpoint calls.<br>*Default*: `1` |
| backOffFactor | `float` | Exponential backoff factor to increase interval between retries.<br>*Default*: `2` |
| maximumRetryWaitTime | `int` | The maximum wait time in seconds for overall retrying requests.<br>*Default*: `0` |
| retryOnTimeout | `bool` | Whether to retry on request timeout.<br>*Default*: `true` |
| httpStatusCodesToRetry | `array` | Http status codes to retry against.<br>*Default*: `408, 413, 429, 500, 502, 503, 504, 521, 522, 524, 408, 413, 429, 500, 502, 503, 504, 521, 522, 524` |
| httpMethodsToRetry | `array` | Http methods to retry against.<br>*Default*: `'GET', 'PUT', 'GET', 'PUT'` |
| loggingConfiguration | [`LoggingConfigurationBuilder`](/llms-pages/php/sdk-infrastructure/configuration/loggingconfigurationbuilder.md) | Represents the logging configurations for API calls |
| proxyConfiguration | [`ProxyConfigurationBuilder`](/llms-pages/php/sdk-infrastructure/configuration/proxyconfigurationbuilder.md) | Represents the proxy configurations for API calls |
| customQueryAuthenticationCredentials | [`CustomQueryAuthenticationCredentials`](/llms-pages/php/getting-started/sdk-quickstart/authorization.md) | The Credentials Setter for Custom Query Parameter |

The API client can be initialized as follows:

```php
use NustLmsApiLib\Logging\LoggingConfigurationBuilder;
use NustLmsApiLib\Logging\RequestLoggingConfigurationBuilder;
use NustLmsApiLib\Logging\ResponseLoggingConfigurationBuilder;
use Psr\Log\LogLevel;
use NustLmsApiLib\Authentication\CustomQueryAuthenticationCredentialsBuilder;
use NustLmsApiLib\NustLmsApiClientBuilder;

$client = NustLmsApiClientBuilder::init()
    ->customQueryAuthenticationCredentials(
        CustomQueryAuthenticationCredentialsBuilder::init(
            'sesskey'
        )
    )
    ->loggingConfiguration(
        LoggingConfigurationBuilder::init()
            ->level(LogLevel::INFO)
            ->requestConfiguration(RequestLoggingConfigurationBuilder::init()->body(true))
            ->responseConfiguration(ResponseLoggingConfigurationBuilder::init()->headers(true))
    )
    ->build();
```


# Authorization

This API uses the following authentication schemes.

* [`SessKey (Custom Query Parameter)`](/llms-pages/php/getting-started/sdk-quickstart/authorization.md)

## SessKey (Custom Query Parameter)



Documentation for accessing and setting credentials for SessKey.

### Auth Credentials

| Name | Type | Description | Setter | Getter |
|  --- | --- | --- | --- | --- |
| sesskey | `string` | Session key obtained after authenticating with the LMS portal. | `sesskey` | `getSesskey()` |



**Note:** Auth credentials can be set using `CustomQueryAuthenticationCredentialsBuilder::init()` in `customQueryAuthenticationCredentials` method in the client builder and accessed through `getCustomQueryAuthenticationCredentials` method in the client instance.

### Usage Example

#### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```php
use NustLmsApiLib\Authentication\CustomQueryAuthenticationCredentialsBuilder;
use NustLmsApiLib\NustLmsApiClientBuilder;

$client = NustLmsApiClientBuilder::init()
    ->customQueryAuthenticationCredentials(
        CustomQueryAuthenticationCredentialsBuilder::init(
            'sesskey'
        )
    )
    ->build();
```




