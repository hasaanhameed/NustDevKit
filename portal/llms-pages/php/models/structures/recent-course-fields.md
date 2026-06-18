# Recent Course Fields

Source: /#/php/x-redirect/JTI0bSUyRlJlY2VudENvdXJzZUZpZWxkcw

Additional fields specific to recently accessed courses.

*This model accepts additional fields of type array.*


# Class Name

`RecentCourseFields`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `timeaccess` | `int` | Required | Unix timestamp of the user's most recent access to this course. | getTimeaccess(): int | setTimeaccess(int timeaccess): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |


# Example

```php
use NustLmsApiLib\Models\Builders\RecentCourseFieldsBuilder;
use NustLmsApiLib\ApiHelper;

$recentCourseFields = RecentCourseFieldsBuilder::init(
    1781632422
)
    ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
    ->build();
```



