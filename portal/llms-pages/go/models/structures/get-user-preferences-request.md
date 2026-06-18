# Get User Preferences Request

Source: /#/go/x-redirect/JTI0bSUyRkdldFVzZXJQcmVmZXJlbmNlc1JlcXVlc3Q

Request parameters for retrieving user preferences.

*This model accepts additional fields of type interface{}.*


# Class Name

`GetUserPreferencesRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Userid` | `int` | Required | ID of the user whose preferences to retrieve. |
| `Name` | `*string` | Optional | Specific preference name to retrieve. Omit to retrieve all preferences. |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
package main

import (
    "nustLmsApi/models"
)

func main() {
    getUserPreferencesRequest := models.GetUserPreferencesRequest{
        Userid:                162154,
        Name:                  models.ToPointer("name6"),
        AdditionalProperties:  map[string]interface{}{
            "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
        },
    }

}
```



