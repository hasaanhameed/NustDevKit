# Get Recent Courses Request

Source: /#/python/x-redirect/JTI0bSUyRkdldFJlY2VudENvdXJzZXNSZXF1ZXN0

Request parameters for retrieving recently accessed courses.

*This model accepts additional fields of type Any.*


# Class Name

`GetRecentCoursesRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Required | Maximum number of courses to return.<br><br>**Default**: `10` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |


# Example

```python
import jsonpickle

from nustlmsapi.models.get_recent_courses_request import GetRecentCoursesRequest

get_recent_courses_request = GetRecentCoursesRequest(
    limit=10,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```



