# Get Recent Courses Request

Source: /#/java/x-redirect/JTI0bSUyRkdldFJlY2VudENvdXJzZXNSZXF1ZXN0

Request parameters for retrieving recently accessed courses.

*This model accepts additional fields of type Object.*


# Class Name

`GetRecentCoursesRequest`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Limit` | `int` | Required | Maximum number of courses to return.<br><br>**Default**: `10` | int getLimit() | setLimit(int limit) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import com.nustdevkit.api.ApiHelper;
import com.nustdevkit.api.models.GetRecentCoursesRequest;
import java.io.IOException;

GetRecentCoursesRequest getRecentCoursesRequest = new GetRecentCoursesRequest.Builder(
    10
)
.additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
.build();
```



