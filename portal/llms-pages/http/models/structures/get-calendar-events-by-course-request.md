# Get Calendar Events by Course Request

Source: /#/http/x-redirect/JTI0bSUyRkdldENhbGVuZGFyRXZlbnRzQnlDb3Vyc2VSZXF1ZXN0

Request parameters for retrieving calendar action events for a specific course.

*This model accepts additional fields of type Object.*


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `courseid` | `Number` | Required | ID of the course to fetch events for. |
| `timesortfrom` | `Number` | Optional | Only return events with timesort >= this Unix timestamp. Optional. |
| `timesortto` | `Number` | Optional | Only return events with timesort <= this Unix timestamp. Optional. |
| `aftereventid` | `Number` | Optional | Cursor-based pagination — return events after this event ID. Optional. |
| `limitnum` | `Number` | Optional | Maximum number of events to return. Optional. |
| `additionalProperties` | `Object` | Optional | - |


# Example (as JSON)

```json
{
  "courseid": 49906,
  "timesortfrom": 134,
  "timesortto": 238,
  "aftereventid": 236,
  "limitnum": 148,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```



