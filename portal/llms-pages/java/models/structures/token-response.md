# Token Response

Source: /#/java/x-redirect/JTI0bSUyRlRva2VuUmVzcG9uc2U

Bearer token issued by the gateway after a successful login.

*This model accepts additional fields of type Object.*


# Class Name

`TokenResponse`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `AccessToken` | `String` | Required | JWT to send as `Authorization: Bearer <token>` on subsequent requests. | String getAccessToken() | setAccessToken(String accessToken) |
| `TokenType` | `String` | Required | **Default**: `"bearer"` | String getTokenType() | setTokenType(String tokenType) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import com.nustdevkit.api.ApiHelper;
import com.nustdevkit.api.models.TokenResponse;
import java.io.IOException;

TokenResponse tokenResponse = new TokenResponse.Builder(
    "access_token2",
    "bearer"
)
.additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
.build();
```



