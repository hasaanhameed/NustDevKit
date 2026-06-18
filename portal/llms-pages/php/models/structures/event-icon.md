# Event Icon

Source: /#/php/x-redirect/JTI0bSUyRkV2ZW50SWNvbg

Icon metadata for a calendar event.

*This model accepts additional fields of type array.*


# Class Name

`EventIcon`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `key` | `string` | Required | Icon key name used to locate the icon asset. | getKey(): string | setKey(string key): void |
| `component` | `string` | Required | Moodle component that owns the icon (e.g., 'assign'). | getComponent(): string | setComponent(string component): void |
| `alttext` | `string` | Required | Accessible alt text for the icon image. | getAlttext(): string | setAlttext(string alttext): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |


# Example

```php
use NustLmsApiLib\Models\Builders\EventIconBuilder;
use NustLmsApiLib\ApiHelper;

$eventIcon = EventIconBuilder::init(
    'icon',
    'assign',
    'Activity event'
)
    ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
    ->build();
```



