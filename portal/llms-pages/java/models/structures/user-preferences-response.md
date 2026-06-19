# User Preferences Response

Source: /#/java/x-redirect/JTI0bSUyRlVzZXJQcmVmZXJlbmNlc1Jlc3BvbnNl

Response envelope for the user-preferences endpoint.

*This model accepts additional fields of type Object.*


# Class Name

`UserPreferencesResponse`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Preferences` | [`List<UserPreference>`](/llms-pages/java/models/structures/user-preference.md) | Required | List of user preference key/value pairs. | List<UserPreference> getPreferences() | setPreferences(List<UserPreference> preferences) |
| `Warnings` | [`List<MoodleWarning>`](/llms-pages/java/models/structures/moodle-warning.md) | Required | Array of warning objects. Empty when no warnings are present. | List<MoodleWarning> getWarnings() | setWarnings(List<MoodleWarning> warnings) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import java.io.IOException;
import java.util.Arrays;
import m18000.m0.m0.m127.ApiHelper;
import m18000.m0.m0.m127.models.MoodleWarning;
import m18000.m0.m0.m127.models.UserPreference;
import m18000.m0.m0.m127.models.UserPreferencesResponse;

UserPreferencesResponse userPreferencesResponse = new UserPreferencesResponse.Builder(
    Arrays.asList(
        new UserPreference.Builder(
            "block_myoverview_user_sort_preference",
            "title"
        )
        .additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
        .build()
    ),
    Arrays.asList(
        new MoodleWarning.Builder()
            .item("item6")
            .itemid(0)
            .warningcode("warningcode4")
            .message("message4")
        .additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
            .build()
    )
)
.additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
.build();
```



