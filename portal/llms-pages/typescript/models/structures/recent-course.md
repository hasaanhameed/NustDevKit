# Recent Course

Source: /#/typescript/x-redirect/JTI0bSUyRlJlY2VudENvdXJzZQ

A recently accessed course, extending Course with the last-access timestamp.

*This model accepts additional fields of type unknown.*


# Interface Name

`RecentCourse`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `number` | Required | Unique course identifier. |
| `fullname` | `string` | Required | Full display name of the course. |
| `shortname` | `string` | Required | Short course code or abbreviated name. |
| `idnumber` | `string` | Required | Institution-assigned course ID number; empty string if not set. |
| `summary` | `string` | Required | HTML summary of the course. |
| `summaryformat` | `number` | Required | Format of the summary field (1 = HTML). |
| `startdate` | `number` | Required | Course start date as Unix timestamp. |
| `enddate` | `number` | Required | Course end date as Unix timestamp. 0 means no end date. |
| `visible` | `boolean` | Required | Whether the course is visible to enrolled students. |
| `fullnamedisplay` | `string` | Required | Display name of the course (may differ from fullname for context). |
| `viewurl` | `string` | Required | URL to the course page on the LMS portal. |
| `progress` | `number` | Required | Student's completion progress as a percentage.<br><br>**Constraints**: `>= 0`, `<= 100` |
| `hasprogress` | `boolean` | Required | Whether completion tracking is enabled for this course. |
| `isfavourite` | `boolean` | Required | Whether the user has marked this course as a favourite. |
| `hidden` | `boolean` | Required | Whether the user has hidden this course from their dashboard. |
| `showshortname` | `boolean` | Required | Whether the short name is displayed alongside the full name. |
| `coursecategory` | `string` | Required | Name of the category this course belongs to. |
| `timeaccess` | `number` | Required | Unix timestamp of the user's most recent access to this course. |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
import { RecentCourse } from 'nust-lms-apilib';

const recentCourse: RecentCourse = {
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
  timeaccess: 1781632422,
  additionalProperties: {
    'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
  },
};
```



