# Get User Preferences Request

Source: /#/java/x-redirect/JTI0bSUyRkdldFVzZXJQcmVmZXJlbmNlc1JlcXVlc3Q

Request parameters for retrieving user preferences.

*This model accepts additional fields of type Object.*


# Class Name

`GetUserPreferencesRequest`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Userid` | `int` | Required | ID of the user whose preferences to retrieve. | int getUserid() | setUserid(int userid) |
| `Name` | `String` | Optional | Specific preference name to retrieve. Omit to retrieve all preferences. | String getName() | setName(String name) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import java.io.IOException;
import m18000.m0.m0.m127.ApiHelper;
import m18000.m0.m0.m127.models.GetUserPreferencesRequest;

GetUserPreferencesRequest getUserPreferencesRequest = new GetUserPreferencesRequest.Builder(
    123456
)
.name("name6")
.additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
.build();
```



