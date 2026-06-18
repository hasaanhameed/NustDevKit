# Get Calendar Events by Timesort Request

Source: /#/go/x-redirect/JTI0bSUyRkdldENhbGVuZGFyRXZlbnRzQnlUaW1lc29ydFJlcXVlc3Q

Request parameters for retrieving calendar action events sorted by time.

*This model accepts additional fields of type interface{}.*


# Class Name

`GetCalendarEventsByTimesortRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Limitnum` | `int` | Required | Maximum number of events to return. |
| `Timesortfrom` | `int` | Required | Only return events with timesort >= this Unix timestamp. Pass 0 for no lower bound. |
| `Timesortto` | `*int` | Optional | Only return events with timesort <= this Unix timestamp. Optional. |
| `Aftereventid` | `*int` | Optional | Return events whose ID is greater than this value (cursor pagination). Optional. |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
package main

import (
    "nustLmsApi/models"
)

func main() {
    getCalendarEventsByTimesortRequest := models.GetCalendarEventsByTimesortRequest{
        Limitnum:              20,
        Timesortfrom:          0,
        Timesortto:            models.ToPointer(114),
        Aftereventid:          models.ToPointer(112),
        AdditionalProperties:  map[string]interface{}{
            "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
        },
    }

}
```



