# Course Section

Source: /#/go/x-redirect/JTI0bSUyRkNvdXJzZVNlY3Rpb24

A section (week/topic) of the course, containing its modules.

*This model accepts additional fields of type interface{}.*


# Class Name

`CourseSection`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Id` | `int` | Required | Section ID. |
| `Name` | `string` | Required | Section title (e.g. a week or topic name). |
| `Section` | `int` | Required | Zero-based section number within the course. |
| `Visible` | `*int` | Optional | Whether the section is visible (1) or hidden (0). |
| `Summary` | `models.Optional[string]` | Optional | HTML summary shown at the top of the section. |
| `Summaryformat` | `*int` | Optional | Moodle text format of the summary (1 = HTML). |
| `Uservisible` | `*bool` | Optional | Whether the section is visible to the current user. |
| `Modules` | [`[]models.CourseModule`](/llms-pages/go/models/structures/course-module.md) | Required | The activities and resources in this section. |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
package main

import (
    "nustLmsApi/models"
)

func main() {
    courseSection := models.CourseSection{
        Id:                    33445,
        Name:                  "Week 1",
        Section:               1,
        Visible:               models.ToPointer(1),
        Summary:               models.NewOptional(models.ToPointer("<p>Introduction and course overview.</p>")),
        Summaryformat:         models.ToPointer(1),
        Uservisible:           models.ToPointer(true),
        Modules:               []models.CourseModule{
            models.CourseModule{
                Id:                    987654,
                Name:                  "Lecture 01 — Introduction",
                Modname:               "resource",
                Modplural:             models.ToPointer("Files"),
                Instance:              models.ToPointer(45678),
                Description:           models.NewOptional(models.ToPointer("<p>Course introduction and logistics.</p>")),
                Visible:               models.ToPointer(1),
                Uservisible:           models.ToPointer(true),
                Url:                   models.NewOptional(models.ToPointer("https://lms.nust.edu.pk/portal/mod/resource/view.php?id=987654")),
                Modicon:               models.NewOptional(models.ToPointer("https://lms.nust.edu.pk/portal/theme/image.php/moove/core/1/f/pdf")),
                AdditionalProperties:  map[string]interface{}{
                    "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
                },
            },
        },
        AdditionalProperties:  map[string]interface{}{
            "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
        },
    }

}
```



