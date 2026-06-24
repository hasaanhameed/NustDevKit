# Course Content File

Source: /#/php/x-redirect/JTI0bSUyRkNvdXJzZUNvbnRlbnRGaWxl

A single file (or link) uploaded inside a course module.

*This model accepts additional fields of type array.*


# Class Name

`CourseContentFile`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `type` | `string` | Required | Content type, e.g. 'file' or 'url'. | getType(): string | setType(string type): void |
| `filename` | `string` | Required | Name of the file (or title of the link). | getFilename(): string | setFilename(string filename): void |
| `filepath` | `?string` | Optional | Folder path within the module; "/" for the module root. | getFilepath(): ?string | setFilepath(?string filepath): void |
| `filesize` | `?int` | Optional | File size in bytes (0 for links). | getFilesize(): ?int | setFilesize(?int filesize): void |
| `fileurl` | `string` | Required | Moodle pluginfile.php URL for the content. Downloading the bytes requires authentication (a webservice token or the active session); the URL alone is not publicly fetchable. | getFileurl(): string | setFileurl(string fileurl): void |
| `mimetype` | `?string` | Optional | MIME type of the file when applicable. | getMimetype(): ?string | setMimetype(?string mimetype): void |
| `timemodified` | `?int` | Optional | Unix timestamp of the last modification. | getTimemodified(): ?int | setTimemodified(?int timemodified): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |


# Example

```php
use NustLmsApiLib\Models\Builders\CourseContentFileBuilder;
use NustLmsApiLib\ApiHelper;

$courseContentFile = CourseContentFileBuilder::init(
    'file',
    'Lecture01-Intro.pdf',
    'https://lms.nust.edu.pk/portal/webservice/pluginfile.php/123456/mod_resource/content/1/Lecture01-Intro.pdf'
)
    ->filepath('/')
    ->filesize(482133)
    ->mimetype('application/pdf')
    ->timemodified(1707745200)
    ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
    ->build();
```



