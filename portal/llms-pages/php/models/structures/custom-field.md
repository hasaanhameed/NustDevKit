# Custom Field

Source: /#/php/x-redirect/JTI0bSUyRkN1c3RvbUZpZWxk

A custom profile field value attached to a user.

*This model accepts additional fields of type array.*


# Class Name

`CustomField`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `type` | `string` | Required | Data type of the custom field (e.g., 'text', 'select'). | getType(): string | setType(string type): void |
| `value` | `string` | Required | Value stored in the custom field. | getValue(): string | setValue(string value): void |
| `name` | `string` | Required | Display label of the custom field. | getName(): string | setName(string name): void |
| `shortname` | `string` | Required | Machine-readable shortname identifier for the custom field. | getShortname(): string | setShortname(string shortname): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |


# Example

```php
use NustLmsApiLib\Models\Builders\CustomFieldBuilder;
use NustLmsApiLib\ApiHelper;

$customField = CustomFieldBuilder::init(
    'text',
    'SEECS',
    'Institute',
    'institution'
)
    ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
    ->build();
```



