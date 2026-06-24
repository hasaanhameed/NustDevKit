# Course Content File

Source: /#/net-standard-library/x-redirect/JTI0bSUyRkNvdXJzZUNvbnRlbnRGaWxl

A single file (or link) uploaded inside a course module.

*This model accepts additional fields of type object.*


# Class Name

`CourseContentFile`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Type` | `string` | Required | Content type, e.g. 'file' or 'url'. |
| `Filename` | `string` | Required | Name of the file (or title of the link). |
| `Filepath` | `string` | Optional | Folder path within the module; "/" for the module root. |
| `Filesize` | `int?` | Optional | File size in bytes (0 for links). |
| `Fileurl` | `string` | Required | Moodle pluginfile.php URL for the content. Downloading the bytes requires authentication (a webservice token or the active session); the URL alone is not publicly fetchable. |
| `Mimetype` | `string` | Optional | MIME type of the file when applicable. |
| `Timemodified` | `int?` | Optional | Unix timestamp of the last modification. |
| `AdditionalProperties` | `object this[string key]` | Optional | - |


# Example

```csharp
using NustLmsApi.Standard.Models;
using NustLmsApi.Standard.Utilities;

CourseContentFile courseContentFile = new CourseContentFile
{
    Type = "file",
    Filename = "Lecture01-Intro.pdf",
    Fileurl = "https://lms.nust.edu.pk/portal/webservice/pluginfile.php/123456/mod_resource/content/1/Lecture01-Intro.pdf",
    Filepath = "/",
    Filesize = 482133,
    Mimetype = "application/pdf",
    Timemodified = 1707745200,
    ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
};
```



