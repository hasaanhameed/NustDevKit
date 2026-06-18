# Event Subscription

Source: /#/php/x-redirect/JTI0bSUyRkV2ZW50U3Vic2NyaXB0aW9u

Subscription display settings for a calendar event.

*This model accepts additional fields of type array.*


# Class Name

`EventSubscription`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `displayeventsource` | `bool` | Required | Whether to display the event source label on the calendar. | getDisplayeventsource(): bool | setDisplayeventsource(bool displayeventsource): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |


# Example

```php
use NustLmsApiLib\Models\Builders\EventSubscriptionBuilder;
use NustLmsApiLib\ApiHelper;

$eventSubscription = EventSubscriptionBuilder::init(
    false
)
    ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
    ->build();
```



