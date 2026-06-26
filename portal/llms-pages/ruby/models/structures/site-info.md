# Site Info

Source: /#/ruby/x-redirect/JTI0bSUyRlNpdGVJbmZv

Your identity plus basic site information, from Moodle's site-info call. The `userid` here is what other endpoints need (e.g. it is the `useridto` for popup notifications).

*This model accepts additional fields of type Object.*


# Class Name

`SiteInfo`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `userid` | `Integer` | Required | Your numeric Moodle user ID. |
| `username` | `String` | Required | Your login username. |
| `firstname` | `String` | Optional | Your first name. |
| `lastname` | `String` | Optional | Your last name. |
| `fullname` | `String` | Required | Your full display name. |
| `userpictureurl` | `String` | Optional | URL of your profile picture. |
| `lang` | `String` | Optional | Your preferred interface language code. |
| `sitename` | `String` | Required | Name of the LMS site. |
| `siteurl` | `String` | Optional | Base URL of the LMS site. |
| `release` | `String` | Optional | Moodle release/version string of the site. |
| `additional_properties` | `Hash[String, Object]` | Optional | - |


# Example

```ruby
site_info = SiteInfo.new(
  userid: 234567,
  username: 'johndoe.bscs23seecs',
  fullname: 'John Doe',
  sitename: 'NUST LMS',
  firstname: 'John',
  lastname: 'Doe',
  userpictureurl: 'https://lms.nust.edu.pk/portal/pluginfile.php/1583361/user/icon/moove/f1',
  lang: 'en',
  siteurl: 'https://lms.nust.edu.pk/portal',
  release: '4.1.2',
  additional_properties: {
    'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
  }
)
```



