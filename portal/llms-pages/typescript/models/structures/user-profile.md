# User Profile

Source: /#/typescript/x-redirect/JTI0bSUyRlVzZXJQcm9maWxl

Complete user profile.

*This model accepts additional fields of type unknown.*


# Interface Name

`UserProfile`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `number` | Required | Unique numeric user identifier. |
| `username` | `string` | Required | Login username for the user. |
| `fullname` | `string` | Required | Full display name of the user. |
| `email` | `string` | Required | Email address of the user. |
| `department` | `string` | Required | Department the user belongs to within the institution. |
| `institution` | `string` | Required | Name of the institution the user is affiliated with. |
| `idnumber` | `string` | Required | Institution-assigned student or staff ID number. |
| `auth` | `string` | Required | Authentication method used by the user (e.g., 'ldap', 'manual'). |
| `confirmed` | `boolean` | Required | Whether the user's account has been confirmed. |
| `lang` | `string` | Required | Preferred interface language code (e.g., 'en'). |
| `theme` | `string` | Required | Preferred LMS theme; empty string means use the site default. |
| `timezone` | `string` | Required | Timezone identifier. "99" means use the server default. |
| `mailformat` | `number` | Required | Email format preference (1 = HTML). |
| `profileimageurlsmall` | `string` | Required | URL to the user's small profile image (thumbnail). |
| `profileimageurl` | `string` | Required | URL to the user's full-size profile image. |
| `customfields` | [`CustomField[] \| undefined`](/llms-pages/typescript/models/structures/custom-field.md) | Optional | List of custom profile field values for the user. |
| `preferences` | [`UserPreference[] \| undefined`](/llms-pages/typescript/models/structures/user-preference.md) | Optional | List of stored preference key/value pairs for the user. |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
import { UserProfile } from 'nust-lms-apilib';

const userProfile: UserProfile = {
  id: 162154,
  username: 'hhameed.bscs23seecs',
  fullname: 'Hasaan Hameed',
  email: 'hhameed.bscs23seecs@seecs.edu.pk',
  department: 'FoC',
  institution: 'SEECS',
  idnumber: '00000454987',
  auth: 'ldap',
  confirmed: true,
  lang: 'en',
  theme: '',
  timezone: '99',
  mailformat: 1,
  profileimageurlsmall: 'https://lms.nust.edu.pk/portal/pluginfile.php/1583361/user/icon/moove/f2?rev=14452894',
  profileimageurl: 'https://lms.nust.edu.pk/portal/pluginfile.php/1583361/user/icon/moove/f1?rev=14452894',
  customfields: [
    {
      type: 'type8',
      value: 'value4',
      name: 'name2',
      shortname: 'shortname4',
      additionalProperties: {
        'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
      },
    },
    {
      type: 'type8',
      value: 'value4',
      name: 'name2',
      shortname: 'shortname4',
      additionalProperties: {
        'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
      },
    }
  ],
  preferences: [
    {
      name: 'name8',
      value: 'value0',
      additionalProperties: {
        'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
      },
    }
  ],
  additionalProperties: {
    'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
  },
};
```



