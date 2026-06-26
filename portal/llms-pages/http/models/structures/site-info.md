# Site Info

Source: /#/http/x-redirect/JTI0bSUyRlNpdGVJbmZv

Your identity plus basic site information, from Moodle's site-info call. The `userid` here is what other endpoints need (e.g. it is the `useridto` for popup notifications).

*This model accepts additional fields of type Object.*


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `userid` | `Number` | Required | Your numeric Moodle user ID. |
| `username` | `String` | Required | Your login username. |
| `firstname` | `String` | Optional | Your first name. |
| `lastname` | `String` | Optional | Your last name. |
| `fullname` | `String` | Required | Your full display name. |
| `userpictureurl` | `String` | Optional | URL of your profile picture. |
| `lang` | `String` | Optional | Your preferred interface language code. |
| `sitename` | `String` | Required | Name of the LMS site. |
| `siteurl` | `String` | Optional | Base URL of the LMS site. |
| `release` | `String` | Optional | Moodle release/version string of the site. |
| `additionalProperties` | `Object` | Optional | - |


# Example (as JSON)

```json
{
  "userid": 234567,
  "username": "johndoe.bscs23seecs",
  "firstname": "John",
  "lastname": "Doe",
  "fullname": "John Doe",
  "userpictureurl": "https://lms.nust.edu.pk/portal/pluginfile.php/1583361/user/icon/moove/f1",
  "lang": "en",
  "sitename": "NUST LMS",
  "siteurl": "https://lms.nust.edu.pk/portal",
  "release": "4.1.2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```



