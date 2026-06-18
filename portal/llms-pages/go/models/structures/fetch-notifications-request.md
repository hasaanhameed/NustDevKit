# Fetch Notifications Request

Source: /#/go/x-redirect/JTI0bSUyRkZldGNoTm90aWZpY2F0aW9uc1JlcXVlc3Q

Request parameters for fetching site-level notifications.

*This model accepts additional fields of type interface{}.*


# Class Name

`FetchNotificationsRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Contextid` | `int` | Required | Moodle context ID for which to fetch notifications. The user context ID can be found in the user profile image URL path segment. |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
package main

import (
    "nustLmsApi/models"
)

func main() {
    fetchNotificationsRequest := models.FetchNotificationsRequest{
        Contextid:             1583361,
        AdditionalProperties:  map[string]interface{}{
            "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
        },
    }

}
```



