# Login Request

Source: /#/http/x-redirect/JTI0bSUyRkxvZ2luUmVxdWVzdA

NUST LMS credentials used to obtain a gateway bearer token.

*This model accepts additional fields of type Object.*


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `username` | `String` | Required | NUST LMS username. |
| `password` | `String` | Required | NUST LMS password. |
| `additionalProperties` | `Object` | Optional | - |


# Example (as JSON)

```json
{
  "username": "johndoe.bscs23seecs",
  "password": "password8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```



