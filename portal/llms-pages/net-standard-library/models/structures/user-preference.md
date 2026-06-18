# User Preference

Source: /#/net-standard-library/x-redirect/JTI0bSUyRlVzZXJQcmVmZXJlbmNl

A single user preference setting.

*This model accepts additional fields of type object.*


# Class Name

`UserPreference`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Name` | `string` | Required | Unique key identifying the preference. |
| `MValue` | `string` | Required | Preference value as a string. Note that the internal _lastloaded preference is returned as an integer by the LMS. |
| `AdditionalProperties` | `object this[string key]` | Optional | - |


# Example

```csharp
using NustLmsApi.Standard.Models;
using NustLmsApi.Standard.Utilities;

UserPreference userPreference = new UserPreference
{
    Name = "block_myoverview_user_sort_preference",
    MValue = "title",
    ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
};
```



