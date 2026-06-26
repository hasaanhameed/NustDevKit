# Site Info

Source: /#/java/x-redirect/JTI0bSUyRlNpdGVJbmZv

Your identity plus basic site information, from Moodle's site-info call. The `userid` here is what other endpoints need (e.g. it is the `useridto` for popup notifications).

*This model accepts additional fields of type Object.*


# Class Name

`SiteInfo`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Userid` | `int` | Required | Your numeric Moodle user ID. | int getUserid() | setUserid(int userid) |
| `Username` | `String` | Required | Your login username. | String getUsername() | setUsername(String username) |
| `Firstname` | `String` | Optional | Your first name. | String getFirstname() | setFirstname(String firstname) |
| `Lastname` | `String` | Optional | Your last name. | String getLastname() | setLastname(String lastname) |
| `Fullname` | `String` | Required | Your full display name. | String getFullname() | setFullname(String fullname) |
| `Userpictureurl` | `String` | Optional | URL of your profile picture. | String getUserpictureurl() | setUserpictureurl(String userpictureurl) |
| `Lang` | `String` | Optional | Your preferred interface language code. | String getLang() | setLang(String lang) |
| `Sitename` | `String` | Required | Name of the LMS site. | String getSitename() | setSitename(String sitename) |
| `Siteurl` | `String` | Optional | Base URL of the LMS site. | String getSiteurl() | setSiteurl(String siteurl) |
| `Release` | `String` | Optional | Moodle release/version string of the site. | String getRelease() | setRelease(String release) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import java.io.IOException;
import m18000.m0.m0.m127.ApiHelper;
import m18000.m0.m0.m127.models.SiteInfo;

SiteInfo siteInfo = new SiteInfo.Builder(
    234567,
    "johndoe.bscs23seecs",
    "John Doe",
    "NUST LMS"
)
.firstname("John")
.lastname("Doe")
.userpictureurl("https://lms.nust.edu.pk/portal/pluginfile.php/1583361/user/icon/moove/f1")
.lang("en")
.siteurl("https://lms.nust.edu.pk/portal")
.release("4.1.2")
.additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
.build();
```



