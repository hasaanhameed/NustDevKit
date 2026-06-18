# SDK Quickstart

Source: /#/typescript/x-redirect/JTI0aCUyRl9fZ2V0dGluZ19zdGFydGVk


# Introduction

NUST Learning Management System API for developer integrations (Moodle AJAX wrapper). Each path is virtual for clean SDK generation; NustDevKit resolves them to the underlying Moodle AJAX service endpoint transparently.


# Building

## Requirements

The SDK relies on **Node.js** and **npm** (to resolve dependencies). It also requires **Typescript version >=4.1**. You can download and install Node.js and [npm](https://www.npmjs.com/) from [the official Node.js website](https://nodejs.org/en/download/).

> **NOTE:** npm is installed by default when Node.js is installed.

## Verify Successful Installation

Run the following commands in the command prompt or shell of your choice to check if Node.js and npm are successfully installed:

* Node.js: `node --version`

* npm: `npm --version`

![Version Check](https://apidocs.io/illustration/typescript?workspaceFolder=NustLmsApi&step=versionCheck)

## Install Dependencies

- To resolve all dependencies, go to the **SDK root directory** and run the following command with npm:

```bash
npm install
```

- This will install all dependencies in the **node_modules** folder.

![Resolve Dependencies](https://apidocs.io/illustration/typescript?workspaceFolder=NustLmsApi&workspaceName=nust-lms-apilib&step=resolveDependency)


# Installation

The following section explains how to use the generated library in a new project.

## 1. Initialize the Node Project

- Open an IDE/text editor for JavaScript like Visual Studio Code. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

- Click on **File** and select **Open Folder**. Select an empty folder of your project, the folder will become visible in the sidebar on the left.

![Open Folder](https://apidocs.io/illustration/typescript?step=openProject)

- To initialize the Node project, click on **Terminal** and select **New Terminal**. Execute the following command in the terminal:

```bash
npm init --y
```

![Initialize the Node Project](https://apidocs.io/illustration/typescript?step=initializeProject)

## 2. Add Dependencies to the Client Library

- The created project manages its dependencies using its `package.json` file. In order to add a dependency on the *NUST LMS APILib* client library, double click on the `package.json` file in the bar on the left and add the dependency to the package in it.

![Add NustLmsApilib Dependency](https://apidocs.io/illustration/typescript?workspaceFolder=NustLmsApi&workspaceName=nust-lms-apilib&step=importDependency)

- To install the package in the project, run the following command in the terminal:

```bash
npm install
```

![Install NustLmsApilib Dependency](https://apidocs.io/illustration/typescript?step=installDependency)



# Initialize the API Client

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| timeout | `number` | Timeout for API calls.<br>*Default*: `30000` |
| httpClientOptions | [`Partial<HttpClientOptions>`](/llms-pages/typescript/sdk-infrastructure/configuration/httpclientoptions.md) | Stable configurable http client options. |
| unstableHttpClientOptions | `any` | Unstable configurable http client options. |
| logging | [`PartialLoggingOptions`](/llms-pages/typescript/sdk-infrastructure/configuration/partialloggingoptions.md) | Logging Configuration to enable logging |
| customQueryAuthenticationCredentials | [`CustomQueryAuthenticationCredentials`](/llms-pages/typescript/getting-started/sdk-quickstart/authorization.md) | The credential object for customQueryAuthentication |

The API client can be initialized as follows:

## Code-Based Client Initialization

```ts
import { Client, LogLevel } from 'nust-lms-apilib';

const client = new Client({
  customQueryAuthenticationCredentials: {
    'sesskey': 'sesskey'
  },
  timeout: 30000,
  logging: {
    logLevel: LogLevel.Info,
    logRequest: {
      logBody: true
    },
    logResponse: {
      logHeaders: true
    }
  },
});
```

## Configuration-Based Client Initialization

```ts
import * as path from 'path';
import * as fs from 'fs';
import { Client } from 'nust-lms-apilib';

// Provide absolute path for the configuration file
const absolutePath = path.resolve('./config.json');

// Read the configuration file content
const fileContent = fs.readFileSync(absolutePath, 'utf-8');

// Initialize client from JSON configuration content
const client = Client.fromJsonConfig(fileContent);
```

See the [Configuration-Based Client Initialization](/llms-pages/typescript/sdk-infrastructure/configuration/configuration-based-client-initialization.md) section for details.

## Environment-Based Client Initialization

```ts
import * as dotenv from 'dotenv';
import * as path from 'path';
import * as fs from 'fs';
import { Client } from 'nust-lms-apilib';

// Optional - Provide absolute path for the .env file
const absolutePath = path.resolve('./.env');

if (fs.existsSync(absolutePath)) {
  // Load environment variables from .env file
  dotenv.config({ path: absolutePath, override: true });
}

// Initialize client using environment variables
const client = Client.fromEnvironment(process.env);
```

See the [Environment-Based Client Initialization](/llms-pages/typescript/sdk-infrastructure/configuration/environment-based-client-initialization.md) section for details.


# Authorization

This API uses the following authentication schemes.

* [`SessKey (Custom Query Parameter)`](/llms-pages/typescript/getting-started/sdk-quickstart/authorization.md)

## SessKey (Custom Query Parameter)



Documentation for accessing and setting credentials for SessKey.

### Auth Credentials

| Name | Type | Description | Setter |
|  --- | --- | --- | --- |
| sesskey | `string` | Session key obtained after authenticating with the LMS portal. | `sesskey` |



**Note:** Auth credentials can be set using `customQueryAuthenticationCredentials` object in the client.

### Usage Example

#### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```ts
import { Client } from 'nust-lms-apilib';

const client = new Client({
  customQueryAuthenticationCredentials: {
    'sesskey': 'sesskey'
  },
});
```




