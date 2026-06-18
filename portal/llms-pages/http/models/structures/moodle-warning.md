# Moodle Warning

Source: /#/http/x-redirect/JTI0bSUyRk1vb2RsZVdhcm5pbmc

A non-fatal warning returned alongside a successful response.

*This model accepts additional fields of type Object.*


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item` | `String` | Optional | Item identifier related to the warning; empty string if not applicable. |
| `itemid` | `Number` | Optional | Numeric item ID related to the warning; 0 if not applicable. |
| `warningcode` | `String` | Optional | Machine-readable warning code; empty string if no code. |
| `message` | `String` | Optional | Human-readable warning description. |
| `additionalProperties` | `Object` | Optional | - |


# Example (as JSON)

```json
{
  "itemid": 0,
  "item": "item2",
  "warningcode": "warningcode0",
  "message": "message0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```



