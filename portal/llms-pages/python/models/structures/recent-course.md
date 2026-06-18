# Recent Course

Source: /#/python/x-redirect/JTI0bSUyRlJlY2VudENvdXJzZQ

A recently accessed course, extending Course with the last-access timestamp.

*This model accepts additional fields of type Any.*


# Class Name

`RecentCourse`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | Unique course identifier. |
| `fullname` | `str` | Required | Full display name of the course. |
| `shortname` | `str` | Required | Short course code or abbreviated name. |
| `idnumber` | `str` | Required | Institution-assigned course ID number; empty string if not set. |
| `summary` | `str` | Required | HTML summary of the course. |
| `summaryformat` | `int` | Required | Format of the summary field (1 = HTML). |
| `startdate` | `int` | Required | Course start date as Unix timestamp. |
| `enddate` | `int` | Required | Course end date as Unix timestamp. 0 means no end date. |
| `visible` | `bool` | Required | Whether the course is visible to enrolled students. |
| `fullnamedisplay` | `str` | Required | Display name of the course (may differ from fullname for context). |
| `viewurl` | `str` | Required | URL to the course page on the LMS portal. |
| `progress` | `int` | Required | Student's completion progress as a percentage.<br><br>**Constraints**: `>= 0`, `<= 100` |
| `hasprogress` | `bool` | Required | Whether completion tracking is enabled for this course. |
| `isfavourite` | `bool` | Required | Whether the user has marked this course as a favourite. |
| `hidden` | `bool` | Required | Whether the user has hidden this course from their dashboard. |
| `showshortname` | `bool` | Required | Whether the short name is displayed alongside the full name. |
| `coursecategory` | `str` | Required | Name of the category this course belongs to. |
| `timeaccess` | `int` | Required | Unix timestamp of the user's most recent access to this course. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |


# Example

```python
import jsonpickle

from nustlmsapi.models.recent_course import RecentCourse

recent_course = RecentCourse(
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
    timeaccess=1781632422,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```



