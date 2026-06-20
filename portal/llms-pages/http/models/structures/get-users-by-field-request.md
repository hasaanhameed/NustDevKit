# Get Users by Field Request

Source: /#/http/x-redirect/JTI0bSUyRkdldFVzZXJzQnlGaWVsZFJlcXVlc3Q

Request parameters for retrieving user profiles by a profile field value.

*This model accepts additional fields of type Object.*


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field` | [`User Profile Field`](/llms-pages/http/models/enumerations/user-profile-field.md) | Required | User profile field to match against when searching for users. |
| `values` | `array<String>` | Required | List of field values to look up. All values must be provided as strings even when the field is numeric (e.g., "123456" for an integer ID). |
| `additionalProperties` | `Object` | Optional | - |


# Example (as JSON)

```json
{
  "field": "id",
  "values": [
    "123456"
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```



