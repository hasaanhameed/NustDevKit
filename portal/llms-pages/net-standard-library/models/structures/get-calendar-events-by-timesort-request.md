# Get Calendar Events by Timesort Request

Source: /#/net-standard-library/x-redirect/JTI0bSUyRkdldENhbGVuZGFyRXZlbnRzQnlUaW1lc29ydFJlcXVlc3Q

Request parameters for retrieving calendar action events sorted by time.

*This model accepts additional fields of type object.*


# Class Name

`GetCalendarEventsByTimesortRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Limitnum` | `int` | Required | Maximum number of events to return. |
| `Timesortfrom` | `int` | Required | Only return events with timesort >= this Unix timestamp. Pass 0 for no lower bound. |
| `Timesortto` | `int?` | Optional | Only return events with timesort <= this Unix timestamp. Optional. |
| `Aftereventid` | `int?` | Optional | Return events whose ID is greater than this value (cursor pagination). Optional. |
| `AdditionalProperties` | `object this[string key]` | Optional | - |


# Example

```csharp
using NustLmsApi.Standard.Models;
using NustLmsApi.Standard.Utilities;

GetCalendarEventsByTimesortRequest getCalendarEventsByTimesortRequest = new GetCalendarEventsByTimesortRequest
{
    Limitnum = 20,
    Timesortfrom = 0,
    Timesortto = 114,
    Aftereventid = 112,
    ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
};
```



