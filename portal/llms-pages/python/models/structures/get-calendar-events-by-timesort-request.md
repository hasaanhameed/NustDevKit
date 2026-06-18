# Get Calendar Events by Timesort Request

Source: /#/python/x-redirect/JTI0bSUyRkdldENhbGVuZGFyRXZlbnRzQnlUaW1lc29ydFJlcXVlc3Q

Request parameters for retrieving calendar action events sorted by time.

*This model accepts additional fields of type Any.*


# Class Name

`GetCalendarEventsByTimesortRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limitnum` | `int` | Required | Maximum number of events to return. |
| `timesortfrom` | `int` | Required | Only return events with timesort >= this Unix timestamp. Pass 0 for no lower bound. |
| `timesortto` | `int` | Optional | Only return events with timesort <= this Unix timestamp. Optional. |
| `aftereventid` | `int` | Optional | Return events whose ID is greater than this value (cursor pagination). Optional. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |


# Example

```python
import jsonpickle

from nustlmsapi.models.get_calendar_events_by_timesort_request import GetCalendarEventsByTimesortRequest

get_calendar_events_by_timesort_request = GetCalendarEventsByTimesortRequest(
    limitnum=20,
    timesortfrom=0,
    timesortto=182,
    aftereventid=180,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```



