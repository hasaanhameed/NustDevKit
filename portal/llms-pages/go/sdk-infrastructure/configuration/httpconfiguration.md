# HttpConfiguration

Source: /#/go/x-redirect/JTI0aCUyRl9fYWRkaXRpb25hbF9kb2N1bWVudGF0aW9uJTJGQ29uZmlndXJhdGlvbiUyRkh0dHBDb25maWd1cmF0aW9u

The following parameters are configurable for the HttpConfiguration:

# Properties

| Name | Type | Description | Setter | Getter |
|  --- | --- | --- | --- | --- |
| timeout | `float64` | Timeout in seconds.<br>*Default*: `30` | `WithTimeout` | `Timeout()` |
| transport | `httpRoundTripper` | Establishes network connection and caches them for reuse.<br>*Default*: `http.DefaultTransport` | `WithTransport` | `Transport()` |
| retryConfiguration | [`nustLmsApiRetryConfiguration`](/llms-pages/go/sdk-infrastructure/configuration/retryconfiguration.md) | Configurations to retry requests.<br>*Default*: `nustLmsApi.DefaultRetryConfiguration()` | `WithRetryConfiguration` | `RetryConfiguration()` |

The httpConfiguration can be initialized as follows:

```go
package main

import (
    "nustLmsApi"
    "net/http"
)

func main() {
    httpConfiguration := nustLmsApi.CreateHttpConfiguration(
        nustLmsApi.WithTimeout(30),
        nustLmsApi.WithTransport(http.DefaultTransport),
        nustLmsApi.WithRetryConfiguration(nustLmsApi.DefaultRetryConfiguration()),
    )
}
```



