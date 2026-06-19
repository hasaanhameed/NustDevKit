# Login Request

Source: /#/java/x-redirect/JTI0bSUyRkxvZ2luUmVxdWVzdA

NUST LMS credentials used to obtain a gateway bearer token.

*This model accepts additional fields of type Object.*


# Class Name

`LoginRequest`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Email` | `String` | Required | NUST LMS username or email. | String getEmail() | setEmail(String email) |
| `Password` | `String` | Required | NUST LMS password. | String getPassword() | setPassword(String password) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import java.io.IOException;
import m18000.m0.m0.m127.ApiHelper;
import m18000.m0.m0.m127.models.LoginRequest;

LoginRequest loginRequest = new LoginRequest.Builder(
    "john.doe@student.nust.edu.pk",
    "password2"
)
.additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
.build();
```



