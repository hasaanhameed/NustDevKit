# User Profile

Source: /#/php/x-redirect/JTI0bSUyRlVzZXJQcm9maWxl

Complete user profile.

*This model accepts additional fields of type array.*


# Class Name

`UserProfile`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `id` | `int` | Required | Unique numeric user identifier. | getId(): int | setId(int id): void |
| `username` | `string` | Required | Login username for the user. | getUsername(): string | setUsername(string username): void |
| `fullname` | `string` | Required | Full display name of the user. | getFullname(): string | setFullname(string fullname): void |
| `email` | `string` | Required | Email address of the user. | getEmail(): string | setEmail(string email): void |
| `department` | `string` | Required | Department the user belongs to within the institution. | getDepartment(): string | setDepartment(string department): void |
| `institution` | `string` | Required | Name of the institution the user is affiliated with. | getInstitution(): string | setInstitution(string institution): void |
| `idnumber` | `string` | Required | Institution-assigned student or staff ID number. | getIdnumber(): string | setIdnumber(string idnumber): void |
| `auth` | `string` | Required | Authentication method used by the user (e.g., 'ldap', 'manual'). | getAuth(): string | setAuth(string auth): void |
| `confirmed` | `bool` | Required | Whether the user's account has been confirmed. | getConfirmed(): bool | setConfirmed(bool confirmed): void |
| `lang` | `string` | Required | Preferred interface language code (e.g., 'en'). | getLang(): string | setLang(string lang): void |
| `theme` | `string` | Required | Preferred LMS theme; empty string means use the site default. | getTheme(): string | setTheme(string theme): void |
| `timezone` | `string` | Required | Timezone identifier. "99" means use the server default. | getTimezone(): string | setTimezone(string timezone): void |
| `mailformat` | `int` | Required | Email format preference (1 = HTML). | getMailformat(): int | setMailformat(int mailformat): void |
| `profileimageurlsmall` | `string` | Required | URL to the user's small profile image (thumbnail). | getProfileimageurlsmall(): string | setProfileimageurlsmall(string profileimageurlsmall): void |
| `profileimageurl` | `string` | Required | URL to the user's full-size profile image. | getProfileimageurl(): string | setProfileimageurl(string profileimageurl): void |
| `customfields` | [`?(CustomField[])`](/llms-pages/php/models/structures/custom-field.md) | Optional | List of custom profile field values for the user. | getCustomfields(): ?array | setCustomfields(?array customfields): void |
| `preferences` | [`?(UserPreference[])`](/llms-pages/php/models/structures/user-preference.md) | Optional | List of stored preference key/value pairs for the user. | getPreferences(): ?array | setPreferences(?array preferences): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |


# Example

```php
use NustLmsApiLib\Models\Builders\UserProfileBuilder;
use NustLmsApiLib\Models\Builders\CustomFieldBuilder;
use NustLmsApiLib\ApiHelper;
use NustLmsApiLib\Models\Builders\UserPreferenceBuilder;

$userProfile = UserProfileBuilder::init(
    123456,
    'johndoe.bscs23seecs',
    'John Doe',
    'johndoe.bscs23seecs@seecs.edu.pk',
    'FoC',
    'SEECS',
    '00000454987',
    'ldap',
    true,
    'en',
    '',
    '99',
    1,
    'https://lms.nust.edu.pk/portal/pluginfile.php/1583361/user/icon/moove/f2?rev=14452894',
    'https://lms.nust.edu.pk/portal/pluginfile.php/1583361/user/icon/moove/f1?rev=14452894'
)
    ->customfields(
        [
            CustomFieldBuilder::init(
                'type8',
                'value4',
                'name2',
                'shortname4'
            )
                ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
                ->build(),
            CustomFieldBuilder::init(
                'type8',
                'value4',
                'name2',
                'shortname4'
            )
                ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
                ->build()
        ]
    )
    ->preferences(
        [
            UserPreferenceBuilder::init(
                'name8',
                'value0'
            )
                ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
                ->build()
        ]
    )
    ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
    ->build();
```



