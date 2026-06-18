# User Preferences Response

Source: /#/go/x-redirect/JTI0bSUyRlVzZXJQcmVmZXJlbmNlc1Jlc3BvbnNl

Response envelope for the user-preferences endpoint.

*This model accepts additional fields of type interface{}.*


# Class Name

`UserPreferencesResponse`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Preferences` | [`[]models.UserPreference`](/llms-pages/go/models/structures/user-preference.md) | Required | List of user preference key/value pairs. |
| `Warnings` | [`[]models.MoodleWarning`](/llms-pages/go/models/structures/moodle-warning.md) | Required | Array of warning objects. Empty when no warnings are present. |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
package main

import (
    "nustLmsApi/models"
)

func main() {
    userPreferencesResponse := models.UserPreferencesResponse{
        Preferences:           []models.UserPreference{
            models.UserPreference{
                Name:                  "block_myoverview_user_sort_preference",
                Value:                 "title",
                AdditionalProperties:  map[string]interface{}{
                    "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
                },
            },
        },
        Warnings:              []models.MoodleWarning{
            models.MoodleWarning{
                Item:                  models.ToPointer("item6"),
                Itemid:                models.ToPointer(0),
                Warningcode:           models.ToPointer("warningcode4"),
                Message:               models.ToPointer("message4"),
                AdditionalProperties:  map[string]interface{}{
                    "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
                },
            },
        },
        AdditionalProperties:  map[string]interface{}{
            "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
        },
    }

}
```



