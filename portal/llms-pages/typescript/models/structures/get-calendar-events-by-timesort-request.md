# Get Calendar Events by Timesort Request

Source: /#/typescript/x-redirect/JTI0bSUyRkdldENhbGVuZGFyRXZlbnRzQnlUaW1lc29ydFJlcXVlc3Q

Request parameters for retrieving calendar action events sorted by time.

*This model accepts additional fields of type unknown.*


# Interface Name

`GetCalendarEventsByTimesortRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limitnum` | `number` | Required | Maximum number of events to return. |
| `timesortfrom` | `number` | Required | Only return events with timesort >= this Unix timestamp. Pass 0 for no lower bound. |
| `timesortto` | `number \| undefined` | Optional | Only return events with timesort <= this Unix timestamp. Optional. |
| `aftereventid` | `number \| undefined` | Optional | Return events whose ID is greater than this value (cursor pagination). Optional. |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
import { GetCalendarEventsByTimesortRequest } from 'nust-lms-apilib';

const getCalendarEventsByTimesortRequest: GetCalendarEventsByTimesortRequest = {
  limitnum: 20,
  timesortfrom: 0,
  timesortto: 114,
  aftereventid: 112,
  additionalProperties: {
    'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
  },
};
```



