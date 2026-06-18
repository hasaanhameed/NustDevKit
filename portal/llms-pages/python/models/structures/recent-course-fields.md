# Recent Course Fields

Source: /#/python/x-redirect/JTI0bSUyRlJlY2VudENvdXJzZUZpZWxkcw

Additional fields specific to recently accessed courses.

*This model accepts additional fields of type Any.*


# Class Name

`RecentCourseFields`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `timeaccess` | `int` | Required | Unix timestamp of the user's most recent access to this course. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |


# Example

```python
import jsonpickle

from nustlmsapi.models.recent_course_fields import RecentCourseFields

recent_course_fields = RecentCourseFields(
    timeaccess=1781632422,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```



