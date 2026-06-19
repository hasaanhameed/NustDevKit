# Login Request

Source: /#/python/x-redirect/JTI0bSUyRkxvZ2luUmVxdWVzdA

NUST LMS credentials used to obtain a gateway bearer token.

*This model accepts additional fields of type Any.*


# Class Name

`LoginRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `str` | Required | NUST LMS username or email. |
| `password` | `str` | Required | NUST LMS password. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |


# Example

```python
import jsonpickle

from nustlmsapi.models.login_request import LoginRequest

login_request = LoginRequest(
    email='john.doe@student.nust.edu.pk',
    password='password6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```



