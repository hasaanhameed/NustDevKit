# Course Module

Source: /#/java/x-redirect/JTI0bSUyRkNvdXJzZU1vZHVsZQ

An item on the course page — an activity or resource (file, page, URL, assignment, ...).

*This model accepts additional fields of type Object.*


# Class Name

`CourseModule`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Id` | `int` | Required | Course module ID (cmid). | int getId() | setId(int id) |
| `Name` | `String` | Required | Display name of the module. | String getName() | setName(String name) |
| `Modname` | `String` | Required | Module type, e.g. 'resource' (file), 'folder', 'url', 'page', 'label', 'assign', 'quiz', 'forum'. | String getModname() | setModname(String modname) |
| `Modplural` | `String` | Optional | Human-readable plural label for the module type. | String getModplural() | setModplural(String modplural) |
| `Instance` | `Integer` | Optional | Instance ID of the activity within its module type. | Integer getInstance() | setInstance(Integer instance) |
| `Description` | `String` | Optional | HTML description/intro for the module, when present. | String getDescription() | setDescription(String description) |
| `Visible` | `Integer` | Optional | Whether the module is visible (1) or hidden (0). | Integer getVisible() | setVisible(Integer visible) |
| `Uservisible` | `Boolean` | Optional | Whether the module is visible to the current user. | Boolean getUservisible() | setUservisible(Boolean uservisible) |
| `Url` | `String` | Optional | Link to open the activity/resource, when applicable. | String getUrl() | setUrl(String url) |
| `Modicon` | `String` | Optional | URL of the module's type icon. | String getModicon() | setModicon(String modicon) |
| `Contents` | [`List<CourseContentFile>`](/llms-pages/java/models/structures/course-content-file.md) | Optional | Uploaded files/links for this module (present for resource/folder modules). | List<CourseContentFile> getContents() | setContents(List<CourseContentFile> contents) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import com.nustdevkit.api.ApiHelper;
import com.nustdevkit.api.models.CourseModule;
import java.io.IOException;

CourseModule courseModule = new CourseModule.Builder(
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
.build();
```



