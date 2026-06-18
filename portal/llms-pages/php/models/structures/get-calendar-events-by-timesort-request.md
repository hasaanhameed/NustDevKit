# Get Calendar Events by Timesort Request

Source: /#/php/x-redirect/JTI0bSUyRkdldENhbGVuZGFyRXZlbnRzQnlUaW1lc29ydFJlcXVlc3Q

Request parameters for retrieving calendar action events sorted by time.

*This model accepts additional fields of type array.*


# Class Name

`GetCalendarEventsByTimesortRequest`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `limitnum` | `int` | Required | Maximum number of events to return. | getLimitnum(): int | setLimitnum(int limitnum): void |
| `timesortfrom` | `int` | Required | Only return events with timesort >= this Unix timestamp. Pass 0 for no lower bound. | getTimesortfrom(): int | setTimesortfrom(int timesortfrom): void |
| `timesortto` | `?int` | Optional | Only return events with timesort <= this Unix timestamp. Optional. | getTimesortto(): ?int | setTimesortto(?int timesortto): void |
| `aftereventid` | `?int` | Optional | Return events whose ID is greater than this value (cursor pagination). Optional. | getAftereventid(): ?int | setAftereventid(?int aftereventid): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |


# Example

```php
use NustLmsApiLib\Models\Builders\GetCalendarEventsByTimesortRequestBuilder;
use NustLmsApiLib\ApiHelper;

$getCalendarEventsByTimesortRequest = GetCalendarEventsByTimesortRequestBuilder::init(
    20,
    0
)
    ->timesortto(114)
    ->aftereventid(112)
    ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
    ->build();
```



