# Get User Preferences Request

Source: /#/python/x-redirect/JTI0bSUyRkdldFVzZXJQcmVmZXJlbmNlc1JlcXVlc3Q

Request parameters for retrieving user preferences.

*This model accepts additional fields of type Any.*


# Class Name

`GetUserPreferencesRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `userid` | `int` | Required | ID of the user whose preferences to retrieve. |
| `name` | `str` | Optional | Specific preference name to retrieve. Omit to retrieve all preferences. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |


# Example

```python
import jsonpickle

from nustlmsapi.models.get_user_preferences_request import GetUserPreferencesRequest

get_user_preferences_request = GetUserPreferencesRequest(
    userid=123456,
    name='name2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```



