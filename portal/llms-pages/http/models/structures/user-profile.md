# User Profile

Source: /#/http/x-redirect/JTI0bSUyRlVzZXJQcm9maWxl

Complete user profile.

*This model accepts additional fields of type Object.*


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `Number` | Required | Unique numeric user identifier. |
| `username` | `String` | Required | Login username for the user. |
| `fullname` | `String` | Required | Full display name of the user. |
| `email` | `String` | Required | Email address of the user. |
| `department` | `String` | Required | Department the user belongs to within the institution. |
| `institution` | `String` | Required | Name of the institution the user is affiliated with. |
| `idnumber` | `String` | Required | Institution-assigned student or staff ID number. |
| `auth` | `String` | Required | Authentication method used by the user (e.g., 'ldap', 'manual'). |
| `confirmed` | `Boolean` | Required | Whether the user's account has been confirmed. |
| `lang` | `String` | Required | Preferred interface language code (e.g., 'en'). |
| `theme` | `String` | Required | Preferred LMS theme; empty string means use the site default. |
| `timezone` | `String` | Required | Timezone identifier. "99" means use the server default. |
| `mailformat` | `Number` | Required | Email format preference (1 = HTML). |
| `profileimageurlsmall` | `String` | Required | URL to the user's small profile image (thumbnail). |
| `profileimageurl` | `String` | Required | URL to the user's full-size profile image. |
| `customfields` | [`array<Custom Field>`](/llms-pages/http/models/structures/custom-field.md) | Optional | List of custom profile field values for the user. |
| `preferences` | [`array<User Preference>`](/llms-pages/http/models/structures/user-preference.md) | Optional | List of stored preference key/value pairs for the user. |
| `additionalProperties` | `Object` | Optional | - |


# Example (as JSON)

```json
{
  "id": 162154,
  "username": "hhameed.bscs23seecs",
  "fullname": "Hasaan Hameed",
  "email": "hhameed.bscs23seecs@seecs.edu.pk",
  "department": "FoC",
  "institution": "SEECS",
  "idnumber": "00000454987",
  "auth": "ldap",
  "confirmed": true,
  "lang": "en",
  "theme": null,
  "timezone": "99",
  "mailformat": 1,
  "profileimageurlsmall": "https://lms.nust.edu.pk/portal/pluginfile.php/1583361/user/icon/moove/f2?rev=14452894",
  "profileimageurl": "https://lms.nust.edu.pk/portal/pluginfile.php/1583361/user/icon/moove/f1?rev=14452894",
  "customfields": [
    {
      "type": "type8",
      "value": "value4",
      "name": "name2",
      "shortname": "shortname4",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    {
      "type": "type8",
      "value": "value4",
      "name": "name2",
      "shortname": "shortname4",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "preferences": [
    {
      "name": "name8",
      "value": "value0",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    {
      "name": "name8",
      "value": "value0",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    {
      "name": "name8",
      "value": "value0",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```



