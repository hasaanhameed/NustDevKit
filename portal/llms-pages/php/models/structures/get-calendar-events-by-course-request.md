# Get Calendar Events by Course Request

Source: /#/php/x-redirect/JTI0bSUyRkdldENhbGVuZGFyRXZlbnRzQnlDb3Vyc2VSZXF1ZXN0

Request parameters for retrieving calendar action events for a specific course.

*This model accepts additional fields of type array.*


# Class Name

`GetCalendarEventsByCourseRequest`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `courseid` | `int` | Required | ID of the course to fetch events for. | getCourseid(): int | setCourseid(int courseid): void |
| `timesortfrom` | `?int` | Optional | Only return events with timesort >= this Unix timestamp. Optional. | getTimesortfrom(): ?int | setTimesortfrom(?int timesortfrom): void |
| `timesortto` | `?int` | Optional | Only return events with timesort <= this Unix timestamp. Optional. | getTimesortto(): ?int | setTimesortto(?int timesortto): void |
| `aftereventid` | `?int` | Optional | Cursor-based pagination — return events after this event ID. Optional. | getAftereventid(): ?int | setAftereventid(?int aftereventid): void |
| `limitnum` | `?int` | Optional | Maximum number of events to return. Optional. | getLimitnum(): ?int | setLimitnum(?int limitnum): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |


# Example

```php
use NustLmsApiLib\Models\Builders\GetCalendarEventsByCourseRequestBuilder;
use NustLmsApiLib\ApiHelper;

$getCalendarEventsByCourseRequest = GetCalendarEventsByCourseRequestBuilder::init(
    49906
)
    ->timesortfrom(22)
    ->timesortto(138)
    ->aftereventid(136)
    ->limitnum(48)
    ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
    ->build();
```



