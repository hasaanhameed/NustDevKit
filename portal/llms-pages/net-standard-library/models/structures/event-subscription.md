# Event Subscription

Source: /#/net-standard-library/x-redirect/JTI0bSUyRkV2ZW50U3Vic2NyaXB0aW9u

Subscription display settings for a calendar event.

*This model accepts additional fields of type object.*


# Class Name

`EventSubscription`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Displayeventsource` | `bool` | Required | Whether to display the event source label on the calendar. |
| `AdditionalProperties` | `object this[string key]` | Optional | - |


# Example

```csharp
using NustLmsApi.Standard.Models;
using NustLmsApi.Standard.Utilities;

EventSubscription eventSubscription = new EventSubscription
{
    Displayeventsource = false,
    ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
};
```



