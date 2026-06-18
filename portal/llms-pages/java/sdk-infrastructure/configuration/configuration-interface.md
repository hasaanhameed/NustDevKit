# Configuration Interface

Source: /#/java/x-redirect/JTI0aCUyRl9fYWRkaXRpb25hbF9kb2N1bWVudGF0aW9uJTJGQ29uZmlndXJhdGlvbiUyRkNvbmZpZ3VyYXRpb24lMjUyMEludGVyZmFjZQ

This is the interface for client class that holds the configuration getters.

# Methods

| Name | Description | Return Type |
|  --- | --- | --- |
| `getEnvironment()` | Current API environment. | `Environment` |
| `getHttpClientConfig()` | Http Client Configuration instance. | [`ReadonlyHttpClientConfiguration`](/llms-pages/java/sdk-infrastructure/configuration/httpclientconfiguration.md) |
| `getLoggingConfig()` | Logging Configuration instance. | [`ReadonlyLoggingConfiguration`](/llms-pages/java/sdk-infrastructure/configuration/apiloggingconfiguration.md) |
| `getBaseUri(Server server)` | Get base URI by current environment. | `String` |
| `getBaseUri()` | Get base URI by current environment. | `String` |



