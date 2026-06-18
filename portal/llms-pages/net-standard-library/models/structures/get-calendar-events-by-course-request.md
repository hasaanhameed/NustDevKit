# Get Calendar Events by Course Request

Source: /#/net-standard-library/x-redirect/JTI0bSUyRkdldENhbGVuZGFyRXZlbnRzQnlDb3Vyc2VSZXF1ZXN0

Request parameters for retrieving calendar action events for a specific course.

*This model accepts additional fields of type object.*


# Class Name

`GetCalendarEventsByCourseRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Courseid` | `int` | Required | ID of the course to fetch events for. |
| `Timesortfrom` | `int?` | Optional | Only return events with timesort >= this Unix timestamp. Optional. |
| `Timesortto` | `int?` | Optional | Only return events with timesort <= this Unix timestamp. Optional. |
| `Aftereventid` | `int?` | Optional | Cursor-based pagination — return events after this event ID. Optional. |
| `Limitnum` | `int?` | Optional | Maximum number of events to return. Optional. |
| `AdditionalProperties` | `object this[string key]` | Optional | - |


# Example

```csharp
using NustLmsApi.Standard.Models;
using NustLmsApi.Standard.Utilities;

GetCalendarEventsByCourseRequest getCalendarEventsByCourseRequest = new GetCalendarEventsByCourseRequest
{
    Courseid = 49906,
    Timesortfrom = 22,
    Timesortto = 138,
    Aftereventid = 136,
    Limitnum = 48,
    ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
};
```



