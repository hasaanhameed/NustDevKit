# Token Response

Source: /#/net-standard-library/x-redirect/JTI0bSUyRlRva2VuUmVzcG9uc2U

Bearer token issued by the gateway after a successful login.

*This model accepts additional fields of type object.*


# Class Name

`TokenResponse`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `AccessToken` | `string` | Required | JWT to send as `Authorization: Bearer <token>` on subsequent requests. |
| `TokenType` | `string` | Required | **Default**: `"bearer"` |
| `AdditionalProperties` | `object this[string key]` | Optional | - |


# Example

```csharp
using NustLmsApi.Standard.Models;
using NustLmsApi.Standard.Utilities;

TokenResponse tokenResponse = new TokenResponse
{
    AccessToken = "access_token2",
    TokenType = "bearer",
    ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
};
```



