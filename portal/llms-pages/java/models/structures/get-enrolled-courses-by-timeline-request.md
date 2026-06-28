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
import com.nustdevkit.api.ApiHelper;
import com.nustdevkit.api.models.CourseTimelineClassification;
import com.nustdevkit.api.models.CourseTimelineSortField;
import com.nustdevkit.api.models.GetEnrolledCoursesByTimelineRequest;
import java.io.IOException;

GetEnrolledCoursesByTimelineRequest getEnrolledCoursesByTimelineRequest = new GetEnrolledCoursesByTimelineRequest.Builder(
    0,
    50,
    CourseTimelineClassification.FUTURE,
    CourseTimelineSortField.IDNUMBER
)
.additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
.build();
```



