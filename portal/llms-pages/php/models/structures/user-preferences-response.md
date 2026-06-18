# User Preferences Response

Source: /#/php/x-redirect/JTI0bSUyRlVzZXJQcmVmZXJlbmNlc1Jlc3BvbnNl

Response envelope for the user-preferences endpoint.

*This model accepts additional fields of type array.*


# Class Name

`UserPreferencesResponse`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `preferences` | [`UserPreference[]`](/llms-pages/php/models/structures/user-preference.md) | Required | List of user preference key/value pairs. | getPreferences(): array | setPreferences(array preferences): void |
| `warnings` | [`MoodleWarning[]`](/llms-pages/php/models/structures/moodle-warning.md) | Required | Array of warning objects. Empty when no warnings are present. | getWarnings(): array | setWarnings(array warnings): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |


# Example

```php
use NustLmsApiLib\Models\Builders\UserPreferencesResponseBuilder;
use NustLmsApiLib\Models\Builders\UserPreferenceBuilder;
use NustLmsApiLib\ApiHelper;
use NustLmsApiLib\Models\Builders\MoodleWarningBuilder;

$userPreferencesResponse = UserPreferencesResponseBuilder::init(
    [
        UserPreferenceBuilder::init(
            'block_myoverview_user_sort_preference',
            'title'
        )
            ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
            ->build()
    ],
    [
        MoodleWarningBuilder::init()
            ->item('item6')
            ->itemid(0)
            ->warningcode('warningcode4')
            ->message('message4')
            ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
            ->build()
    ]
)
    ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
    ->build();
```



