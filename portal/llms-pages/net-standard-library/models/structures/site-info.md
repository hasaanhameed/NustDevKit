# Site Info

Source: /#/net-standard-library/x-redirect/JTI0bSUyRlNpdGVJbmZv

Your identity plus basic site information, from Moodle's site-info call. The `userid` here is what other endpoints need (e.g. it is the `useridto` for popup notifications).

*This model accepts additional fields of type object.*


# Class Name

`SiteInfo`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Userid` | `int` | Required | Your numeric Moodle user ID. |
| `Username` | `string` | Required | Your login username. |
| `Firstname` | `string` | Optional | Your first name. |
| `Lastname` | `string` | Optional | Your last name. |
| `Fullname` | `string` | Required | Your full display name. |
| `Userpictureurl` | `string` | Optional | URL of your profile picture. |
| `Lang` | `string` | Optional | Your preferred interface language code. |
| `Sitename` | `string` | Required | Name of the LMS site. |
| `Siteurl` | `string` | Optional | Base URL of the LMS site. |
| `Release` | `string` | Optional | Moodle release/version string of the site. |
| `AdditionalProperties` | `object this[string key]` | Optional | - |


# Example

```csharp
using NustLmsApi.Standard.Models;
using NustLmsApi.Standard.Utilities;

SiteInfo siteInfo = new SiteInfo
{
    Userid = 234567,
    Username = "johndoe.bscs23seecs",
    Fullname = "John Doe",
    Sitename = "NUST LMS",
    Firstname = "John",
    Lastname = "Doe",
    Userpictureurl = "https://lms.nust.edu.pk/portal/pluginfile.php/1583361/user/icon/moove/f1",
    Lang = "en",
    Siteurl = "https://lms.nust.edu.pk/portal",
    Release = "4.1.2",
    ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
};
```



