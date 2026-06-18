# Custom Field

Source: /#/go/x-redirect/JTI0bSUyRkN1c3RvbUZpZWxk

A custom profile field value attached to a user.

*This model accepts additional fields of type interface{}.*


# Class Name

`CustomField`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Type` | `string` | Required | Data type of the custom field (e.g., 'text', 'select'). |
| `Value` | `string` | Required | Value stored in the custom field. |
| `Name` | `string` | Required | Display label of the custom field. |
| `Shortname` | `string` | Required | Machine-readable shortname identifier for the custom field. |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
package main

import (
    "nustLmsApi/models"
)

func main() {
    customField := models.CustomField{
        Type:                  "text",
        Value:                 "SEECS",
        Name:                  "Institute",
        Shortname:             "institution",
        AdditionalProperties:  map[string]interface{}{
            "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
        },
    }

}
```



