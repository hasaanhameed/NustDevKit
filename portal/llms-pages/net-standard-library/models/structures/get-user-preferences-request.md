# Get User Preferences Request

Source: /#/net-standard-library/x-redirect/JTI0bSUyRkdldFVzZXJQcmVmZXJlbmNlc1JlcXVlc3Q

Request parameters for retrieving user preferences.

*This model accepts additional fields of type object.*


# Class Name

`GetUserPreferencesRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Userid` | `int` | Required | ID of the user whose preferences to retrieve. |
| `Name` | `string` | Optional | Specific preference name to retrieve. Omit to retrieve all preferences. |
| `AdditionalProperties` | `object this[string key]` | Optional | - |


# Example

```csharp
using NustLmsApi.Standard.Models;
using NustLmsApi.Standard.Utilities;

GetUserPreferencesRequest getUserPreferencesRequest = new GetUserPreferencesRequest
{
    Userid = 162154,
    Name = "name6",
    ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
};
```



