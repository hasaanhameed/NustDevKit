# Get Calendar Events by Course Request

Source: /#/java/x-redirect/JTI0bSUyRkdldENhbGVuZGFyRXZlbnRzQnlDb3Vyc2VSZXF1ZXN0

Request parameters for retrieving calendar action events for a specific course.

*This model accepts additional fields of type Object.*


# Class Name

`GetCalendarEventsByCourseRequest`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Courseid` | `int` | Required | ID of the course to fetch events for. | int getCourseid() | setCourseid(int courseid) |
| `Timesortfrom` | `Integer` | Optional | Only return events with timesort >= this Unix timestamp. Optional. | Integer getTimesortfrom() | setTimesortfrom(Integer timesortfrom) |
| `Timesortto` | `Integer` | Optional | Only return events with timesort <= this Unix timestamp. Optional. | Integer getTimesortto() | setTimesortto(Integer timesortto) |
| `Aftereventid` | `Integer` | Optional | Cursor-based pagination — return events after this event ID. Optional. | Integer getAftereventid() | setAftereventid(Integer aftereventid) |
| `Limitnum` | `Integer` | Optional | Maximum number of events to return. Optional. | Integer getLimitnum() | setLimitnum(Integer limitnum) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import java.io.IOException;
import pk.edu.nust.lms.ApiHelper;
import pk.edu.nust.lms.models.GetCalendarEventsByCourseRequest;

GetCalendarEventsByCourseRequest getCalendarEventsByCourseRequest = new GetCalendarEventsByCourseRequest.Builder(
    49906
)
.timesortfrom(22)
.timesortto(138)
.aftereventid(136)
.limitnum(48)
.additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
.build();
```



