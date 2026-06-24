# Course Content File

Source: /#/http/x-redirect/JTI0bSUyRkNvdXJzZUNvbnRlbnRGaWxl

A single file (or link) uploaded inside a course module.

*This model accepts additional fields of type Object.*


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `type` | `String` | Required | Content type, e.g. 'file' or 'url'. |
| `filename` | `String` | Required | Name of the file (or title of the link). |
| `filepath` | `String` | Optional | Folder path within the module; "/" for the module root. |
| `filesize` | `Number` | Optional | File size in bytes (0 for links). |
| `fileurl` | `String` | Required | Moodle pluginfile.php URL for the content. Downloading the bytes requires authentication (a webservice token or the active session); the URL alone is not publicly fetchable. |
| `mimetype` | `String` | Optional | MIME type of the file when applicable. |
| `timemodified` | `Number` | Optional | Unix timestamp of the last modification. |
| `additionalProperties` | `Object` | Optional | - |


# Example (as JSON)

```json
{
  "type": "file",
  "filename": "Lecture01-Intro.pdf",
  "filepath": "/",
  "filesize": 482133,
  "fileurl": "https://lms.nust.edu.pk/portal/webservice/pluginfile.php/123456/mod_resource/content/1/Lecture01-Intro.pdf",
  "mimetype": "application/pdf",
  "timemodified": 1707745200,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```



