# Login Request

Source: /#/java/x-redirect/JTI0bSUyRkxvZ2luUmVxdWVzdA

NUST LMS credentials used to obtain a gateway bearer token.

*This model accepts additional fields of type Object.*


# Class Name

`LoginRequest`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Username` | `String` | Required | NUST LMS username. | String getUsername() | setUsername(String username) |
| `Password` | `String` | Required | NUST LMS password. | String getPassword() | setPassword(String password) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import com.nustdevkit.api.ApiHelper;
import com.nustdevkit.api.models.LoginRequest;
import java.io.IOException;

LoginRequest loginRequest = new LoginRequest.Builder(
    "johndoe.bscs23seecs",
    "password2"
)
.additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
.build();
```



