# Get Calendar Events by Timesort Request

Source: /#/http/x-redirect/JTI0bSUyRkdldENhbGVuZGFyRXZlbnRzQnlUaW1lc29ydFJlcXVlc3Q

Request parameters for retrieving calendar action events sorted by time.

*This model accepts additional fields of type Object.*


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limitnum` | `Number` | Required | Maximum number of events to return. |
| `timesortfrom` | `Number` | Required | Only return events with timesort >= this Unix timestamp. Pass 0 for no lower bound. |
| `timesortto` | `Number` | Optional | Only return events with timesort <= this Unix timestamp. Optional. |
| `aftereventid` | `Number` | Optional | Return events whose ID is greater than this value (cursor pagination). Optional. |
| `additionalProperties` | `Object` | Optional | - |


# Example (as JSON)

```json
{
  "limitnum": 20,
  "timesortfrom": 0,
  "timesortto": 124,
  "aftereventid": 122,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```



