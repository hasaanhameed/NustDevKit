# Recent Course Fields

Source: /#/java/x-redirect/JTI0bSUyRlJlY2VudENvdXJzZUZpZWxkcw

Additional fields specific to recently accessed courses.

*This model accepts additional fields of type Object.*


# Class Name

`RecentCourseFields`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Timeaccess` | `int` | Required | Unix timestamp of the user's most recent access to this course. | int getTimeaccess() | setTimeaccess(int timeaccess) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import com.nustdevkit.api.ApiHelper;
import com.nustdevkit.api.models.RecentCourseFields;
import java.io.IOException;

RecentCourseFields recentCourseFields = new RecentCourseFields.Builder(
    1781632422
)
.additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
.build();
```



