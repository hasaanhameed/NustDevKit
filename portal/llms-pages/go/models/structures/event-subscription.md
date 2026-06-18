# Event Subscription

Source: /#/go/x-redirect/JTI0bSUyRkV2ZW50U3Vic2NyaXB0aW9u

Subscription display settings for a calendar event.

*This model accepts additional fields of type interface{}.*


# Class Name

`EventSubscription`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Displayeventsource` | `bool` | Required | Whether to display the event source label on the calendar. |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
package main

import (
    "nustLmsApi/models"
)

func main() {
    eventSubscription := models.EventSubscription{
        Displayeventsource:    false,
        AdditionalProperties:  map[string]interface{}{
            "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
        },
    }

}
```



