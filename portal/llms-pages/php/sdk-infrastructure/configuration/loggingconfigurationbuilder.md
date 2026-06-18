# LoggingConfigurationBuilder

Source: /#/php/x-redirect/JTI0aCUyRl9fYWRkaXRpb25hbF9kb2N1bWVudGF0aW9uJTJGQ29uZmlndXJhdGlvbiUyRkxvZ2dpbmdDb25maWd1cmF0aW9uQnVpbGRlcg

Represents the logging configurations for API calls. Create instance using `LoggingConfigurationBuilder::init()`

# Methods

| Name | Parameter Type | Description |
|  --- | --- | --- |
| `logger` | `LoggerInterface` | Takes in your custom implementation of the Psr\Log\LoggerInterface.php. **Default Implementation : `ConsoleLogger`** |
| `level` | `string(LogLevel)` | Defines the log message severity mentioned in Psr\Log\LogLevel.php (e.g., DEBUG, INFO, etc). **Default : `logLevel::INFO`** |
| `maskSensitiveHeaders` | `bool` | Toggles the global setting to mask sensitive HTTP headers in both requests and responses before logging, safeguarding confidential data. **Default : `true`** |
| `requestConfiguration` | [`RequestLoggingConfigurationBuilder`](/llms-pages/php/sdk-infrastructure/configuration/requestloggingconfigurationbuilder.md) | The logging configurations for an API request. |
| `responseConfiguration` | [`ResponseLoggingConfigurationBuilder`](/llms-pages/php/sdk-infrastructure/configuration/responseloggingconfigurationbuilder.md) | The logging configurations for an API response. |

# Usage Example

## Client Initialization with Custom Logger

In order to provide custom logger, any implementation of the `Psr\Log\LoggerInterface` can be used so that you can override the `log` behavior and provide its instance directly in the SDK client initialization.

The following example uses `Monolog\Logger` implementation of `Psr\Log\LoggerInterface` for NustLmsApiClient initialization.

```php
<?php

use NustLmsApiLib\NustLmsApiClientBuilder;
use NustLmsApiLib\Logging\LoggingConfigurationBuilder;
use NustLmsApiLib\Logging\RequestLoggingConfigurationBuilder;
use NustLmsApiLib\Logging\ResponseLoggingConfigurationBuilder;
use Psr\Log\LogLevel;
use Monolog\Logger;
use Monolog\Handler\StreamHandler;

// create a log channel
$logger = new Logger('NustLmsApi');
$logger->pushHandler(new StreamHandler(__DIR__ . '/api_data.log'));

// initialize the sdk client using this logger
$client = NustLmsApiClientBuilder::init()
    ->loggingConfiguration(
        LoggingConfigurationBuilder::init()
            ->logger($logger)
            ->level(LogLevel::INFO)
            ->requestConfiguration(RequestLoggingConfigurationBuilder::init()->body(true))
            ->responseConfiguration(ResponseLoggingConfigurationBuilder::init()->headers(true))
    )
    ->build();
```



