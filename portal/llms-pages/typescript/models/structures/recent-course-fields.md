# Recent Course Fields

Source: /#/typescript/x-redirect/JTI0bSUyRlJlY2VudENvdXJzZUZpZWxkcw

Additional fields specific to recently accessed courses.

*This model accepts additional fields of type unknown.*


# Interface Name

`RecentCourseFields`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `timeaccess` | `number` | Required | Unix timestamp of the user's most recent access to this course. |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
import { RecentCourseFields } from 'nust-lms-apilib';

const recentCourseFields: RecentCourseFields = {
  timeaccess: 1781632422,
  additionalProperties: {
    'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
  },
};
```



