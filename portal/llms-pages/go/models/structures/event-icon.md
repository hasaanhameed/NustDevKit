# Event Icon

Source: /#/go/x-redirect/JTI0bSUyRkV2ZW50SWNvbg

Icon metadata for a calendar event.

*This model accepts additional fields of type interface{}.*


# Class Name

`EventIcon`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Key` | `string` | Required | Icon key name used to locate the icon asset. |
| `Component` | `string` | Required | Moodle component that owns the icon (e.g., 'assign'). |
| `Alttext` | `string` | Required | Accessible alt text for the icon image. |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
package main

import (
    "nustLmsApi/models"
)

func main() {
    eventIcon := models.EventIcon{
        Key:                   "icon",
        Component:             "assign",
        Alttext:               "Activity event",
        AdditionalProperties:  map[string]interface{}{
            "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
        },
    }

}
```



