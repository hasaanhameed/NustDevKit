# Enrolled Courses Response

Source: /#/java/x-redirect/JTI0bSUyRkVucm9sbGVkQ291cnNlc1Jlc3BvbnNl

Paginated enrolled-courses response.

*This model accepts additional fields of type Object.*


# Class Name

`EnrolledCoursesResponse`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Courses` | [`List<Course>`](/llms-pages/java/models/structures/course.md) | Required | List of enrolled courses for the current page. | List<Course> getCourses() | setCourses(List<Course> courses) |
| `Nextoffset` | `int` | Required | Offset to pass on the next page request; -1 when no further pages exist. | int getNextoffset() | setNextoffset(int nextoffset) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import com.nustdevkit.api.ApiHelper;
import com.nustdevkit.api.models.Course;
import com.nustdevkit.api.models.EnrolledCoursesResponse;
import java.io.IOException;
import java.util.Arrays;

EnrolledCoursesResponse enrolledCoursesResponse = new EnrolledCoursesResponse.Builder(
    Arrays.asList(
        new Course.Builder(
            49900,
            "CS-212 Object Oriented Programming BSCS-13 2K23 ABC",
            "CS-212-Sp'24 BSCS-13 2K23 ABC",
            null,
            null,
            1,
            1706468400,
            1717362000,
            true,
            "CS-212 Object Oriented Programming BSCS-13 2K23 ABC",
            "https://lms.nust.edu.pk/portal/course/view.php?id=49900",
            21,
            true,
            false,
            false,
            false,
            "2nd Semester (SP-2024)"
        )
        .additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
        .build()
    ),
    29
)
.additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
.build();
```



