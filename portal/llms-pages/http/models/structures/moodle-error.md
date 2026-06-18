# Moodle Error

Source: /#/http/x-redirect/JTI0bSUyRk1vb2RsZUVycm9y

Error returned by the LMS on a failed operation.

*This model accepts additional fields of type Object.*


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errorcode` | `String` | Optional | Machine-readable error code identifier. |
| `message` | `String` | Optional | Human-readable error description. |
| `link` | `String` | Optional | Redirect URL for the user; empty string if not applicable. |
| `moreinfourl` | `String` | Optional | URL to additional error documentation; empty string if not available. |
| `debuginfo` | `String` | Optional | Additional debug information; empty string when not in debug mode. |
| `additionalProperties` | `Object` | Optional | - |


# Example (as JSON)

```json
{
  "errorcode": "invalidrecord",
  "message": "Can't find data record in database table.",
  "link": "link0",
  "moreinfourl": "moreinfourl8",
  "debuginfo": "debuginfo8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```



