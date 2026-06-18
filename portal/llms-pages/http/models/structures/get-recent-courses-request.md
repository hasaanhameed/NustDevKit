# Get Recent Courses Request

Source: /#/http/x-redirect/JTI0bSUyRkdldFJlY2VudENvdXJzZXNSZXF1ZXN0

Request parameters for retrieving recently accessed courses.

*This model accepts additional fields of type Object.*


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `Number` | Required | Maximum number of courses to return.<br><br>**Default**: `10` |
| `additionalProperties` | `Object` | Optional | - |


# Example (as JSON)

```json
{
  "limit": 10,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```



