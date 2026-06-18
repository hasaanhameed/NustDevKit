# Moodle Warning

Source: /#/net-standard-library/x-redirect/JTI0bSUyRk1vb2RsZVdhcm5pbmc

A non-fatal warning returned alongside a successful response.

*This model accepts additional fields of type object.*


# Class Name

`MoodleWarning`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Item` | `string` | Optional | Item identifier related to the warning; empty string if not applicable. |
| `Itemid` | `int?` | Optional | Numeric item ID related to the warning; 0 if not applicable. |
| `Warningcode` | `string` | Optional | Machine-readable warning code; empty string if no code. |
| `Message` | `string` | Optional | Human-readable warning description. |
| `AdditionalProperties` | `object this[string key]` | Optional | - |


# Example

```csharp
using NustLmsApi.Standard.Models;
using NustLmsApi.Standard.Utilities;

MoodleWarning moodleWarning = new MoodleWarning
{
    Item = "item6",
    Itemid = 0,
    Warningcode = "warningcode6",
    Message = "message4",
    ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
};
```



