# Site Notification

Source: /#/go/x-redirect/JTI0bSUyRlNpdGVOb3RpZmljYXRpb24

A site-level notification (structure varies by type).

*This model accepts additional fields of type interface{}.*


# Class Name

`SiteNotification`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Id` | `*int` | Optional | Unique identifier for the site notification. |
| `Message` | `*string` | Optional | Notification message content. |
| `Type` | `*string` | Optional | Notification type identifier. |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
package main

import (
    "nustLmsApi/models"
)

func main() {
    siteNotification := models.SiteNotification{
        Id:                    models.ToPointer(96),
        Message:               models.ToPointer("message8"),
        Type:                  models.ToPointer("type8"),
        AdditionalProperties:  map[string]interface{}{
            "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
        },
    }

}
```



