# ResponseLoggingConfigurationBuilder

Source: /#/php/x-redirect/JTI0aCUyRl9fYWRkaXRpb25hbF9kb2N1bWVudGF0aW9uJTJGQ29uZmlndXJhdGlvbiUyRlJlc3BvbnNlTG9nZ2luZ0NvbmZpZ3VyYXRpb25CdWlsZGVy

Represents the logging configurations for API responses. Create instance using `ResponseLoggingConfigurationBuilder::init()`

# Methods

| Name | Parameter Type | Description |
|  --- | --- | --- |
| `body` | `bool` | Toggles the logging of the request body. **Default : `false`** |
| `headers` | `bool` | Toggles the logging of the request headers. **Default : `false`** |
| `includeHeaders` | `string[]` | Includes only specified request headers in the log output. **Default : `[]`** |
| `excludeHeaders` | `string[]` | Excludes specified request headers from the log output. **Default : `[]`** |
| `unmaskHeaders` | `string[]` | Logs specified request headers without masking, revealing their actual values. **Default : `[]`** |



