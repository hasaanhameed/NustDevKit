# Token Response

Source: /#/http/x-redirect/JTI0bSUyRlRva2VuUmVzcG9uc2U

Bearer token issued by the gateway after a successful login.

*This model accepts additional fields of type Object.*


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `access_token` | `String` | Required | JWT to send as `Authorization: Bearer <token>` on subsequent requests. |
| `token_type` | `String` | Required | **Default**: `bearer` |
| `additionalProperties` | `Object` | Optional | - |


# Example (as JSON)

```json
{
  "access_token": "access_token4",
  "token_type": "bearer",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```



