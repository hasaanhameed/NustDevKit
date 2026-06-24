# Course Content File

Source: /#/go/x-redirect/JTI0bSUyRkNvdXJzZUNvbnRlbnRGaWxl

A single file (or link) uploaded inside a course module.

*This model accepts additional fields of type interface{}.*


# Class Name

`CourseContentFile`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Type` | `string` | Required | Content type, e.g. 'file' or 'url'. |
| `Filename` | `string` | Required | Name of the file (or title of the link). |
| `Filepath` | `models.Optional[string]` | Optional | Folder path within the module; "/" for the module root. |
| `Filesize` | `*int` | Optional | File size in bytes (0 for links). |
| `Fileurl` | `string` | Required | Moodle pluginfile.php URL for the content. Downloading the bytes requires authentication (a webservice token or the active session); the URL alone is not publicly fetchable. |
| `Mimetype` | `models.Optional[string]` | Optional | MIME type of the file when applicable. |
| `Timemodified` | `*int` | Optional | Unix timestamp of the last modification. |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
package main

import (
    "nustLmsApi/models"
)

func main() {
    courseContentFile := models.CourseContentFile{
        Type:                  "file",
        Filename:              "Lecture01-Intro.pdf",
        Filepath:              models.NewOptional(models.ToPointer("/")),
        Filesize:              models.ToPointer(482133),
        Fileurl:               "https://lms.nust.edu.pk/portal/webservice/pluginfile.php/123456/mod_resource/content/1/Lecture01-Intro.pdf",
        Mimetype:              models.NewOptional(models.ToPointer("application/pdf")),
        Timemodified:          models.ToPointer(1707745200),
        AdditionalProperties:  map[string]interface{}{
            "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
        },
    }

}
```



