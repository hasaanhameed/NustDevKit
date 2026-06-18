# Get Popup Notifications Request

Source: /#/python/x-redirect/JTI0bSUyRkdldFBvcHVwTm90aWZpY2F0aW9uc1JlcXVlc3Q

Request parameters for retrieving popup notifications for a user.

*This model accepts additional fields of type Any.*


# Class Name

`GetPopupNotificationsRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `useridto` | `str` | Required | ID of the recipient user, passed as a string. |
| `limit` | `int` | Required | Maximum number of notifications to return. |
| `offset` | `int` | Required | Pagination offset.<br><br>**Default**: `0` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |


# Example

```python
import jsonpickle

from nustlmsapi.models.get_popup_notifications_request import GetPopupNotificationsRequest

get_popup_notifications_request = GetPopupNotificationsRequest(
    useridto='162154',
    limit=20,
    offset=0,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```



