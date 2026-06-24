# Course Content File

Source: /#/python/x-redirect/JTI0bSUyRkNvdXJzZUNvbnRlbnRGaWxl

A single file (or link) uploaded inside a course module.

*This model accepts additional fields of type Any.*


# Class Name

`CourseContentFile`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Required | Content type, e.g. 'file' or 'url'. |
| `filename` | `str` | Required | Name of the file (or title of the link). |
| `filepath` | `str` | Optional | Folder path within the module; "/" for the module root. |
| `filesize` | `int` | Optional | File size in bytes (0 for links). |
| `fileurl` | `str` | Required | Moodle pluginfile.php URL for the content. Downloading the bytes requires authentication (a webservice token or the active session); the URL alone is not publicly fetchable. |
| `mimetype` | `str` | Optional | MIME type of the file when applicable. |
| `timemodified` | `int` | Optional | Unix timestamp of the last modification. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |


# Example

```python
import jsonpickle

from nustlmsapi.models.course_content_file import CourseContentFile

course_content_file = CourseContentFile(
    mtype='file',
    filename='Lecture01-Intro.pdf',
    fileurl='https://lms.nust.edu.pk/portal/webservice/pluginfile.php/123456/mod_resource/content/1/Lecture01-Intro.pdf',
    filepath='/',
    filesize=482133,
    mimetype='application/pdf',
    timemodified=1707745200,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```



