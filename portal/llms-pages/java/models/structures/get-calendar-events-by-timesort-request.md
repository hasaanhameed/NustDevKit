# Get Calendar Events by Timesort Request

Source: /#/java/x-redirect/JTI0bSUyRkdldENhbGVuZGFyRXZlbnRzQnlUaW1lc29ydFJlcXVlc3Q

Request parameters for retrieving calendar action events sorted by time.

*This model accepts additional fields of type Object.*


# Class Name

`GetCalendarEventsByTimesortRequest`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Limitnum` | `int` | Required | Maximum number of events to return. | int getLimitnum() | setLimitnum(int limitnum) |
| `Timesortfrom` | `int` | Required | Only return events with timesort >= this Unix timestamp. Pass 0 for no lower bound. | int getTimesortfrom() | setTimesortfrom(int timesortfrom) |
| `Timesortto` | `Integer` | Optional | Only return events with timesort <= this Unix timestamp. Optional. | Integer getTimesortto() | setTimesortto(Integer timesortto) |
| `Aftereventid` | `Integer` | Optional | Return events whose ID is greater than this value (cursor pagination). Optional. | Integer getAftereventid() | setAftereventid(Integer aftereventid) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import com.nustdevkit.api.ApiHelper;
import com.nustdevkit.api.models.GetCalendarEventsByTimesortRequest;
import java.io.IOException;

GetCalendarEventsByTimesortRequest getCalendarEventsByTimesortRequest = new GetCalendarEventsByTimesortRequest.Builder(
    20,
    0
)
.timesortto(114)
.aftereventid(112)
.additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
.build();
```



