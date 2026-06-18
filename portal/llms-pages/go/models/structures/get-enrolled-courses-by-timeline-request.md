# Get Enrolled Courses by Timeline Request

Source: /#/go/x-redirect/JTI0bSUyRkdldEVucm9sbGVkQ291cnNlc0J5VGltZWxpbmVSZXF1ZXN0

Request parameters for retrieving enrolled courses filtered by timeline classification.

*This model accepts additional fields of type interface{}.*


# Class Name

`GetEnrolledCoursesByTimelineRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Offset` | `int` | Required | Zero-based pagination offset.<br><br>**Default**: `0` |
| `Limit` | `int` | Required | Maximum number of courses to return.<br><br>**Default**: `50` |
| `Classification` | [`models.CourseTimelineClassification`](/llms-pages/go/models/enumerations/course-timeline-classification.md) | Required | Timeline classification filter for enrolled courses. |
| `Sort` | [`models.CourseTimelineSortField`](/llms-pages/go/models/enumerations/course-timeline-sort-field.md) | Required | Field used to sort enrolled course results. |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
package main

import (
    "nustLmsApi/models"
)

func main() {
    getEnrolledCoursesByTimelineRequest := models.GetEnrolledCoursesByTimelineRequest{
        Offset:                0,
        Limit:                 50,
        Classification:        models.CourseTimelineClassification_Future,
        Sort:                  models.CourseTimelineSortField_Idnumber,
        AdditionalProperties:  map[string]interface{}{
            "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
        },
    }

}
```



