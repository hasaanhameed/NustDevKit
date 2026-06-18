# Enrolled Courses Response

Source: /#/go/x-redirect/JTI0bSUyRkVucm9sbGVkQ291cnNlc1Jlc3BvbnNl

Paginated enrolled-courses response.

*This model accepts additional fields of type interface{}.*


# Class Name

`EnrolledCoursesResponse`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Courses` | [`[]models.Course`](/llms-pages/go/models/structures/course.md) | Required | List of enrolled courses for the current page. |
| `Nextoffset` | `int` | Required | Offset to pass on the next page request; -1 when no further pages exist. |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
package main

import (
    "nustLmsApi/models"
)

func main() {
    enrolledCoursesResponse := models.EnrolledCoursesResponse{
        Courses:               []models.Course{
            models.Course{
                Id:                    49900,
                Fullname:              "CS-212 Object Oriented Programming BSCS-13 2K23 ABC",
                Shortname:             "CS-212-Sp'24 BSCS-13 2K23 ABC",
                Idnumber:              "",
                Summary:               "",
                Summaryformat:         1,
                Startdate:             1706468400,
                Enddate:               1717362000,
                Visible:               true,
                Fullnamedisplay:       "CS-212 Object Oriented Programming BSCS-13 2K23 ABC",
                Viewurl:               "https://lms.nust.edu.pk/portal/course/view.php?id=49900",
                Progress:              21,
                Hasprogress:           true,
                Isfavourite:           false,
                Hidden:                false,
                Showshortname:         false,
                Coursecategory:        "2nd Semester (SP-2024)",
                AdditionalProperties:  map[string]interface{}{
                    "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
                },
            },
        },
        Nextoffset:            29,
        AdditionalProperties:  map[string]interface{}{
            "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
        },
    }

}
```



