# Course Module

Source: /#/ruby/x-redirect/JTI0bSUyRkNvdXJzZU1vZHVsZQ

An item on the course page — an activity or resource (file, page, URL, assignment, ...).

*This model accepts additional fields of type Object.*


# Class Name

`CourseModule`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `Integer` | Required | Course module ID (cmid). |
| `name` | `String` | Required | Display name of the module. |
| `modname` | `String` | Required | Module type, e.g. 'resource' (file), 'folder', 'url', 'page', 'label', 'assign', 'quiz', 'forum'. |
| `modplural` | `String` | Optional | Human-readable plural label for the module type. |
| `instance` | `Integer` | Optional | Instance ID of the activity within its module type. |
| `description` | `String` | Optional | HTML description/intro for the module, when present. |
| `visible` | `Integer` | Optional | Whether the module is visible (1) or hidden (0). |
| `uservisible` | `TrueClass \| FalseClass` | Optional | Whether the module is visible to the current user. |
| `url` | `String` | Optional | Link to open the activity/resource, when applicable. |
| `modicon` | `String` | Optional | URL of the module's type icon. |
| `contents` | [`Array[CourseContentFile]`](/llms-pages/ruby/models/structures/course-content-file.md) | Optional | Uploaded files/links for this module (present for resource/folder modules). |
| `additional_properties` | `Hash[String, Object]` | Optional | - |


# Example

```ruby
course_module = CourseModule.new(
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
  additional_properties: {
    'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
  }
)
```



