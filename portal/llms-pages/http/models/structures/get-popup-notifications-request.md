# Get Popup Notifications Request

Source: /#/http/x-redirect/JTI0bSUyRkdldFBvcHVwTm90aWZpY2F0aW9uc1JlcXVlc3Q

Request parameters for retrieving popup notifications for a user.

*This model accepts additional fields of type Object.*


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `useridto` | `String` | Required | ID of the recipient user, passed as a string. |
| `limit` | `Number` | Required | Maximum number of notifications to return. |
| `offset` | `Number` | Required | Pagination offset.<br><br>**Default**: `0` |
| `additionalProperties` | `Object` | Optional | - |


# Example (as JSON)

```json
{
  "useridto": "123456",
  "limit": 20,
  "offset": 0,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```



