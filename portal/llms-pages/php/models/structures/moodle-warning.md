# Moodle Warning

Source: /#/php/x-redirect/JTI0bSUyRk1vb2RsZVdhcm5pbmc

A non-fatal warning returned alongside a successful response.

*This model accepts additional fields of type array.*


# Class Name

`MoodleWarning`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `item` | `?string` | Optional | Item identifier related to the warning; empty string if not applicable. | getItem(): ?string | setItem(?string item): void |
| `itemid` | `?int` | Optional | Numeric item ID related to the warning; 0 if not applicable. | getItemid(): ?int | setItemid(?int itemid): void |
| `warningcode` | `?string` | Optional | Machine-readable warning code; empty string if no code. | getWarningcode(): ?string | setWarningcode(?string warningcode): void |
| `message` | `?string` | Optional | Human-readable warning description. | getMessage(): ?string | setMessage(?string message): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |


# Example

```php
use NustLmsApiLib\Models\Builders\MoodleWarningBuilder;
use NustLmsApiLib\ApiHelper;

$moodleWarning = MoodleWarningBuilder::init()
    ->item('item6')
    ->itemid(0)
    ->warningcode('warningcode6')
    ->message('message4')
    ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
    ->build();
```



