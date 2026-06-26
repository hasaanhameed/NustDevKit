# Site Info

Source: /#/php/x-redirect/JTI0bSUyRlNpdGVJbmZv

Your identity plus basic site information, from Moodle's site-info call. The `userid` here is what other endpoints need (e.g. it is the `useridto` for popup notifications).

*This model accepts additional fields of type array.*


# Class Name

`SiteInfo`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `userid` | `int` | Required | Your numeric Moodle user ID. | getUserid(): int | setUserid(int userid): void |
| `username` | `string` | Required | Your login username. | getUsername(): string | setUsername(string username): void |
| `firstname` | `?string` | Optional | Your first name. | getFirstname(): ?string | setFirstname(?string firstname): void |
| `lastname` | `?string` | Optional | Your last name. | getLastname(): ?string | setLastname(?string lastname): void |
| `fullname` | `string` | Required | Your full display name. | getFullname(): string | setFullname(string fullname): void |
| `userpictureurl` | `?string` | Optional | URL of your profile picture. | getUserpictureurl(): ?string | setUserpictureurl(?string userpictureurl): void |
| `lang` | `?string` | Optional | Your preferred interface language code. | getLang(): ?string | setLang(?string lang): void |
| `sitename` | `string` | Required | Name of the LMS site. | getSitename(): string | setSitename(string sitename): void |
| `siteurl` | `?string` | Optional | Base URL of the LMS site. | getSiteurl(): ?string | setSiteurl(?string siteurl): void |
| `release` | `?string` | Optional | Moodle release/version string of the site. | getRelease(): ?string | setRelease(?string release): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |


# Example

```php
use NustLmsApiLib\Models\Builders\SiteInfoBuilder;
use NustLmsApiLib\ApiHelper;

$siteInfo = SiteInfoBuilder::init(
    234567,
    'johndoe.bscs23seecs',
    'John Doe',
    'NUST LMS'
)
    ->firstname('John')
    ->lastname('Doe')
    ->userpictureurl('https://lms.nust.edu.pk/portal/pluginfile.php/1583361/user/icon/moove/f1')
    ->lang('en')
    ->siteurl('https://lms.nust.edu.pk/portal')
    ->release('4.1.2')
    ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
    ->build();
```



