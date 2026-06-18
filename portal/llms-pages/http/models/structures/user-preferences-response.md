# User Preferences Response

Source: /#/http/x-redirect/JTI0bSUyRlVzZXJQcmVmZXJlbmNlc1Jlc3BvbnNl

Response envelope for the user-preferences endpoint.

*This model accepts additional fields of type Object.*


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `preferences` | [`array<User Preference>`](/llms-pages/http/models/structures/user-preference.md) | Required | List of user preference key/value pairs. |
| `warnings` | [`array<Moodle Warning>`](/llms-pages/http/models/structures/moodle-warning.md) | Required | Array of warning objects. Empty when no warnings are present. |
| `additionalProperties` | `Object` | Optional | - |


# Example (as JSON)

```json
{
  "preferences": [
    {
      "name": "block_myoverview_user_sort_preference",
      "value": "title",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "warnings": [
    {
      "itemid": 0,
      "item": "item6",
      "warningcode": "warningcode4",
      "message": "message4",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```



