# Course Module

Source: /#/go/x-redirect/JTI0bSUyRkNvdXJzZU1vZHVsZQ

An item on the course page — an activity or resource (file, page, URL, assignment, ...).

*This model accepts additional fields of type interface{}.*


# Class Name

`CourseModule`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Id` | `int` | Required | Course module ID (cmid). |
| `Name` | `string` | Required | Display name of the module. |
| `Modname` | `string` | Required | Module type, e.g. 'resource' (file), 'folder', 'url', 'page', 'label', 'assign', 'quiz', 'forum'. |
| `Modplural` | `*string` | Optional | Human-readable plural label for the module type. |
| `Instance` | `*int` | Optional | Instance ID of the activity within its module type. |
| `Description` | `models.Optional[string]` | Optional | HTML description/intro for the module, when present. |
| `Visible` | `*int` | Optional | Whether the module is visible (1) or hidden (0). |
| `Uservisible` | `*bool` | Optional | Whether the module is visible to the current user. |
| `Url` | `models.Optional[string]` | Optional | Link to open the activity/resource, when applicable. |
| `Modicon` | `models.Optional[string]` | Optional | URL of the module's type icon. |
| `Contents` | [`[]models.CourseContentFile`](/llms-pages/go/models/structures/course-content-file.md) | Optional | Uploaded files/links for this module (present for resource/folder modules). |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
package main

import (
    "nustLmsApi/models"
)

func main() {
    courseModule := models.CourseModule{
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
    }

}
```



