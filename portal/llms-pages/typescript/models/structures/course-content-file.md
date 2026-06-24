# Course Content File

Source: /#/typescript/x-redirect/JTI0bSUyRkNvdXJzZUNvbnRlbnRGaWxl

A single file (or link) uploaded inside a course module.

*This model accepts additional fields of type unknown.*


# Interface Name

`CourseContentFile`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `type` | `string` | Required | Content type, e.g. 'file' or 'url'. |
| `filename` | `string` | Required | Name of the file (or title of the link). |
| `filepath` | `string \| null \| undefined` | Optional | Folder path within the module; "/" for the module root. |
| `filesize` | `number \| undefined` | Optional | File size in bytes (0 for links). |
| `fileurl` | `string` | Required | Moodle pluginfile.php URL for the content. Downloading the bytes requires authentication (a webservice token or the active session); the URL alone is not publicly fetchable. |
| `mimetype` | `string \| null \| undefined` | Optional | MIME type of the file when applicable. |
| `timemodified` | `number \| undefined` | Optional | Unix timestamp of the last modification. |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
import { CourseContentFile } from 'nust-lms-apilib';

const courseContentFile: CourseContentFile = {
  type: 'file',
  filename: 'Lecture01-Intro.pdf',
  fileurl: 'https://lms.nust.edu.pk/portal/webservice/pluginfile.php/123456/mod_resource/content/1/Lecture01-Intro.pdf',
  filepath: '/',
  filesize: 482133,
  mimetype: 'application/pdf',
  timemodified: 1707745200,
  additionalProperties: {
    'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
  },
};
```



