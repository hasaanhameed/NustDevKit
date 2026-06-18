# Get Users by Field Request

Source: /#/net-standard-library/x-redirect/JTI0bSUyRkdldFVzZXJzQnlGaWVsZFJlcXVlc3Q

Request parameters for retrieving user profiles by a profile field value.

*This model accepts additional fields of type object.*


# Class Name

`GetUsersByFieldRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Field` | [`UserProfileField`](/llms-pages/net-standard-library/models/enumerations/user-profile-field.md) | Required | User profile field to match against when searching for users. |
| `Values` | `List<string>` | Required | List of field values to look up. All values must be provided as strings even when the field is numeric (e.g., "162154" for an integer ID). |
| `AdditionalProperties` | `object this[string key]` | Optional | - |


# Example

```csharp
using NustLmsApi.Standard.Models;
using NustLmsApi.Standard.Utilities;
using System.Collections.Generic;

GetUsersByFieldRequest getUsersByFieldRequest = new GetUsersByFieldRequest
{
    Field = UserProfileField.Id,
    Values = new List<string>
    {
        "162154",
    },
    ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
};
```



