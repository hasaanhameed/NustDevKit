# Custom Field

Source: /#/net-standard-library/x-redirect/JTI0bSUyRkN1c3RvbUZpZWxk

A custom profile field value attached to a user.

*This model accepts additional fields of type object.*


# Class Name

`CustomField`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Type` | `string` | Required | Data type of the custom field (e.g., 'text', 'select'). |
| `MValue` | `string` | Required | Value stored in the custom field. |
| `Name` | `string` | Required | Display label of the custom field. |
| `Shortname` | `string` | Required | Machine-readable shortname identifier for the custom field. |
| `AdditionalProperties` | `object this[string key]` | Optional | - |


# Example

```csharp
using NustLmsApi.Standard.Models;
using NustLmsApi.Standard.Utilities;

CustomField customField = new CustomField
{
    Type = "text",
    MValue = "SEECS",
    Name = "Institute",
    Shortname = "institution",
    ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
};
```



