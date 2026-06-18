# Get Popup Notifications Request

Source: /#/go/x-redirect/JTI0bSUyRkdldFBvcHVwTm90aWZpY2F0aW9uc1JlcXVlc3Q

Request parameters for retrieving popup notifications for a user.

*This model accepts additional fields of type interface{}.*


# Class Name

`GetPopupNotificationsRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Useridto` | `string` | Required | ID of the recipient user, passed as a string. |
| `Limit` | `int` | Required | Maximum number of notifications to return. |
| `Offset` | `int` | Required | Pagination offset.<br><br>**Default**: `0` |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
package main

import (
    "nustLmsApi/models"
)

func main() {
    getPopupNotificationsRequest := models.GetPopupNotificationsRequest{
        Useridto:              "162154",
        Limit:                 20,
        Offset:                0,
        AdditionalProperties:  map[string]interface{}{
            "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
        },
    }

}
```



