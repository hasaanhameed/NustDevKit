# Enrolled Courses Response

Source: /#/python/x-redirect/JTI0bSUyRkVucm9sbGVkQ291cnNlc1Jlc3BvbnNl

Paginated enrolled-courses response.

*This model accepts additional fields of type Any.*


# Class Name

`EnrolledCoursesResponse`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `courses` | [`List[Course]`](/llms-pages/python/models/structures/course.md) | Required | List of enrolled courses for the current page. |
| `nextoffset` | `int` | Required | Offset to pass on the next page request; -1 when no further pages exist. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |


# Example

```python
import jsonpickle

from nustlmsapi.models.course import Course
from nustlmsapi.models.enrolled_courses_response import EnrolledCoursesResponse

enrolled_courses_response = EnrolledCoursesResponse(
    courses=[
        Course(
            id=49900,
            fullname='CS-212 Object Oriented Programming BSCS-13 2K23 ABC',
            shortname='CS-212-Sp\'24 BSCS-13 2K23 ABC',
            idnumber=None,
            summary=None,
            summaryformat=1,
            startdate=1706468400,
            enddate=1717362000,
            visible=True,
            fullnamedisplay='CS-212 Object Oriented Programming BSCS-13 2K23 ABC',
            viewurl='https://lms.nust.edu.pk/portal/course/view.php?id=49900',
            progress=21,
            hasprogress=True,
            isfavourite=False,
            hidden=False,
            showshortname=False,
            coursecategory='2nd Semester (SP-2024)',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    nextoffset=29,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```



