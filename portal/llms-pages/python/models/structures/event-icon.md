# Event Icon

Source: /#/python/x-redirect/JTI0bSUyRkV2ZW50SWNvbg

Icon metadata for a calendar event.

*This model accepts additional fields of type Any.*


# Class Name

`EventIcon`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `str` | Required | Icon key name used to locate the icon asset. |
| `component` | `str` | Required | Moodle component that owns the icon (e.g., 'assign'). |
| `alttext` | `str` | Required | Accessible alt text for the icon image. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |


# Example

```python
import jsonpickle

from nustlmsapi.models.event_icon import EventIcon

event_icon = EventIcon(
    key='icon',
    component='assign',
    alttext='Activity event',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```



