# ResponseLoggingConfiguration

Source: /#/python/x-redirect/JTI0aCUyRl9fYWRkaXRpb25hbF9kb2N1bWVudGF0aW9uJTJGQ29uZmlndXJhdGlvbiUyRlJlc3BvbnNlTG9nZ2luZ0NvbmZpZ3VyYXRpb24

Represents the logging configuration for API response.

# Parameters

| Name | Type | Tag | Description |
|  --- | --- | --- | --- |
| log_body | `bool` | optional | Toggles the logging of the response body. **Default : `False`** |
| log_headers | `bool` | optional | Toggles the logging of the response headers. **Default : `False`** |
| headers_to_include | `List[str]` | optional | Includes only specified response headers in the log output. **Default : `[]`** |
| headers_to_exclude | `List[str]` | optional | Excludes specified response headers from the log output. **Default : `[]`** |
| headers_to_unmask | `List[str]` | optional | Logs specified response headers without masking, revealing their actual values. **Default : `[]`** |



