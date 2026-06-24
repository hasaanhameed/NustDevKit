# Course Section

Source: /#/python/x-redirect/JTI0bSUyRkNvdXJzZVNlY3Rpb24

A section (week/topic) of the course, containing its modules.

*This model accepts additional fields of type Any.*


# Class Name

`CourseSection`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | Section ID. |
| `name` | `str` | Required | Section title (e.g. a week or topic name). |
| `section` | `int` | Required | Zero-based section number within the course. |
| `visible` | `int` | Optional | Whether the section is visible (1) or hidden (0). |
| `summary` | `str` | Optional | HTML summary shown at the top of the section. |
| `summaryformat` | `int` | Optional | Moodle text format of the summary (1 = HTML). |
| `uservisible` | `bool` | Optional | Whether the section is visible to the current user. |
| `modules` | [`List[CourseModule]`](/llms-pages/python/models/structures/course-module.md) | Required | The activities and resources in this section. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |


# Example

```python
import jsonpickle

from nustlmsapi.models.course_module import CourseModule
from nustlmsapi.models.course_section import CourseSection

course_section = CourseSection(
    id=33445,
    name='Week 1',
    section=1,
    modules=[
        CourseModule(
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
    ],
    visible=1,
    summary='<p>Introduction and course overview.</p>',
    summaryformat=1,
    uservisible=True,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```



