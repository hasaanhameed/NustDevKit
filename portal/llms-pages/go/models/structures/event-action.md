# Event Action

Source: /#/go/x-redirect/JTI0bSUyRkV2ZW50QWN0aW9u

Primary action button metadata for a calendar event.

*This model accepts additional fields of type interface{}.*


# Class Name

`EventAction`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Name` | `string` | Required | Display label for the primary action button. |
| `Url` | `string` | Required | URL the user should navigate to in order to perform the action. |
| `Itemcount` | `int` | Required | Number of items associated with this action. |
| `Actionable` | `bool` | Required | Whether the action can currently be taken by the user. |
| `Showitemcount` | `bool` | Required | Whether to display the item count alongside the action label. |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
package main

import (
    "nustLmsApi/models"
)

func main() {
    eventAction := models.EventAction{
        Name:                  "Add submission",
        Url:                   "https://lms.nust.edu.pk/portal/mod/assign/view.php?id=999404&action=editsubmission",
        Itemcount:             1,
        Actionable:            true,
        Showitemcount:         false,
        AdditionalProperties:  map[string]interface{}{
            "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
        },
    }

}
```



