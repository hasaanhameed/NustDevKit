# AbstractLogger

Source: /#/ruby/x-redirect/JTI0aCUyRl9fYWRkaXRpb25hbF9kb2N1bWVudGF0aW9uJTJGQ29uZmlndXJhdGlvbiUyRkFic3RyYWN0TG9nZ2Vy

An abstract class for custom logger implementation.

# Logger Methods

| Name | Description | Return Type | Parameters | Method Signature |
|  --- | --- | --- | --- | --- |
| log | Logs a message with a specified log level and additional parameters. | nil | 1. level (Integer): The log level of the message.<br>2. message (String): The message template to log.<br>3. params: (Hash): The parameters to include in the log message. | log(level, message, params) |

# Usage Example

## Client Initialization with Custom Logger

In order to provide custom logger implementation, the `AbstractLogger` class must be inherited so that you can override the `log` behavior.

```ruby
require 'ougai'
require 'logger'

include NustLmsApi


class CustomLogger < AbstractLogger
  def initialize
    @logger = Ougai::Logger.new($stdout)
  end
  def log(level, message, params)
    case level
    when Logger::INFO
      @logger.info(message, params)
    end
  end
end
```

Following is how the custom logger implementation can be injected in the SDK client.

```ruby
require 'nust_lms_api'
include NustLmsApi

client = Client.new(
  logging_configuration: LoggingConfiguration.new(
    logger: CustomLogger.new
  )
)
```



