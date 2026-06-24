# Course Content File

Source: /#/ruby/x-redirect/JTI0bSUyRkNvdXJzZUNvbnRlbnRGaWxl

A single file (or link) uploaded inside a course module.

*This model accepts additional fields of type Object.*


# Class Name

`CourseContentFile`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `type` | `String` | Required | Content type, e.g. 'file' or 'url'. |
| `filename` | `String` | Required | Name of the file (or title of the link). |
| `filepath` | `String` | Optional | Folder path within the module; "/" for the module root. |
| `filesize` | `Integer` | Optional | File size in bytes (0 for links). |
| `fileurl` | `String` | Required | Moodle pluginfile.php URL for the content. Downloading the bytes requires authentication (a webservice token or the active session); the URL alone is not publicly fetchable. |
| `mimetype` | `String` | Optional | MIME type of the file when applicable. |
| `timemodified` | `Integer` | Optional | Unix timestamp of the last modification. |
| `additional_properties` | `Hash[String, Object]` | Optional | - |


# Example

```ruby
course_content_file = CourseContentFile.new(
  type: 'file',
  filename: 'Lecture01-Intro.pdf',
  fileurl: 'https://lms.nust.edu.pk/portal/webservice/pluginfile.php/123456/mod_resource/content/1/Lecture01-Intro.pdf',
  filepath: '/',
  filesize: 482133,
  mimetype: 'application/pdf',
  timemodified: 1707745200,
  additional_properties: {
    'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
  }
)
```



