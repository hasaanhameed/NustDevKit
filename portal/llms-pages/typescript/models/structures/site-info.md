# Site Info

Source: /#/typescript/x-redirect/JTI0bSUyRlNpdGVJbmZv

Your identity plus basic site information, from Moodle's site-info call. The `userid` here is what other endpoints need (e.g. it is the `useridto` for popup notifications).

*This model accepts additional fields of type unknown.*


# Interface Name

`SiteInfo`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `userid` | `number` | Required | Your numeric Moodle user ID. |
| `username` | `string` | Required | Your login username. |
| `firstname` | `string \| undefined` | Optional | Your first name. |
| `lastname` | `string \| undefined` | Optional | Your last name. |
| `fullname` | `string` | Required | Your full display name. |
| `userpictureurl` | `string \| undefined` | Optional | URL of your profile picture. |
| `lang` | `string \| undefined` | Optional | Your preferred interface language code. |
| `sitename` | `string` | Required | Name of the LMS site. |
| `siteurl` | `string \| undefined` | Optional | Base URL of the LMS site. |
| `release` | `string \| undefined` | Optional | Moodle release/version string of the site. |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
import { SiteInfo } from 'nust-lms-apilib';

const siteInfo: SiteInfo = {
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
  additionalProperties: {
    'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
  },
};
```



