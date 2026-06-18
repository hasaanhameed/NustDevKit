# Recent Course

Source: /#/go/x-redirect/JTI0bSUyRlJlY2VudENvdXJzZQ

A recently accessed course, extending Course with the last-access timestamp.

*This model accepts additional fields of type interface{}.*


# Class Name

`RecentCourse`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Id` | `int` | Required | Unique course identifier. |
| `Fullname` | `string` | Required | Full display name of the course. |
| `Shortname` | `string` | Required | Short course code or abbreviated name. |
| `Idnumber` | `string` | Required | Institution-assigned course ID number; empty string if not set. |
| `Summary` | `string` | Required | HTML summary of the course. |
| `Summaryformat` | `int` | Required | Format of the summary field (1 = HTML). |
| `Startdate` | `int` | Required | Course start date as Unix timestamp. |
| `Enddate` | `int` | Required | Course end date as Unix timestamp. 0 means no end date. |
| `Visible` | `bool` | Required | Whether the course is visible to enrolled students. |
| `Fullnamedisplay` | `string` | Required | Display name of the course (may differ from fullname for context). |
| `Viewurl` | `string` | Required | URL to the course page on the LMS portal. |
| `Progress` | `int` | Required | Student's completion progress as a percentage.<br><br>**Constraints**: `>= 0`, `<= 100` |
| `Hasprogress` | `bool` | Required | Whether completion tracking is enabled for this course. |
| `Isfavourite` | `bool` | Required | Whether the user has marked this course as a favourite. |
| `Hidden` | `bool` | Required | Whether the user has hidden this course from their dashboard. |
| `Showshortname` | `bool` | Required | Whether the short name is displayed alongside the full name. |
| `Coursecategory` | `string` | Required | Name of the category this course belongs to. |
| `Timeaccess` | `int` | Required | Unix timestamp of the user's most recent access to this course. |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
package main

import (
    "nustLmsApi/models"
)

func main() {
    recentCourse := models.RecentCourse{
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
        Timeaccess:            1781632422,
        AdditionalProperties:  map[string]interface{}{
            "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
        },
    }

}
```



