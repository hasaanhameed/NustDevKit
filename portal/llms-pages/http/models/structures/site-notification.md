# Site Notification

Source: /#/http/x-redirect/JTI0bSUyRlNpdGVOb3RpZmljYXRpb24

A site-level notification (structure varies by type).

*This model accepts additional fields of type Object.*


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `Number` | Optional | Unique identifier for the site notification. |
| `message` | `String` | Optional | Notification message content. |
| `type` | `String` | Optional | Notification type identifier. |
| `additionalProperties` | `Object` | Optional | - |


# Example (as JSON)

```json
{
  "id": 220,
  "message": "message2",
  "type": "type2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```



