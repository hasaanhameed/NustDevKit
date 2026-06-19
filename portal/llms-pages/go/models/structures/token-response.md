# Token Response

Source: /#/go/x-redirect/JTI0bSUyRlRva2VuUmVzcG9uc2U

Bearer token issued by the gateway after a successful login.

*This model accepts additional fields of type interface{}.*


# Class Name

`TokenResponse`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `AccessToken` | `string` | Required | JWT to send as `Authorization: Bearer <token>` on subsequent requests. |
| `TokenType` | `string` | Required | **Default**: `"bearer"` |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
package main

import (
    "nustLmsApi/models"
)

func main() {
    tokenResponse := models.TokenResponse{
        AccessToken:           "access_token2",
        TokenType:             "bearer",
        AdditionalProperties:  map[string]interface{}{
            "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
        },
    }

}
```



