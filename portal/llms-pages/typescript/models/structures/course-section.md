# Course Section

Source: /#/typescript/x-redirect/JTI0bSUyRkNvdXJzZVNlY3Rpb24

A section (week/topic) of the course, containing its modules.

*This model accepts additional fields of type unknown.*


# Interface Name

`CourseSection`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `number` | Required | Section ID. |
| `name` | `string` | Required | Section title (e.g. a week or topic name). |
| `section` | `number` | Required | Zero-based section number within the course. |
| `visible` | `number \| undefined` | Optional | Whether the section is visible (1) or hidden (0). |
| `summary` | `string \| null \| undefined` | Optional | HTML summary shown at the top of the section. |
| `summaryformat` | `number \| undefined` | Optional | Moodle text format of the summary (1 = HTML). |
| `uservisible` | `boolean \| undefined` | Optional | Whether the section is visible to the current user. |
| `modules` | [`CourseModule[]`](/llms-pages/typescript/models/structures/course-module.md) | Required | The activities and resources in this section. |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
import { CourseSection } from 'nust-lms-apilib';

const courseSection: CourseSection = {
  id: 33445,
  name: 'Week 1',
  section: 1,
  modules: [
    {
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
    }
  ],
  visible: 1,
  summary: '<p>Introduction and course overview.</p>',
  summaryformat: 1,
  uservisible: true,
  additionalProperties: {
    'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
  },
};
```



