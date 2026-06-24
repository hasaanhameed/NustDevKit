# Course Section

Source: /#/http/x-redirect/JTI0bSUyRkNvdXJzZVNlY3Rpb24

A section (week/topic) of the course, containing its modules.

*This model accepts additional fields of type Object.*


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `Number` | Required | Section ID. |
| `name` | `String` | Required | Section title (e.g. a week or topic name). |
| `section` | `Number` | Required | Zero-based section number within the course. |
| `visible` | `Number` | Optional | Whether the section is visible (1) or hidden (0). |
| `summary` | `String` | Optional | HTML summary shown at the top of the section. |
| `summaryformat` | `Number` | Optional | Moodle text format of the summary (1 = HTML). |
| `uservisible` | `Boolean` | Optional | Whether the section is visible to the current user. |
| `modules` | [`array<Course Module>`](/llms-pages/http/models/structures/course-module.md) | Required | The activities and resources in this section. |
| `additionalProperties` | `Object` | Optional | - |


# Example (as JSON)

```json
{
  "id": 33445,
  "name": "Week 1",
  "section": 1,
  "visible": 1,
  "summary": "<p>Introduction and course overview.</p>",
  "summaryformat": 1,
  "uservisible": true,
  "modules": [
    {
      "id": 987654,
      "name": "Lecture 01 — Introduction",
      "modname": "resource",
      "modplural": "Files",
      "instance": 45678,
      "description": "<p>Course introduction and logistics.</p>",
      "visible": 1,
      "uservisible": true,
      "url": "https://lms.nust.edu.pk/portal/mod/resource/view.php?id=987654",
      "modicon": "https://lms.nust.edu.pk/portal/theme/image.php/moove/core/1/f/pdf",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```



