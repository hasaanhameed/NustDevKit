# Get Calendar Events by Course Request

Source: /#/typescript/x-redirect/JTI0bSUyRkdldENhbGVuZGFyRXZlbnRzQnlDb3Vyc2VSZXF1ZXN0

Request parameters for retrieving calendar action events for a specific course.

*This model accepts additional fields of type unknown.*


# Interface Name

`GetCalendarEventsByCourseRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `courseid` | `number` | Required | ID of the course to fetch events for. |
| `timesortfrom` | `number \| undefined` | Optional | Only return events with timesort >= this Unix timestamp. Optional. |
| `timesortto` | `number \| undefined` | Optional | Only return events with timesort <= this Unix timestamp. Optional. |
| `aftereventid` | `number \| undefined` | Optional | Cursor-based pagination — return events after this event ID. Optional. |
| `limitnum` | `number \| undefined` | Optional | Maximum number of events to return. Optional. |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
import { GetCalendarEventsByCourseRequest } from 'nust-lms-apilib';

const getCalendarEventsByCourseRequest: GetCalendarEventsByCourseRequest = {
  courseid: 49906,
  timesortfrom: 22,
  timesortto: 138,
  aftereventid: 136,
  limitnum: 48,
  additionalProperties: {
    'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
  },
};
```



