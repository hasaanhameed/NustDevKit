# Fetch Notifications Request

Source: /#/net-standard-library/x-redirect/JTI0bSUyRkZldGNoTm90aWZpY2F0aW9uc1JlcXVlc3Q

Request parameters for fetching site-level notifications.

*This model accepts additional fields of type object.*


# Class Name

`FetchNotificationsRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Contextid` | `int` | Required | Moodle context ID for which to fetch notifications. The user context ID can be found in the user profile image URL path segment. |
| `AdditionalProperties` | `object this[string key]` | Optional | - |


# Example

```csharp
using NustLmsApi.Standard.Models;
using NustLmsApi.Standard.Utilities;

FetchNotificationsRequest fetchNotificationsRequest = new FetchNotificationsRequest
{
    Contextid = 1583361,
    ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
};
```



