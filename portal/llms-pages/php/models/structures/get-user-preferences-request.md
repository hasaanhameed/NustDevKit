# Get User Preferences Request

Source: /#/php/x-redirect/JTI0bSUyRkdldFVzZXJQcmVmZXJlbmNlc1JlcXVlc3Q

Request parameters for retrieving user preferences.

*This model accepts additional fields of type array.*


# Class Name

`GetUserPreferencesRequest`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `userid` | `int` | Required | ID of the user whose preferences to retrieve. | getUserid(): int | setUserid(int userid): void |
| `name` | `?string` | Optional | Specific preference name to retrieve. Omit to retrieve all preferences. | getName(): ?string | setName(?string name): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |


# Example

```php
use NustLmsApiLib\Models\Builders\GetUserPreferencesRequestBuilder;
use NustLmsApiLib\ApiHelper;

$getUserPreferencesRequest = GetUserPreferencesRequestBuilder::init(
    162154
)
    ->name('name6')
    ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
    ->build();
```



