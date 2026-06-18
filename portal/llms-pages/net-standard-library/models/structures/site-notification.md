# Site Notification

Source: /#/net-standard-library/x-redirect/JTI0bSUyRlNpdGVOb3RpZmljYXRpb24

A site-level notification (structure varies by type).

*This model accepts additional fields of type object.*


# Class Name

`SiteNotification`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Id` | `int?` | Optional | Unique identifier for the site notification. |
| `Message` | `string` | Optional | Notification message content. |
| `Type` | `string` | Optional | Notification type identifier. |
| `AdditionalProperties` | `object this[string key]` | Optional | - |


# Example

```csharp
using NustLmsApi.Standard.Models;
using NustLmsApi.Standard.Utilities;

SiteNotification siteNotification = new SiteNotification
{
    Id = 96,
    Message = "message8",
    Type = "type8",
    ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
};
```



