# PartialLoggingOptions

Source: /#/typescript/x-redirect/JTI0aCUyRl9fYWRkaXRpb25hbF9kb2N1bWVudGF0aW9uJTJGQ29uZmlndXJhdGlvbiUyRlBhcnRpYWxMb2dnaW5nT3B0aW9ucw

Represents the logging configurations for API calls.

# Properties

| Name | Type | Description |
|  --- | --- | --- |
| logger | [`LoggerInterface`](/llms-pages/typescript/sdk-infrastructure/configuration/loggerinterface.md) | logger to be configured. <br> *Default*: `new ConsoleLogger()` |
| logLevel | `LogLevel` | Set log level. <br> *Default*: `LogLevel.Info` |
| maskSensitiveHeaders | `boolean` | Enable masking senstive headers <br> *Default*: `true` |
| logRequest | [`PartialRequestLoggingOptions`](/llms-pages/typescript/sdk-infrastructure/configuration/partialrequestloggingoptions.md) | Set request information options <br> *Default*: `{}` |
| logResponse | [`PartialResponseLoggingOptions`](/llms-pages/typescript/sdk-infrastructure/configuration/partialresponseloggingoptions.md) | Set response information options <br> *Default*: `{}` |



