# Get Users by Field Request

Source: /#/php/x-redirect/JTI0bSUyRkdldFVzZXJzQnlGaWVsZFJlcXVlc3Q

Request parameters for retrieving user profiles by a profile field value.

*This model accepts additional fields of type array.*


# Class Name

`GetUsersByFieldRequest`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `field` | [`string(UserProfileField)`](/llms-pages/php/models/enumerations/user-profile-field.md) | Required | User profile field to match against when searching for users. | getField(): string | setField(string field): void |
| `values` | `string[]` | Required | List of field values to look up. All values must be provided as strings even when the field is numeric (e.g., "162154" for an integer ID). | getValues(): array | setValues(array values): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |


# Example

```php
use NustLmsApiLib\Models\Builders\GetUsersByFieldRequestBuilder;
use NustLmsApiLib\Models\UserProfileField;
use NustLmsApiLib\ApiHelper;

$getUsersByFieldRequest = GetUsersByFieldRequestBuilder::init(
    UserProfileField::ID,
    [
        '162154'
    ]
)
    ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
    ->build();
```



