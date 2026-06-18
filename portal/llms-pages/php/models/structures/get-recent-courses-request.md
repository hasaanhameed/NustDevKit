# Get Recent Courses Request

Source: /#/php/x-redirect/JTI0bSUyRkdldFJlY2VudENvdXJzZXNSZXF1ZXN0

Request parameters for retrieving recently accessed courses.

*This model accepts additional fields of type array.*


# Class Name

`GetRecentCoursesRequest`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `limit` | `int` | Required | Maximum number of courses to return.<br><br>**Default**: `10` | getLimit(): int | setLimit(int limit): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |


# Example

```php
use NustLmsApiLib\Models\Builders\GetRecentCoursesRequestBuilder;
use NustLmsApiLib\ApiHelper;

$getRecentCoursesRequest = GetRecentCoursesRequestBuilder::init(
    10
)
    ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
    ->build();
```



