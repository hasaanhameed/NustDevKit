# Site Notification

Source: /#/python/x-redirect/JTI0bSUyRlNpdGVOb3RpZmljYXRpb24

A site-level notification (structure varies by type).

*This model accepts additional fields of type Any.*


# Class Name

`SiteNotification`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | Unique identifier for the site notification. |
| `message` | `str` | Optional | Notification message content. |
| `mtype` | `str` | Optional | Notification type identifier. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |


# Example

```python
import jsonpickle

from nustlmsapi.models.site_notification import SiteNotification

site_notification = SiteNotification(
    id=238,
    message='message6',
    mtype='type6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```



