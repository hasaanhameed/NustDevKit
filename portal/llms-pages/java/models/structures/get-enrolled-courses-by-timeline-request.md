# Get Enrolled Courses by Timeline Request

Source: /#/java/x-redirect/JTI0bSUyRkdldEVucm9sbGVkQ291cnNlc0J5VGltZWxpbmVSZXF1ZXN0

Request parameters for retrieving enrolled courses filtered by timeline classification.

*This model accepts additional fields of type Object.*


# Class Name

`GetEnrolledCoursesByTimelineRequest`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Offset` | `int` | Required | Zero-based pagination offset.<br><br>**Default**: `0` | int getOffset() | setOffset(int offset) |
| `Limit` | `int` | Required | Maximum number of courses to return.<br><br>**Default**: `50` | int getLimit() | setLimit(int limit) |
| `Classification` | [`CourseTimelineClassification`](/llms-pages/java/models/enumerations/course-timeline-classification.md) | Required | Timeline classification filter for enrolled courses. | CourseTimelineClassification getClassification() | setClassification(CourseTimelineClassification classification) |
| `Sort` | [`CourseTimelineSortField`](/llms-pages/java/models/enumerations/course-timeline-sort-field.md) | Required | Field used to sort enrolled course results. | CourseTimelineSortField getSort() | setSort(CourseTimelineSortField sort) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import java.io.IOException;
import m18000.m0.m0.m127.ApiHelper;
import m18000.m0.m0.m127.models.CourseTimelineClassification;
import m18000.m0.m0.m127.models.CourseTimelineSortField;
import m18000.m0.m0.m127.models.GetEnrolledCoursesByTimelineRequest;

GetEnrolledCoursesByTimelineRequest getEnrolledCoursesByTimelineRequest = new GetEnrolledCoursesByTimelineRequest.Builder(
    0,
    50,
    CourseTimelineClassification.FUTURE,
    CourseTimelineSortField.IDNUMBER
)
.additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
.build();
```



