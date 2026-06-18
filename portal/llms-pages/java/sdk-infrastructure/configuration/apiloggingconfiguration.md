# ApiLoggingConfiguration

Source: /#/java/x-redirect/JTI0aCUyRl9fYWRkaXRpb25hbF9kb2N1bWVudGF0aW9uJTJGQ29uZmlndXJhdGlvbiUyRkFwaUxvZ2dpbmdDb25maWd1cmF0aW9u

Class for holding logging configuration.

# Methods

| Name | Description | Return Type |
|  --- | --- | --- |
| `getLevel()` | Getter for level. | `org.slf4j.event.Level` |
| `getLogger()` | Getter for provided logger. | `org.slf4j.Logger` |
| `getMaskSensitiveHeaders()` | Getter for the masking sensitive headers flag. | `boolean` |
| `getRequestConfig()` | Getter for request log configuration. | `ReadonlyRequestLoggingConfiguration` |
| `getResponseConfig()` | Getter for response log configuration. | `ReadonlyResponseLoggingConfiguration` |
| `toString()` | Converts this ApiLoggingConfiguration into string format. | `String` |
| `newBuilder()` | Builds a new ApiLoggingConfiguration.Builder object. Creates the instance with the current state. | [`ApiLoggingConfiguration.Builder`](/llms-pages/java/sdk-infrastructure/configuration/apiloggingconfiguration-builder.md) |



