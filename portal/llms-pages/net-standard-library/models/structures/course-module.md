# Course Module

Source: /#/net-standard-library/x-redirect/JTI0bSUyRkNvdXJzZU1vZHVsZQ

An item on the course page — an activity or resource (file, page, URL, assignment, ...).

*This model accepts additional fields of type object.*


# Class Name

`CourseModule`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Id` | `int` | Required | Course module ID (cmid). |
| `Name` | `string` | Required | Display name of the module. |
| `Modname` | `string` | Required | Module type, e.g. 'resource' (file), 'folder', 'url', 'page', 'label', 'assign', 'quiz', 'forum'. |
| `Modplural` | `string` | Optional | Human-readable plural label for the module type. |
| `Instance` | `int?` | Optional | Instance ID of the activity within its module type. |
| `Description` | `string` | Optional | HTML description/intro for the module, when present. |
| `Visible` | `int?` | Optional | Whether the module is visible (1) or hidden (0). |
| `Uservisible` | `bool?` | Optional | Whether the module is visible to the current user. |
| `Url` | `string` | Optional | Link to open the activity/resource, when applicable. |
| `Modicon` | `string` | Optional | URL of the module's type icon. |
| `Contents` | [`List<CourseContentFile>`](/llms-pages/net-standard-library/models/structures/course-content-file.md) | Optional | Uploaded files/links for this module (present for resource/folder modules). |
| `AdditionalProperties` | `object this[string key]` | Optional | - |


# Example

```csharp
using NustLmsApi.Standard.Models;
using NustLmsApi.Standard.Utilities;

CourseModule courseModule = new CourseModule
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
};
```



