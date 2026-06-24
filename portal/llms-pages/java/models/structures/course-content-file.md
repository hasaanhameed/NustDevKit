# Course Content File

Source: /#/java/x-redirect/JTI0bSUyRkNvdXJzZUNvbnRlbnRGaWxl

A single file (or link) uploaded inside a course module.

*This model accepts additional fields of type Object.*


# Class Name

`CourseContentFile`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Type` | `String` | Required | Content type, e.g. 'file' or 'url'. | String getType() | setType(String type) |
| `Filename` | `String` | Required | Name of the file (or title of the link). | String getFilename() | setFilename(String filename) |
| `Filepath` | `String` | Optional | Folder path within the module; "/" for the module root. | String getFilepath() | setFilepath(String filepath) |
| `Filesize` | `Integer` | Optional | File size in bytes (0 for links). | Integer getFilesize() | setFilesize(Integer filesize) |
| `Fileurl` | `String` | Required | Moodle pluginfile.php URL for the content. Downloading the bytes requires authentication (a webservice token or the active session); the URL alone is not publicly fetchable. | String getFileurl() | setFileurl(String fileurl) |
| `Mimetype` | `String` | Optional | MIME type of the file when applicable. | String getMimetype() | setMimetype(String mimetype) |
| `Timemodified` | `Integer` | Optional | Unix timestamp of the last modification. | Integer getTimemodified() | setTimemodified(Integer timemodified) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import java.io.IOException;
import m18000.m0.m0.m127.ApiHelper;
import m18000.m0.m0.m127.models.CourseContentFile;

CourseContentFile courseContentFile = new CourseContentFile.Builder(
    "file",
    "Lecture01-Intro.pdf",
    "https://lms.nust.edu.pk/portal/webservice/pluginfile.php/123456/mod_resource/content/1/Lecture01-Intro.pdf"
)
.filepath("/")
.filesize(482133)
.mimetype("application/pdf")
.timemodified(1707745200)
.additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
.build();
```



