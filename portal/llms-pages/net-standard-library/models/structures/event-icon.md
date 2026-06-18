# Event Icon

Source: /#/net-standard-library/x-redirect/JTI0bSUyRkV2ZW50SWNvbg

Icon metadata for a calendar event.

*This model accepts additional fields of type object.*


# Class Name

`EventIcon`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Key` | `string` | Required | Icon key name used to locate the icon asset. |
| `Component` | `string` | Required | Moodle component that owns the icon (e.g., 'assign'). |
| `Alttext` | `string` | Required | Accessible alt text for the icon image. |
| `AdditionalProperties` | `object this[string key]` | Optional | - |


# Example

```csharp
using NustLmsApi.Standard.Models;
using NustLmsApi.Standard.Utilities;

EventIcon eventIcon = new EventIcon
{
    Key = "icon",
    Component = "assign",
    Alttext = "Activity event",
    ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
};
```



