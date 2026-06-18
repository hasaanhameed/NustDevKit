# User Preference

Source: /#/go/x-redirect/JTI0bSUyRlVzZXJQcmVmZXJlbmNl

A single user preference setting.

*This model accepts additional fields of type interface{}.*


# Class Name

`UserPreference`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Name` | `string` | Required | Unique key identifying the preference. |
| `Value` | `string` | Required | Preference value as a string. Note that the internal _lastloaded preference is returned as an integer by the LMS. |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
package main

import (
    "nustLmsApi/models"
)

func main() {
    userPreference := models.UserPreference{
        Name:                  "block_myoverview_user_sort_preference",
        Value:                 "title",
        AdditionalProperties:  map[string]interface{}{
            "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
        },
    }

}
```



