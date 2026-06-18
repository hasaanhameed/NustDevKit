# Enrolled Courses Response

Source: /#/http/x-redirect/JTI0bSUyRkVucm9sbGVkQ291cnNlc1Jlc3BvbnNl

Paginated enrolled-courses response.

*This model accepts additional fields of type Object.*


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `courses` | [`array<Course>`](/llms-pages/http/models/structures/course.md) | Required | List of enrolled courses for the current page. |
| `nextoffset` | `Number` | Required | Offset to pass on the next page request; -1 when no further pages exist. |
| `additionalProperties` | `Object` | Optional | - |


# Example (as JSON)

```json
{
  "courses": [
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
  ],
  "nextoffset": 29,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```



