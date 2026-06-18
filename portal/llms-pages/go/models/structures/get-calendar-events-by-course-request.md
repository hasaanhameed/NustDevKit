# Get Calendar Events by Course Request

Source: /#/go/x-redirect/JTI0bSUyRkdldENhbGVuZGFyRXZlbnRzQnlDb3Vyc2VSZXF1ZXN0

Request parameters for retrieving calendar action events for a specific course.

*This model accepts additional fields of type interface{}.*


# Class Name

`GetCalendarEventsByCourseRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Courseid` | `int` | Required | ID of the course to fetch events for. |
| `Timesortfrom` | `*int` | Optional | Only return events with timesort >= this Unix timestamp. Optional. |
| `Timesortto` | `*int` | Optional | Only return events with timesort <= this Unix timestamp. Optional. |
| `Aftereventid` | `*int` | Optional | Cursor-based pagination — return events after this event ID. Optional. |
| `Limitnum` | `*int` | Optional | Maximum number of events to return. Optional. |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
package main

import (
    "nustLmsApi/models"
)

func main() {
    getCalendarEventsByCourseRequest := models.GetCalendarEventsByCourseRequest{
        Courseid:              49906,
        Timesortfrom:          models.ToPointer(22),
        Timesortto:            models.ToPointer(138),
        Aftereventid:          models.ToPointer(136),
        Limitnum:              models.ToPointer(48),
        AdditionalProperties:  map[string]interface{}{
            "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
        },
    }

}
```



