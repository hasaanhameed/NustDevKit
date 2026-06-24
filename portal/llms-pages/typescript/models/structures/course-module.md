# Course Module

Source: /#/typescript/x-redirect/JTI0bSUyRkNvdXJzZU1vZHVsZQ

An item on the course page — an activity or resource (file, page, URL, assignment, ...).

*This model accepts additional fields of type unknown.*


# Interface Name

`CourseModule`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `number` | Required | Course module ID (cmid). |
| `name` | `string` | Required | Display name of the module. |
| `modname` | `string` | Required | Module type, e.g. 'resource' (file), 'folder', 'url', 'page', 'label', 'assign', 'quiz', 'forum'. |
| `modplural` | `string \| undefined` | Optional | Human-readable plural label for the module type. |
| `instance` | `number \| undefined` | Optional | Instance ID of the activity within its module type. |
| `description` | `string \| null \| undefined` | Optional | HTML description/intro for the module, when present. |
| `visible` | `number \| undefined` | Optional | Whether the module is visible (1) or hidden (0). |
| `uservisible` | `boolean \| undefined` | Optional | Whether the module is visible to the current user. |
| `url` | `string \| null \| undefined` | Optional | Link to open the activity/resource, when applicable. |
| `modicon` | `string \| null \| undefined` | Optional | URL of the module's type icon. |
| `contents` | [`CourseContentFile[] \| undefined`](/llms-pages/typescript/models/structures/course-content-file.md) | Optional | Uploaded files/links for this module (present for resource/folder modules). |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
import { CourseModule } from 'nust-lms-apilib';

const courseModule: CourseModule = {
  id: 987654,
  name: 'Lecture 01 — Introduction',
  modname: 'resource',
  modplural: 'Files',
  instance: 45678,
  description: '<p>Course introduction and logistics.</p>',
  visible: 1,
  uservisible: true,
  url: 'https://lms.nust.edu.pk/portal/mod/resource/view.php?id=987654',
  modicon: 'https://lms.nust.edu.pk/portal/theme/image.php/moove/core/1/f/pdf',
  additionalProperties: {
    'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
  },
};
```



