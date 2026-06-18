# Event Subscription

Source: /#/python/x-redirect/JTI0bSUyRkV2ZW50U3Vic2NyaXB0aW9u

Subscription display settings for a calendar event.

*This model accepts additional fields of type Any.*


# Class Name

`EventSubscription`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `displayeventsource` | `bool` | Required | Whether to display the event source label on the calendar. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |


# Example

```python
import jsonpickle

from nustlmsapi.models.event_subscription import EventSubscription

event_subscription = EventSubscription(
    displayeventsource=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```



