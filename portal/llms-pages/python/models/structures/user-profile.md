# User Profile

Source: /#/python/x-redirect/JTI0bSUyRlVzZXJQcm9maWxl

Complete user profile.

*This model accepts additional fields of type Any.*


# Class Name

`UserProfile`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | Unique numeric user identifier. |
| `username` | `str` | Required | Login username for the user. |
| `fullname` | `str` | Required | Full display name of the user. |
| `email` | `str` | Required | Email address of the user. |
| `department` | `str` | Required | Department the user belongs to within the institution. |
| `institution` | `str` | Required | Name of the institution the user is affiliated with. |
| `idnumber` | `str` | Required | Institution-assigned student or staff ID number. |
| `auth` | `str` | Required | Authentication method used by the user (e.g., 'ldap', 'manual'). |
| `confirmed` | `bool` | Required | Whether the user's account has been confirmed. |
| `lang` | `str` | Required | Preferred interface language code (e.g., 'en'). |
| `theme` | `str` | Required | Preferred LMS theme; empty string means use the site default. |
| `timezone` | `str` | Required | Timezone identifier. "99" means use the server default. |
| `mailformat` | `int` | Required | Email format preference (1 = HTML). |
| `profileimageurlsmall` | `str` | Required | URL to the user's small profile image (thumbnail). |
| `profileimageurl` | `str` | Required | URL to the user's full-size profile image. |
| `customfields` | [`List[CustomField]`](/llms-pages/python/models/structures/custom-field.md) | Optional | List of custom profile field values for the user. |
| `preferences` | [`List[UserPreference]`](/llms-pages/python/models/structures/user-preference.md) | Optional | List of stored preference key/value pairs for the user. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |


# Example

```python
import jsonpickle

from nustlmsapi.models.custom_field import CustomField
from nustlmsapi.models.user_preference import UserPreference
from nustlmsapi.models.user_profile import UserProfile

user_profile = UserProfile(
    id=123456,
    username='johndoe.bscs23seecs',
    fullname='John Doe',
    email='johndoe.bscs23seecs@seecs.edu.pk',
    department='FoC',
    institution='SEECS',
    idnumber='00000454987',
    auth='ldap',
    confirmed=True,
    lang='en',
    theme=None,
    timezone='99',
    mailformat=1,
    profileimageurlsmall='https://lms.nust.edu.pk/portal/pluginfile.php/1583361/user/icon/moove/f2?rev=14452894',
    profileimageurl='https://lms.nust.edu.pk/portal/pluginfile.php/1583361/user/icon/moove/f1?rev=14452894',
    customfields=[
        CustomField(
            mtype='type8',
            value='value4',
            name='name2',
            shortname='shortname4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        CustomField(
            mtype='type8',
            value='value4',
            name='name2',
            shortname='shortname4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    preferences=[
        UserPreference(
            name='name8',
            value='value0',
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



