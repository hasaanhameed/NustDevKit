# User Preferences Response

Source: /#/net-standard-library/x-redirect/JTI0bSUyRlVzZXJQcmVmZXJlbmNlc1Jlc3BvbnNl

Response envelope for the user-preferences endpoint.

*This model accepts additional fields of type object.*


# Class Name

`UserPreferencesResponse`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Preferences` | [`List<UserPreference>`](/llms-pages/net-standard-library/models/structures/user-preference.md) | Required | List of user preference key/value pairs. |
| `Warnings` | [`List<MoodleWarning>`](/llms-pages/net-standard-library/models/structures/moodle-warning.md) | Required | Array of warning objects. Empty when no warnings are present. |
| `AdditionalProperties` | `object this[string key]` | Optional | - |


# Example

```csharp
using NustLmsApi.Standard.Models;
using NustLmsApi.Standard.Utilities;
using System.Collections.Generic;

UserPreferencesResponse userPreferencesResponse = new UserPreferencesResponse
{
    Preferences = new List<UserPreference>
    {
        new UserPreference
        {
            Name = "block_myoverview_user_sort_preference",
            MValue = "title",
            ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
        },
    },
    Warnings = new List<MoodleWarning>
    {
        new MoodleWarning
        {
            Item = "item6",
            Itemid = 0,
            Warningcode = "warningcode4",
            Message = "message4",
            ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
        },
    },
    ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
};
```



