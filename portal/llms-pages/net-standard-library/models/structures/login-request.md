# Login Request

Source: /#/net-standard-library/x-redirect/JTI0bSUyRkxvZ2luUmVxdWVzdA

NUST LMS credentials used to obtain a gateway bearer token.

*This model accepts additional fields of type object.*


# Class Name

`LoginRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Email` | `string` | Required | NUST LMS username or email. |
| `Password` | `string` | Required | NUST LMS password. |
| `AdditionalProperties` | `object this[string key]` | Optional | - |


# Example

```csharp
using NustLmsApi.Standard.Models;
using NustLmsApi.Standard.Utilities;

LoginRequest loginRequest = new LoginRequest
{
    Email = "john.doe@student.nust.edu.pk",
    Password = "password2",
    ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
};
```



