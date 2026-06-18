# Site Notification

Source: /#/php/x-redirect/JTI0bSUyRlNpdGVOb3RpZmljYXRpb24

A site-level notification (structure varies by type).

*This model accepts additional fields of type array.*


# Class Name

`SiteNotification`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `id` | `?int` | Optional | Unique identifier for the site notification. | getId(): ?int | setId(?int id): void |
| `message` | `?string` | Optional | Notification message content. | getMessage(): ?string | setMessage(?string message): void |
| `type` | `?string` | Optional | Notification type identifier. | getType(): ?string | setType(?string type): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |


# Example

```php
use NustLmsApiLib\Models\Builders\SiteNotificationBuilder;
use NustLmsApiLib\ApiHelper;

$siteNotification = SiteNotificationBuilder::init()
    ->id(96)
    ->message('message8')
    ->type('type8')
    ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
    ->build();
```



