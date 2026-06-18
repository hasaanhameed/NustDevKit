# User Preference

Source: /#/python/x-redirect/JTI0bSUyRlVzZXJQcmVmZXJlbmNl

A single user preference setting.

*This model accepts additional fields of type Any.*


# Class Name

`UserPreference`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | Unique key identifying the preference. |
| `value` | `str` | Required | Preference value as a string. Note that the internal _lastloaded preference is returned as an integer by the LMS. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |


# Example

```python
import jsonpickle

from nustlmsapi.models.user_preference import UserPreference

user_preference = UserPreference(
    name='block_myoverview_user_sort_preference',
    value='title',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```



