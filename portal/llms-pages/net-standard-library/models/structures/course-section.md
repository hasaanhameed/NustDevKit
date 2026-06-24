# Course Section

Source: /#/net-standard-library/x-redirect/JTI0bSUyRkNvdXJzZVNlY3Rpb24

A section (week/topic) of the course, containing its modules.

*This model accepts additional fields of type object.*


# Class Name

`CourseSection`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Id` | `int` | Required | Section ID. |
| `Name` | `string` | Required | Section title (e.g. a week or topic name). |
| `Section` | `int` | Required | Zero-based section number within the course. |
| `Visible` | `int?` | Optional | Whether the section is visible (1) or hidden (0). |
| `Summary` | `string` | Optional | HTML summary shown at the top of the section. |
| `Summaryformat` | `int?` | Optional | Moodle text format of the summary (1 = HTML). |
| `Uservisible` | `bool?` | Optional | Whether the section is visible to the current user. |
| `Modules` | [`List<CourseModule>`](/llms-pages/net-standard-library/models/structures/course-module.md) | Required | The activities and resources in this section. |
| `AdditionalProperties` | `object this[string key]` | Optional | - |


# Example

```csharp
using NustLmsApi.Standard.Models;
using NustLmsApi.Standard.Utilities;
using System.Collections.Generic;

CourseSection courseSection = new CourseSection
{
    Id = 33445,
    Name = "Week 1",
    Section = 1,
    Modules = new List<CourseModule>
    {
        new CourseModule
        {
            Id = 987654,
            Name = "Lecture 01 — Introduction",
            Modname = "resource",
            Modplural = "Files",
            Instance = 45678,
            Description = "<p>Course introduction and logistics.</p>",
            Visible = 1,
            Uservisible = true,
            Url = "https://lms.nust.edu.pk/portal/mod/resource/view.php?id=987654",
            Modicon = "https://lms.nust.edu.pk/portal/theme/image.php/moove/core/1/f/pdf",
            ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
        },
    },
    Visible = 1,
    Summary = "<p>Introduction and course overview.</p>",
    Summaryformat = 1,
    Uservisible = true,
    ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
};
```



