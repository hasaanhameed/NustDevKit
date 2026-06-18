# Get Enrolled Courses by Timeline Request

Source: /#/php/x-redirect/JTI0bSUyRkdldEVucm9sbGVkQ291cnNlc0J5VGltZWxpbmVSZXF1ZXN0

Request parameters for retrieving enrolled courses filtered by timeline classification.

*This model accepts additional fields of type array.*


# Class Name

`GetEnrolledCoursesByTimelineRequest`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `offset` | `int` | Required | Zero-based pagination offset.<br><br>**Default**: `0` | getOffset(): int | setOffset(int offset): void |
| `limit` | `int` | Required | Maximum number of courses to return.<br><br>**Default**: `50` | getLimit(): int | setLimit(int limit): void |
| `classification` | [`string(CourseTimelineClassification)`](/llms-pages/php/models/enumerations/course-timeline-classification.md) | Required | Timeline classification filter for enrolled courses. | getClassification(): string | setClassification(string classification): void |
| `sort` | [`string(CourseTimelineSortField)`](/llms-pages/php/models/enumerations/course-timeline-sort-field.md) | Required | Field used to sort enrolled course results. | getSort(): string | setSort(string sort): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |


# Example

```php
use NustLmsApiLib\Models\Builders\GetEnrolledCoursesByTimelineRequestBuilder;
use NustLmsApiLib\Models\CourseTimelineClassification;
use NustLmsApiLib\Models\CourseTimelineSortField;
use NustLmsApiLib\ApiHelper;

$getEnrolledCoursesByTimelineRequest = GetEnrolledCoursesByTimelineRequestBuilder::init(
    0,
    50,
    CourseTimelineClassification::FUTURE,
    CourseTimelineSortField::IDNUMBER
)
    ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
    ->build();
```



