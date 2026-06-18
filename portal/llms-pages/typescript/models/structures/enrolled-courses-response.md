# Enrolled Courses Response

Source: /#/typescript/x-redirect/JTI0bSUyRkVucm9sbGVkQ291cnNlc1Jlc3BvbnNl

Paginated enrolled-courses response.

*This model accepts additional fields of type unknown.*


# Interface Name

`EnrolledCoursesResponse`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `courses` | [`Course[]`](/llms-pages/typescript/models/structures/course.md) | Required | List of enrolled courses for the current page. |
| `nextoffset` | `number` | Required | Offset to pass on the next page request; -1 when no further pages exist. |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
import { EnrolledCoursesResponse } from 'nust-lms-apilib';

const enrolledCoursesResponse: EnrolledCoursesResponse = {
  courses: [
    {
      id: 49900,
      fullname: 'CS-212 Object Oriented Programming BSCS-13 2K23 ABC',
      shortname: 'CS-212-Sp\'24 BSCS-13 2K23 ABC',
      idnumber: '',
      summary: '',
      summaryformat: 1,
      startdate: 1706468400,
      enddate: 1717362000,
      visible: true,
      fullnamedisplay: 'CS-212 Object Oriented Programming BSCS-13 2K23 ABC',
      viewurl: 'https://lms.nust.edu.pk/portal/course/view.php?id=49900',
      progress: 21,
      hasprogress: true,
      isfavourite: false,
      hidden: false,
      showshortname: false,
      coursecategory: '2nd Semester (SP-2024)',
      additionalProperties: {
        'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
      },
    }
  ],
  nextoffset: 29,
  additionalProperties: {
    'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
  },
};
```



