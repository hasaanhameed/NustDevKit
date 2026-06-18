# Get User Preferences Request

Source: /#/http/x-redirect/JTI0bSUyRkdldFVzZXJQcmVmZXJlbmNlc1JlcXVlc3Q

Request parameters for retrieving user preferences.

*This model accepts additional fields of type Object.*


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `userid` | `Number` | Required | ID of the user whose preferences to retrieve. |
| `name` | `String` | Optional | Specific preference name to retrieve. Omit to retrieve all preferences. |
| `additionalProperties` | `Object` | Optional | - |


# Example (as JSON)

```json
{
  "userid": 162154,
  "name": "name4",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```



