# Get Enrolled Courses by Timeline Request

Source: /#/typescript/x-redirect/JTI0bSUyRkdldEVucm9sbGVkQ291cnNlc0J5VGltZWxpbmVSZXF1ZXN0

Request parameters for retrieving enrolled courses filtered by timeline classification.

*This model accepts additional fields of type unknown.*


# Interface Name

`GetEnrolledCoursesByTimelineRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `offset` | `number` | Required | Zero-based pagination offset.<br><br>**Default**: `0` |
| `limit` | `number` | Required | Maximum number of courses to return.<br><br>**Default**: `50` |
| `classification` | [`CourseTimelineClassification`](/llms-pages/typescript/models/enumerations/course-timeline-classification.md) | Required | Timeline classification filter for enrolled courses. |
| `sort` | [`CourseTimelineSortField`](/llms-pages/typescript/models/enumerations/course-timeline-sort-field.md) | Required | Field used to sort enrolled course results. |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
import {
  CourseTimelineClassification,
  CourseTimelineSortField,
  GetEnrolledCoursesByTimelineRequest,
} from 'nust-lms-apilib';

const getEnrolledCoursesByTimelineRequest: GetEnrolledCoursesByTimelineRequest = {
  offset: 0,
  limit: 50,
  classification: CourseTimelineClassification.Future,
  sort: CourseTimelineSortField.Idnumber,
  additionalProperties: {
    'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
  },
};
```



