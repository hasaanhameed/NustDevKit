# User Preference

Source: /#/java/x-redirect/JTI0bSUyRlVzZXJQcmVmZXJlbmNl

A single user preference setting.

*This model accepts additional fields of type Object.*


# Class Name

`UserPreference`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Name` | `String` | Required | Unique key identifying the preference. | String getName() | setName(String name) |
| `Value` | `String` | Required | Preference value as a string. Note that the internal _lastloaded preference is returned as an integer by the LMS. | String getValue() | setValue(String value) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import java.io.IOException;
import m18000.m0.m0.m127.ApiHelper;
import m18000.m0.m0.m127.models.UserPreference;

UserPreference userPreference = new UserPreference.Builder(
    "block_myoverview_user_sort_preference",
    "title"
)
.additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
.build();
```



