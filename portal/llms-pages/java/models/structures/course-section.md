# Course Section

Source: /#/java/x-redirect/JTI0bSUyRkNvdXJzZVNlY3Rpb24

A section (week/topic) of the course, containing its modules.

*This model accepts additional fields of type Object.*


# Class Name

`CourseSection`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Id` | `int` | Required | Section ID. | int getId() | setId(int id) |
| `Name` | `String` | Required | Section title (e.g. a week or topic name). | String getName() | setName(String name) |
| `Section` | `int` | Required | Zero-based section number within the course. | int getSection() | setSection(int section) |
| `Visible` | `Integer` | Optional | Whether the section is visible (1) or hidden (0). | Integer getVisible() | setVisible(Integer visible) |
| `Summary` | `String` | Optional | HTML summary shown at the top of the section. | String getSummary() | setSummary(String summary) |
| `Summaryformat` | `Integer` | Optional | Moodle text format of the summary (1 = HTML). | Integer getSummaryformat() | setSummaryformat(Integer summaryformat) |
| `Uservisible` | `Boolean` | Optional | Whether the section is visible to the current user. | Boolean getUservisible() | setUservisible(Boolean uservisible) |
| `Modules` | [`List<CourseModule>`](/llms-pages/java/models/structures/course-module.md) | Required | The activities and resources in this section. | List<CourseModule> getModules() | setModules(List<CourseModule> modules) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import java.io.IOException;
import java.util.Arrays;
import m18000.m0.m0.m127.ApiHelper;
import m18000.m0.m0.m127.models.CourseModule;
import m18000.m0.m0.m127.models.CourseSection;

CourseSection courseSection = new CourseSection.Builder(
    33445,
    "Week 1",
    1,
    Arrays.asList(
        new CourseModule.Builder(
            987654,
            "Lecture 01 — Introduction",
            "resource"
        )
        .modplural("Files")
        .instance(45678)
        .description("<p>Course introduction and logistics.</p>")
        .visible(1)
        .uservisible(true)
        .url("https://lms.nust.edu.pk/portal/mod/resource/view.php?id=987654")
        .modicon("https://lms.nust.edu.pk/portal/theme/image.php/moove/core/1/f/pdf")
        .additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
        .build()
    )
)
.visible(1)
.summary("<p>Introduction and course overview.</p>")
.summaryformat(1)
.uservisible(true)
.additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
.build();
```



