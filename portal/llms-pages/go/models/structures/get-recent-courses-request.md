# Get Recent Courses Request

Source: /#/go/x-redirect/JTI0bSUyRkdldFJlY2VudENvdXJzZXNSZXF1ZXN0

Request parameters for retrieving recently accessed courses.

*This model accepts additional fields of type interface{}.*


# Class Name

`GetRecentCoursesRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Limit` | `int` | Required | Maximum number of courses to return.<br><br>**Default**: `10` |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
package main

import (
    "nustLmsApi/models"
)

func main() {
    getRecentCoursesRequest := models.GetRecentCoursesRequest{
        Limit:                 10,
        AdditionalProperties:  map[string]interface{}{
            "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
        },
    }

}
```



