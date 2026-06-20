# Get Users by Field Request

Source: /#/python/x-redirect/JTI0bSUyRkdldFVzZXJzQnlGaWVsZFJlcXVlc3Q

Request parameters for retrieving user profiles by a profile field value.

*This model accepts additional fields of type Any.*


# Class Name

`GetUsersByFieldRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field` | [`UserProfileField`](/llms-pages/python/models/enumerations/user-profile-field.md) | Required | User profile field to match against when searching for users. |
| `values` | `List[str]` | Required | List of field values to look up. All values must be provided as strings even when the field is numeric (e.g., "123456" for an integer ID). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |


# Example

```python
import jsonpickle

from nustlmsapi.models.get_users_by_field_request import GetUsersByFieldRequest
from nustlmsapi.models.user_profile_field import UserProfileField

get_users_by_field_request = GetUsersByFieldRequest(
    field=UserProfileField.ID,
    values=[
        '123456'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```



