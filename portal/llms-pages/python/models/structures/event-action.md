# Event Action

Source: /#/python/x-redirect/JTI0bSUyRkV2ZW50QWN0aW9u

Primary action button metadata for a calendar event.

*This model accepts additional fields of type Any.*


# Class Name

`EventAction`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | Display label for the primary action button. |
| `url` | `str` | Required | URL the user should navigate to in order to perform the action. |
| `itemcount` | `int` | Required | Number of items associated with this action. |
| `actionable` | `bool` | Required | Whether the action can currently be taken by the user. |
| `showitemcount` | `bool` | Required | Whether to display the item count alongside the action label. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |


# Example

```python
import jsonpickle

from nustlmsapi.models.event_action import EventAction

event_action = EventAction(
    name='Add submission',
    url='https://lms.nust.edu.pk/portal/mod/assign/view.php?id=999404&action=editsubmission',
    itemcount=1,
    actionable=True,
    showitemcount=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```



