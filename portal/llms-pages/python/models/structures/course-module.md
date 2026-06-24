# Course Module

Source: /#/python/x-redirect/JTI0bSUyRkNvdXJzZU1vZHVsZQ

An item on the course page — an activity or resource (file, page, URL, assignment, ...).

*This model accepts additional fields of type Any.*


# Class Name

`CourseModule`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | Course module ID (cmid). |
| `name` | `str` | Required | Display name of the module. |
| `modname` | `str` | Required | Module type, e.g. 'resource' (file), 'folder', 'url', 'page', 'label', 'assign', 'quiz', 'forum'. |
| `modplural` | `str` | Optional | Human-readable plural label for the module type. |
| `instance` | `int` | Optional | Instance ID of the activity within its module type. |
| `description` | `str` | Optional | HTML description/intro for the module, when present. |
| `visible` | `int` | Optional | Whether the module is visible (1) or hidden (0). |
| `uservisible` | `bool` | Optional | Whether the module is visible to the current user. |
| `url` | `str` | Optional | Link to open the activity/resource, when applicable. |
| `modicon` | `str` | Optional | URL of the module's type icon. |
| `contents` | [`List[CourseContentFile]`](/llms-pages/python/models/structures/course-content-file.md) | Optional | Uploaded files/links for this module (present for resource/folder modules). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |


# Example

```python
import jsonpickle

from nustlmsapi.models.course_module import CourseModule

course_module = CourseModule(
    id=987654,
    name='Lecture 01 — Introduction',
    modname='resource',
    modplural='Files',
    instance=45678,
    description='<p>Course introduction and logistics.</p>',
    visible=1,
    uservisible=True,
    url='https://lms.nust.edu.pk/portal/mod/resource/view.php?id=987654',
    modicon='https://lms.nust.edu.pk/portal/theme/image.php/moove/core/1/f/pdf',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```



