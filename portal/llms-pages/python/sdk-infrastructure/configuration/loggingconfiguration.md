# LoggingConfiguration

Source: /#/python/x-redirect/JTI0aCUyRl9fYWRkaXRpb25hbF9kb2N1bWVudGF0aW9uJTJGQ29uZmlndXJhdGlvbiUyRkxvZ2dpbmdDb25maWd1cmF0aW9u

Represents the logging configuration for API calls.

# Parameters

| Name | Type | Tag | Description |
|  --- | --- | --- | --- |
| logger | [`AbstractLogger`](/llms-pages/python/sdk-infrastructure/configuration/abstractlogger.md) | optional | Takes in your custom implementation of the abstract logger class here. **Default Implementation : `ConsoleLogger`** |
| log_level | `int` | optional | Defines the log message severity mentioned in python logging module (e.g., DEBUG, INFO, WARN\|WARNING, ERROR, FATAL\|CRITICAL). **Default : `logging.INFO`** |
| mask_sensitive_headers | `bool` | optional | Toggles the global setting to mask sensitive HTTP headers in both requests and responses before logging, safeguarding confidential data. **Default : `True`** |
| request_logging_config | [`RequestLoggingConfiguration`](/llms-pages/python/sdk-infrastructure/configuration/requestloggingconfiguration.md) | optional | The logging configuration for an API request. |
| response_logging_config | [`ResponseLoggingConfiguration`](/llms-pages/python/sdk-infrastructure/configuration/responseloggingconfiguration.md) | optional | The logging configuration for an API response. |



