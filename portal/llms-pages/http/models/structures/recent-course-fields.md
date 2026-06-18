# Recent Course Fields

Source: /#/http/x-redirect/JTI0bSUyRlJlY2VudENvdXJzZUZpZWxkcw

Additional fields specific to recently accessed courses.

*This model accepts additional fields of type Object.*


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `timeaccess` | `Number` | Required | Unix timestamp of the user's most recent access to this course. |
| `additionalProperties` | `Object` | Optional | - |


# Example (as JSON)

```json
{
  "timeaccess": 1781632422,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```



