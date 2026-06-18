# ResponseLoggingConfiguration

Source: /#/ruby/x-redirect/JTI0aCUyRl9fYWRkaXRpb25hbF9kb2N1bWVudGF0aW9uJTJGQ29uZmlndXJhdGlvbiUyRlJlc3BvbnNlTG9nZ2luZ0NvbmZpZ3VyYXRpb24

Represents the logging configuration for API response.

# Parameters

| Name | Type | Tag | Description |
|  --- | --- | --- | --- |
| log_body | `Boolean` | optional | Toggles the logging of the response body. **Default : `false`** |
| log_headers | `Boolean` | optional | Toggles the logging of the response headers. **Default : `false`** |
| headers_to_include | `Array` | optional | Includes only specified response headers in the log output. **Default : `[]`** |
| headers_to_exclude | `Array` | optional | Excludes specified request headers from the log output. **Default : `[]`** |
| headers_to_unmask | `Array` | optional | Logs specified request headers without masking, revealing their actual values. **Default : `[]`** |



