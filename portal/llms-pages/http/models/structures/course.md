# Course

Source: /#/http/x-redirect/JTI0bSUyRkNvdXJzZQ

An enrolled course.

*This model accepts additional fields of type Object.*


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `Number` | Required | Unique course identifier. |
| `fullname` | `String` | Required | Full display name of the course. |
| `shortname` | `String` | Required | Short course code or abbreviated name. |
| `idnumber` | `String` | Required | Institution-assigned course ID number; empty string if not set. |
| `summary` | `String` | Required | HTML summary of the course. |
| `summaryformat` | `Number` | Required | Format of the summary field (1 = HTML). |
| `startdate` | `Number` | Required | Course start date as Unix timestamp. |
| `enddate` | `Number` | Required | Course end date as Unix timestamp. 0 means no end date. |
| `visible` | `Boolean` | Required | Whether the course is visible to enrolled students. |
| `fullnamedisplay` | `String` | Required | Display name of the course (may differ from fullname for context). |
| `viewurl` | `String` | Required | URL to the course page on the LMS portal. |
| `progress` | `Number` | Required | Student's completion progress as a percentage.<br><br>**Constraints**: `>= 0`, `<= 100` |
| `hasprogress` | `Boolean` | Required | Whether completion tracking is enabled for this course. |
| `isfavourite` | `Boolean` | Required | Whether the user has marked this course as a favourite. |
| `hidden` | `Boolean` | Required | Whether the user has hidden this course from their dashboard. |
| `showshortname` | `Boolean` | Required | Whether the short name is displayed alongside the full name. |
| `coursecategory` | `String` | Required | Name of the category this course belongs to. |
| `additionalProperties` | `Object` | Optional | - |


# Example (as JSON)

```json
{
  "id": 49900,
  "fullname": "CS-212 Object Oriented Programming BSCS-13 2K23 ABC",
  "shortname": "CS-212-Sp'24 BSCS-13 2K23 ABC",
  "idnumber": null,
  "summary": null,
  "summaryformat": 1,
  "startdate": 1706468400,
  "enddate": 1717362000,
  "visible": true,
  "fullnamedisplay": "CS-212 Object Oriented Programming BSCS-13 2K23 ABC",
  "viewurl": "https://lms.nust.edu.pk/portal/course/view.php?id=49900",
  "progress": 21,
  "hasprogress": true,
  "isfavourite": false,
  "hidden": false,
  "showshortname": false,
  "coursecategory": "2nd Semester (SP-2024)",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```



