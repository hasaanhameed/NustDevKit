# User Profile

Source: /#/go/x-redirect/JTI0bSUyRlVzZXJQcm9maWxl

Complete user profile.

*This model accepts additional fields of type interface{}.*


# Class Name

`UserProfile`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Id` | `int` | Required | Unique numeric user identifier. |
| `Username` | `string` | Required | Login username for the user. |
| `Fullname` | `string` | Required | Full display name of the user. |
| `Email` | `string` | Required | Email address of the user. |
| `Department` | `string` | Required | Department the user belongs to within the institution. |
| `Institution` | `string` | Required | Name of the institution the user is affiliated with. |
| `Idnumber` | `string` | Required | Institution-assigned student or staff ID number. |
| `Auth` | `string` | Required | Authentication method used by the user (e.g., 'ldap', 'manual'). |
| `Confirmed` | `bool` | Required | Whether the user's account has been confirmed. |
| `Lang` | `string` | Required | Preferred interface language code (e.g., 'en'). |
| `Theme` | `string` | Required | Preferred LMS theme; empty string means use the site default. |
| `Timezone` | `string` | Required | Timezone identifier. "99" means use the server default. |
| `Mailformat` | `int` | Required | Email format preference (1 = HTML). |
| `Profileimageurlsmall` | `string` | Required | URL to the user's small profile image (thumbnail). |
| `Profileimageurl` | `string` | Required | URL to the user's full-size profile image. |
| `Customfields` | [`[]models.CustomField`](/llms-pages/go/models/structures/custom-field.md) | Optional | List of custom profile field values for the user. |
| `Preferences` | [`[]models.UserPreference`](/llms-pages/go/models/structures/user-preference.md) | Optional | List of stored preference key/value pairs for the user. |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
package main

import (
    "nustLmsApi/models"
)

func main() {
    userProfile := models.UserProfile{
        Id:                    123456,
        Username:              "johndoe.bscs23seecs",
        Fullname:              "John Doe",
        Email:                 "johndoe.bscs23seecs@seecs.edu.pk",
        Department:            "FoC",
        Institution:           "SEECS",
        Idnumber:              "00000454987",
        Auth:                  "ldap",
        Confirmed:             true,
        Lang:                  "en",
        Theme:                 "",
        Timezone:              "99",
        Mailformat:            1,
        Profileimageurlsmall:  "https://lms.nust.edu.pk/portal/pluginfile.php/1583361/user/icon/moove/f2?rev=14452894",
        Profileimageurl:       "https://lms.nust.edu.pk/portal/pluginfile.php/1583361/user/icon/moove/f1?rev=14452894",
        Customfields:          []models.CustomField{
            models.CustomField{
                Type:                  "type8",
                Value:                 "value4",
                Name:                  "name2",
                Shortname:             "shortname4",
                AdditionalProperties:  map[string]interface{}{
                    "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
                },
            },
            models.CustomField{
                Type:                  "type8",
                Value:                 "value4",
                Name:                  "name2",
                Shortname:             "shortname4",
                AdditionalProperties:  map[string]interface{}{
                    "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
                },
            },
        },
        Preferences:           []models.UserPreference{
            models.UserPreference{
                Name:                  "name8",
                Value:                 "value0",
                AdditionalProperties:  map[string]interface{}{
                    "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
                },
            },
        },
        AdditionalProperties:  map[string]interface{}{
            "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
        },
    }

}
```



