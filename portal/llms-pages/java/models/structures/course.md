# Course

Source: /#/java/x-redirect/JTI0bSUyRkNvdXJzZQ

An enrolled course.

*This model accepts additional fields of type Object.*


# Class Name

`Course`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Id` | `int` | Required | Unique course identifier. | int getId() | setId(int id) |
| `Fullname` | `String` | Required | Full display name of the course. | String getFullname() | setFullname(String fullname) |
| `Shortname` | `String` | Required | Short course code or abbreviated name. | String getShortname() | setShortname(String shortname) |
| `Idnumber` | `String` | Required | Institution-assigned course ID number; empty string if not set. | String getIdnumber() | setIdnumber(String idnumber) |
| `Summary` | `String` | Required | HTML summary of the course. | String getSummary() | setSummary(String summary) |
| `Summaryformat` | `int` | Required | Format of the summary field (1 = HTML). | int getSummaryformat() | setSummaryformat(int summaryformat) |
| `Startdate` | `int` | Required | Course start date as Unix timestamp. | int getStartdate() | setStartdate(int startdate) |
| `Enddate` | `int` | Required | Course end date as Unix timestamp. 0 means no end date. | int getEnddate() | setEnddate(int enddate) |
| `Visible` | `boolean` | Required | Whether the course is visible to enrolled students. | boolean getVisible() | setVisible(boolean visible) |
| `Fullnamedisplay` | `String` | Required | Display name of the course (may differ from fullname for context). | String getFullnamedisplay() | setFullnamedisplay(String fullnamedisplay) |
| `Viewurl` | `String` | Required | URL to the course page on the LMS portal. | String getViewurl() | setViewurl(String viewurl) |
| `Progress` | `int` | Required | Student's completion progress as a percentage.<br><br>**Constraints**: `>= 0`, `<= 100` | int getProgress() | setProgress(int progress) |
| `Hasprogress` | `boolean` | Required | Whether completion tracking is enabled for this course. | boolean getHasprogress() | setHasprogress(boolean hasprogress) |
| `Isfavourite` | `boolean` | Required | Whether the user has marked this course as a favourite. | boolean getIsfavourite() | setIsfavourite(boolean isfavourite) |
| `Hidden` | `boolean` | Required | Whether the user has hidden this course from their dashboard. | boolean getHidden() | setHidden(boolean hidden) |
| `Showshortname` | `boolean` | Required | Whether the short name is displayed alongside the full name. | boolean getShowshortname() | setShowshortname(boolean showshortname) |
| `Coursecategory` | `String` | Required | Name of the category this course belongs to. | String getCoursecategory() | setCoursecategory(String coursecategory) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import java.io.IOException;
import m18000.m0.m0.m127.ApiHelper;
import m18000.m0.m0.m127.models.Course;

Course course = new Course.Builder(
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
.build();
```



