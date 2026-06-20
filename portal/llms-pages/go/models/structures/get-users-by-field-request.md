# Get Users by Field Request

Source: /#/go/x-redirect/JTI0bSUyRkdldFVzZXJzQnlGaWVsZFJlcXVlc3Q

Request parameters for retrieving user profiles by a profile field value.

*This model accepts additional fields of type interface{}.*


# Class Name

`GetUsersByFieldRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Field` | [`models.UserProfileField`](/llms-pages/go/models/enumerations/user-profile-field.md) | Required | User profile field to match against when searching for users. |
| `Values` | `[]string` | Required | List of field values to look up. All values must be provided as strings even when the field is numeric (e.g., "123456" for an integer ID). |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
package main

import (
    "nustLmsApi/models"
)

func main() {
    getUsersByFieldRequest := models.GetUsersByFieldRequest{
        Field:                 models.UserProfileField_Id,
        Values:                []string{
            "123456",
        },
        AdditionalProperties:  map[string]interface{}{
            "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
        },
    }

}
```



