# Login Request

Source: /#/go/x-redirect/JTI0bSUyRkxvZ2luUmVxdWVzdA

NUST LMS credentials used to obtain a gateway bearer token.

*This model accepts additional fields of type interface{}.*


# Class Name

`LoginRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Email` | `string` | Required | NUST LMS username or email. |
| `Password` | `string` | Required | NUST LMS password. |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
package main

import (
    "nustLmsApi/models"
)

func main() {
    loginRequest := models.LoginRequest{
        Email:                 "john.doe@student.nust.edu.pk",
        Password:              "password2",
        AdditionalProperties:  map[string]interface{}{
            "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
        },
    }

}
```



