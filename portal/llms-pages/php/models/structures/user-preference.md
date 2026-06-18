# User Preference

Source: /#/php/x-redirect/JTI0bSUyRlVzZXJQcmVmZXJlbmNl

A single user preference setting.

*This model accepts additional fields of type array.*


# Class Name

`UserPreference`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `name` | `string` | Required | Unique key identifying the preference. | getName(): string | setName(string name): void |
| `value` | `string` | Required | Preference value as a string. Note that the internal _lastloaded preference is returned as an integer by the LMS. | getValue(): string | setValue(string value): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |


# Example

```php
use NustLmsApiLib\Models\Builders\UserPreferenceBuilder;
use NustLmsApiLib\ApiHelper;

$userPreference = UserPreferenceBuilder::init(
    'block_myoverview_user_sort_preference',
    'title'
)
    ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
    ->build();
```



