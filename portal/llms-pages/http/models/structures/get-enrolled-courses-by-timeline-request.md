# Get Enrolled Courses by Timeline Request

Source: /#/http/x-redirect/JTI0bSUyRkdldEVucm9sbGVkQ291cnNlc0J5VGltZWxpbmVSZXF1ZXN0

Request parameters for retrieving enrolled courses filtered by timeline classification.

*This model accepts additional fields of type Object.*


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `offset` | `Number` | Required | Zero-based pagination offset.<br><br>**Default**: `0` |
| `limit` | `Number` | Required | Maximum number of courses to return.<br><br>**Default**: `50` |
| `classification` | [`Course Timeline Classification`](/llms-pages/http/models/enumerations/course-timeline-classification.md) | Required | Timeline classification filter for enrolled courses. |
| `sort` | [`Course Timeline Sort Field`](/llms-pages/http/models/enumerations/course-timeline-sort-field.md) | Required | Field used to sort enrolled course results. |
| `additionalProperties` | `Object` | Optional | - |


# Example (as JSON)

```json
{
  "offset": 0,
  "limit": 50,
  "classification": "hidden",
  "sort": "id",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```



