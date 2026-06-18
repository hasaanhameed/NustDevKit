# Fetch Notifications Request

Source: /#/http/x-redirect/JTI0bSUyRkZldGNoTm90aWZpY2F0aW9uc1JlcXVlc3Q

Request parameters for fetching site-level notifications.

*This model accepts additional fields of type Object.*


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `contextid` | `Number` | Required | Moodle context ID for which to fetch notifications. The user context ID can be found in the user profile image URL path segment. |
| `additionalProperties` | `Object` | Optional | - |


# Example (as JSON)

```json
{
  "contextid": 1583361,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```



