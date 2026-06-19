# Token Response

Source: /#/python/x-redirect/JTI0bSUyRlRva2VuUmVzcG9uc2U

Bearer token issued by the gateway after a successful login.

*This model accepts additional fields of type Any.*


# Class Name

`TokenResponse`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `access_token` | `str` | Required | JWT to send as `Authorization: Bearer <token>` on subsequent requests. |
| `token_type` | `str` | Required | **Default**: `"bearer"` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |


# Example

```python
import jsonpickle

from nustlmsapi.models.token_response import TokenResponse

token_response = TokenResponse(
    access_token='access_token0',
    token_type='bearer',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```



