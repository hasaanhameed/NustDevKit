# Event Icon

Source: /#/http/x-redirect/JTI0bSUyRkV2ZW50SWNvbg

Icon metadata for a calendar event.

*This model accepts additional fields of type Object.*


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `String` | Required | Icon key name used to locate the icon asset. |
| `component` | `String` | Required | Moodle component that owns the icon (e.g., 'assign'). |
| `alttext` | `String` | Required | Accessible alt text for the icon image. |
| `additionalProperties` | `Object` | Optional | - |


# Example (as JSON)

```json
{
  "key": "icon",
  "component": "assign",
  "alttext": "Activity event",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```



