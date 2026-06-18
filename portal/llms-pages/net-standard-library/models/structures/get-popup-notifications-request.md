# Get Popup Notifications Request

Source: /#/net-standard-library/x-redirect/JTI0bSUyRkdldFBvcHVwTm90aWZpY2F0aW9uc1JlcXVlc3Q

Request parameters for retrieving popup notifications for a user.

*This model accepts additional fields of type object.*


# Class Name

`GetPopupNotificationsRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Useridto` | `string` | Required | ID of the recipient user, passed as a string. |
| `Limit` | `int` | Required | Maximum number of notifications to return. |
| `Offset` | `int` | Required | Pagination offset.<br><br>**Default**: `0` |
| `AdditionalProperties` | `object this[string key]` | Optional | - |


# Example

```csharp
using NustLmsApi.Standard.Models;
using NustLmsApi.Standard.Utilities;

GetPopupNotificationsRequest getPopupNotificationsRequest = new GetPopupNotificationsRequest
{
    Useridto = "162154",
    Limit = 20,
    Offset = 0,
    ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
};
```



