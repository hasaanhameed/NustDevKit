# ApiLoggingConfiguration.Builder

Source: /#/java/x-redirect/JTI0aCUyRl9fYWRkaXRpb25hbF9kb2N1bWVudGF0aW9uJTJGQ29uZmlndXJhdGlvbiUyRkFwaUxvZ2dpbmdDb25maWd1cmF0aW9uLkJ1aWxkZXI

Class to build instances of ApiLoggingConfiguration.

# Constructors

| Name | Description |
|  --- | --- |
| `Builder()` | Default Constructor to initiate builder with default properties. |

# Methods

| Name | Description |
|  --- | --- |
| `level(org.slf4j.event.Level level)` | Set level for logging. Default level is INFO. Other available levels are `ERROR`, `WARN`, `DEBUG`, and `TRACE`. |
| `logger(org.slf4j.Logger logger)` | Set Logger for logging. Here you can provide custom slf4j implementation if needed. |
| `maskSensitiveHeaders(boolean maskSensitiveHeaders)` | Set mask sensitive headers flag. Default value is true. |
| `requestConfig(Consumer<ApiRequestLoggingConfiguration.Builder> consumer)` | Sets the [`ApiRequestLoggingConfiguration.Builder`](/llms-pages/java/sdk-infrastructure/configuration/apirequestloggingconfiguration-builder.md) for the builder. |
| `responseConfig(Consumer<ApiResponseLoggingConfiguration.Builder> consumer)` | Sets the [`ApiResponseLoggingConfiguration.Builder`](/llms-pages/java/sdk-infrastructure/configuration/apiresponseloggingconfiguration-builder.md) for the builder. |
| `build()` | Builds a new [`ApiLoggingConfiguration`](/llms-pages/java/sdk-infrastructure/configuration/apiloggingconfiguration.md) object using the set fields. |

# Usage Example

## Add Logger dependencies to Project

In order to provide custom logger, any implementation of the logging facade `org.slf4j.Logger` can be used by adding its dependencies to the `pom.xml`.

```xml
<dependencies>
    <dependency>
        <groupId>org.apache.logging.log4j</groupId>
        <artifactId>log4j-api</artifactId>
        <version>${log4j.version}</version>
    </dependency>
    <dependency>
        <groupId>org.apache.logging.log4j</groupId>
        <artifactId>log4j-core</artifactId>
        <version>${log4j.version}</version>
    </dependency>
    <dependency>
        <groupId>org.apache.logging.log4j</groupId>
        <artifactId>log4j-slf4j2-impl</artifactId>
        <version>${log4j.version}</version>
    </dependency>
    <dependency>
        <groupId>org.apache.logging.log4j</groupId>
        <artifactId>log4j-layout-template-json</artifactId>
        <version>${log4j.version}</version>
    </dependency>
</dependencies>
```

## Create Logger Configuration

As we are using `org.apache.logging.log4j` dependency which itself provides its own logging API and implementation using the logging facade `org.slf4j.Logger`. So we would need to create a `log4j2.xml` configuration file and add it to the project's build path.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Configuration>
    <Appenders>
        <Console name="Console" target="SYSTEM_OUT">
            <JsonTemplateLayout eventTemplateUri="classpath:EcsLayout.json"/>
        </Console>
    </Appenders>
    <Loggers>
        <Root level="trace">
            <AppenderRef ref="Console" />
        </Root>
    </Loggers>
</Configuration>
```

## Client Initialization with Custom Logger

The following example uses the `LoggerFactory.getLogger` to get the underlying log4j implementation from the project's build path for NustLmsApiClient initialization.

```java
package examples;

import com.nustdevkit.api.NustLmsApiClient;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.slf4j.event.Level;

public class App {
    private static final Logger CUSTOM_LOGGER = LoggerFactory.getLogger(App.class);

    public static void main(String[] args) {
        NustLmsApiClient client = new NustLmsApiClient.Builder()
            .loggingConfig(builder -> builder
                .logger(CUSTOM_LOGGER)
                .level(Level.DEBUG)
                .requestConfig(logConfigBuilder -> logConfigBuilder.body(true))
                .responseConfig(logConfigBuilder -> logConfigBuilder.headers(true)))
            .build();
    }
}
```



