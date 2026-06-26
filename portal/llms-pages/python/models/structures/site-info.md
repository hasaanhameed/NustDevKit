# Site Info

Source: /#/python/x-redirect/JTI0bSUyRlNpdGVJbmZv

Your identity plus basic site information, from Moodle's site-info call. The `userid` here is what other endpoints need (e.g. it is the `useridto` for popup notifications).

*This model accepts additional fields of type Any.*


# Class Name

`SiteInfo`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `userid` | `int` | Required | Your numeric Moodle user ID. |
| `username` | `str` | Required | Your login username. |
| `firstname` | `str` | Optional | Your first name. |
| `lastname` | `str` | Optional | Your last name. |
| `fullname` | `str` | Required | Your full display name. |
| `userpictureurl` | `str` | Optional | URL of your profile picture. |
| `lang` | `str` | Optional | Your preferred interface language code. |
| `sitename` | `str` | Required | Name of the LMS site. |
| `siteurl` | `str` | Optional | Base URL of the LMS site. |
| `release` | `str` | Optional | Moodle release/version string of the site. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |


# Example

```python
import jsonpickle

from nustlmsapi.models.site_info import SiteInfo

site_info = SiteInfo(
    userid=234567,
    username='johndoe.bscs23seecs',
    fullname='John Doe',
    sitename='NUST LMS',
    firstname='John',
    lastname='Doe',
    userpictureurl='https://lms.nust.edu.pk/portal/pluginfile.php/1583361/user/icon/moove/f1',
    lang='en',
    siteurl='https://lms.nust.edu.pk/portal',
    release='4.1.2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```



