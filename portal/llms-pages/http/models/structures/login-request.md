# Login Request

Source: /#/http/x-redirect/JTI0bSUyRkxvZ2luUmVxdWVzdA

NUST LMS credentials used to obtain a gateway bearer token.

*This model accepts additional fields of type Object.*


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `String` | Required | NUST LMS username or email. |
| `password` | `String` | Required | NUST LMS password. |
| `additionalProperties` | `Object` | Optional | - |


# Example (as JSON)

```json
{
  "email": "john.doe@student.nust.edu.pk",
  "password": "password8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```



