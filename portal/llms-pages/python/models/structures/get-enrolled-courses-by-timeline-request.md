# Get Enrolled Courses by Timeline Request

Source: /#/python/x-redirect/JTI0bSUyRkdldEVucm9sbGVkQ291cnNlc0J5VGltZWxpbmVSZXF1ZXN0

Request parameters for retrieving enrolled courses filtered by timeline classification.

*This model accepts additional fields of type Any.*


# Class Name

`GetEnrolledCoursesByTimelineRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `offset` | `int` | Required | Zero-based pagination offset.<br><br>**Default**: `0` |
| `limit` | `int` | Required | Maximum number of courses to return.<br><br>**Default**: `50` |
| `classification` | [`CourseTimelineClassification`](/llms-pages/python/models/enumerations/course-timeline-classification.md) | Required | Timeline classification filter for enrolled courses. |
| `sort` | [`CourseTimelineSortField`](/llms-pages/python/models/enumerations/course-timeline-sort-field.md) | Required | Field used to sort enrolled course results. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |


# Example

```python
import jsonpickle

from nustlmsapi.models.course_timeline_classification import CourseTimelineClassification
from nustlmsapi.models.course_timeline_sort_field import CourseTimelineSortField
from nustlmsapi.models.get_enrolled_courses_by_timeline_request import GetEnrolledCoursesByTimelineRequest

get_enrolled_courses_by_timeline_request = GetEnrolledCoursesByTimelineRequest(
    offset=0,
    limit=50,
    classification=CourseTimelineClassification.ALLINCLUDINGHIDDEN,
    sort=CourseTimelineSortField.IDNUMBER,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```



