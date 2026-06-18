# Event Action

Source: /#/php/x-redirect/JTI0bSUyRkV2ZW50QWN0aW9u

Primary action button metadata for a calendar event.

*This model accepts additional fields of type array.*


# Class Name

`EventAction`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `name` | `string` | Required | Display label for the primary action button. | getName(): string | setName(string name): void |
| `url` | `string` | Required | URL the user should navigate to in order to perform the action. | getUrl(): string | setUrl(string url): void |
| `itemcount` | `int` | Required | Number of items associated with this action. | getItemcount(): int | setItemcount(int itemcount): void |
| `actionable` | `bool` | Required | Whether the action can currently be taken by the user. | getActionable(): bool | setActionable(bool actionable): void |
| `showitemcount` | `bool` | Required | Whether to display the item count alongside the action label. | getShowitemcount(): bool | setShowitemcount(bool showitemcount): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |


# Example

```php
use NustLmsApiLib\Models\Builders\EventActionBuilder;
use NustLmsApiLib\ApiHelper;

$eventAction = EventActionBuilder::init(
    'Add submission',
    'https://lms.nust.edu.pk/portal/mod/assign/view.php?id=999404&action=editsubmission',
    1,
    true,
    false
)
    ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
    ->build();
```



