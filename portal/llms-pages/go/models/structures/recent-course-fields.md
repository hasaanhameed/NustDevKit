# Recent Course Fields

Source: /#/go/x-redirect/JTI0bSUyRlJlY2VudENvdXJzZUZpZWxkcw

Additional fields specific to recently accessed courses.

*This model accepts additional fields of type interface{}.*


# Class Name

`RecentCourseFields`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Timeaccess` | `int` | Required | Unix timestamp of the user's most recent access to this course. |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
package main

import (
    "nustLmsApi/models"
)

func main() {
    recentCourseFields := models.RecentCourseFields{
        Timeaccess:            1781632422,
        AdditionalProperties:  map[string]interface{}{
            "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
        },
    }

}
```



