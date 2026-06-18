# Get Recent Courses Request

Source: /#/typescript/x-redirect/JTI0bSUyRkdldFJlY2VudENvdXJzZXNSZXF1ZXN0

Request parameters for retrieving recently accessed courses.

*This model accepts additional fields of type unknown.*


# Interface Name

`GetRecentCoursesRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `number` | Required | Maximum number of courses to return.<br><br>**Default**: `10` |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
import { GetRecentCoursesRequest } from 'nust-lms-apilib';

const getRecentCoursesRequest: GetRecentCoursesRequest = {
  limit: 10,
  additionalProperties: {
    'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
  },
};
```



