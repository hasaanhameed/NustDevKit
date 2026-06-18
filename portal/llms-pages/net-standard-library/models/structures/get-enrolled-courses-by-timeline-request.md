# Get Enrolled Courses by Timeline Request

Source: /#/net-standard-library/x-redirect/JTI0bSUyRkdldEVucm9sbGVkQ291cnNlc0J5VGltZWxpbmVSZXF1ZXN0

Request parameters for retrieving enrolled courses filtered by timeline classification.

*This model accepts additional fields of type object.*


# Class Name

`GetEnrolledCoursesByTimelineRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Offset` | `int` | Required | Zero-based pagination offset.<br><br>**Default**: `0` |
| `Limit` | `int` | Required | Maximum number of courses to return.<br><br>**Default**: `50` |
| `Classification` | [`CourseTimelineClassification`](/llms-pages/net-standard-library/models/enumerations/course-timeline-classification.md) | Required | Timeline classification filter for enrolled courses. |
| `Sort` | [`CourseTimelineSortField`](/llms-pages/net-standard-library/models/enumerations/course-timeline-sort-field.md) | Required | Field used to sort enrolled course results. |
| `AdditionalProperties` | `object this[string key]` | Optional | - |


# Example

```csharp
using NustLmsApi.Standard.Models;
using NustLmsApi.Standard.Utilities;

GetEnrolledCoursesByTimelineRequest getEnrolledCoursesByTimelineRequest = new GetEnrolledCoursesByTimelineRequest
{
    Offset = 0,
    Limit = 50,
    Classification = CourseTimelineClassification.Future,
    Sort = CourseTimelineSortField.Idnumber,
    ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
};
```



