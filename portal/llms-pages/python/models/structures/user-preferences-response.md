# User Preferences Response

Source: /#/python/x-redirect/JTI0bSUyRlVzZXJQcmVmZXJlbmNlc1Jlc3BvbnNl

Response envelope for the user-preferences endpoint.

*This model accepts additional fields of type Any.*


# Class Name

`UserPreferencesResponse`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `preferences` | [`List[UserPreference]`](/llms-pages/python/models/structures/user-preference.md) | Required | List of user preference key/value pairs. |
| `warnings` | [`List[MoodleWarning]`](/llms-pages/python/models/structures/moodle-warning.md) | Required | Array of warning objects. Empty when no warnings are present. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |


# Example

```python
import jsonpickle

from nustlmsapi.models.moodle_warning import MoodleWarning
from nustlmsapi.models.user_preference import UserPreference
from nustlmsapi.models.user_preferences_response import UserPreferencesResponse

user_preferences_response = UserPreferencesResponse(
    preferences=[
        UserPreference(
            name='block_myoverview_user_sort_preference',
            value='title',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    warnings=[
        MoodleWarning(
            item='item6',
            itemid=0,
            warningcode='warningcode4',
            message='message4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```



