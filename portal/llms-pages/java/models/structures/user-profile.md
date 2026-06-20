# User Profile

Source: /#/java/x-redirect/JTI0bSUyRlVzZXJQcm9maWxl

Complete user profile.

*This model accepts additional fields of type Object.*


# Class Name

`UserProfile`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Id` | `int` | Required | Unique numeric user identifier. | int getId() | setId(int id) |
| `Username` | `String` | Required | Login username for the user. | String getUsername() | setUsername(String username) |
| `Fullname` | `String` | Required | Full display name of the user. | String getFullname() | setFullname(String fullname) |
| `Email` | `String` | Required | Email address of the user. | String getEmail() | setEmail(String email) |
| `Department` | `String` | Required | Department the user belongs to within the institution. | String getDepartment() | setDepartment(String department) |
| `Institution` | `String` | Required | Name of the institution the user is affiliated with. | String getInstitution() | setInstitution(String institution) |
| `Idnumber` | `String` | Required | Institution-assigned student or staff ID number. | String getIdnumber() | setIdnumber(String idnumber) |
| `Auth` | `String` | Required | Authentication method used by the user (e.g., 'ldap', 'manual'). | String getAuth() | setAuth(String auth) |
| `Confirmed` | `boolean` | Required | Whether the user's account has been confirmed. | boolean getConfirmed() | setConfirmed(boolean confirmed) |
| `Lang` | `String` | Required | Preferred interface language code (e.g., 'en'). | String getLang() | setLang(String lang) |
| `Theme` | `String` | Required | Preferred LMS theme; empty string means use the site default. | String getTheme() | setTheme(String theme) |
| `Timezone` | `String` | Required | Timezone identifier. "99" means use the server default. | String getTimezone() | setTimezone(String timezone) |
| `Mailformat` | `int` | Required | Email format preference (1 = HTML). | int getMailformat() | setMailformat(int mailformat) |
| `Profileimageurlsmall` | `String` | Required | URL to the user's small profile image (thumbnail). | String getProfileimageurlsmall() | setProfileimageurlsmall(String profileimageurlsmall) |
| `Profileimageurl` | `String` | Required | URL to the user's full-size profile image. | String getProfileimageurl() | setProfileimageurl(String profileimageurl) |
| `Customfields` | [`List<CustomField>`](/llms-pages/java/models/structures/custom-field.md) | Optional | List of custom profile field values for the user. | List<CustomField> getCustomfields() | setCustomfields(List<CustomField> customfields) |
| `Preferences` | [`List<UserPreference>`](/llms-pages/java/models/structures/user-preference.md) | Optional | List of stored preference key/value pairs for the user. | List<UserPreference> getPreferences() | setPreferences(List<UserPreference> preferences) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import java.io.IOException;
import java.util.Arrays;
import m18000.m0.m0.m127.ApiHelper;
import m18000.m0.m0.m127.models.CustomField;
import m18000.m0.m0.m127.models.UserPreference;
import m18000.m0.m0.m127.models.UserProfile;

UserProfile userProfile = new UserProfile.Builder(
    123456,
    "johndoe.bscs23seecs",
    "John Doe",
    "johndoe.bscs23seecs@seecs.edu.pk",
    "FoC",
    "SEECS",
    "00000454987",
    "ldap",
    true,
    "en",
    null,
    "99",
    1,
    "https://lms.nust.edu.pk/portal/pluginfile.php/1583361/user/icon/moove/f2?rev=14452894",
    "https://lms.nust.edu.pk/portal/pluginfile.php/1583361/user/icon/moove/f1?rev=14452894"
)
.customfields(Arrays.asList(
        new CustomField.Builder(
            "type8",
            "value4",
            "name2",
            "shortname4"
        )
        .additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
        .build(),
        new CustomField.Builder(
            "type8",
            "value4",
            "name2",
            "shortname4"
        )
        .additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
        .build()
    ))
.preferences(Arrays.asList(
        new UserPreference.Builder(
            "name8",
            "value0"
        )
        .additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
        .build()
    ))
.additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
.build();
```



