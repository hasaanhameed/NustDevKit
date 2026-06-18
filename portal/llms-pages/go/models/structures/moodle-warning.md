# Moodle Warning

Source: /#/go/x-redirect/JTI0bSUyRk1vb2RsZVdhcm5pbmc

A non-fatal warning returned alongside a successful response.

*This model accepts additional fields of type interface{}.*


# Class Name

`MoodleWarning`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Item` | `*string` | Optional | Item identifier related to the warning; empty string if not applicable. |
| `Itemid` | `*int` | Optional | Numeric item ID related to the warning; 0 if not applicable. |
| `Warningcode` | `*string` | Optional | Machine-readable warning code; empty string if no code. |
| `Message` | `*string` | Optional | Human-readable warning description. |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
package main

import (
    "nustLmsApi/models"
)

func main() {
    moodleWarning := models.MoodleWarning{
        Item:                  models.ToPointer("item6"),
        Itemid:                models.ToPointer(0),
        Warningcode:           models.ToPointer("warningcode6"),
        Message:               models.ToPointer("message4"),
        AdditionalProperties:  map[string]interface{}{
            "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
        },
    }

}
```



