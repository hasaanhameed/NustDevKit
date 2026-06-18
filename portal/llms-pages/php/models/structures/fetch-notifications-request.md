# Fetch Notifications Request

Source: /#/php/x-redirect/JTI0bSUyRkZldGNoTm90aWZpY2F0aW9uc1JlcXVlc3Q

Request parameters for fetching site-level notifications.

*This model accepts additional fields of type array.*


# Class Name

`FetchNotificationsRequest`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `contextid` | `int` | Required | Moodle context ID for which to fetch notifications. The user context ID can be found in the user profile image URL path segment. | getContextid(): int | setContextid(int contextid): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |


# Example

```php
use NustLmsApiLib\Models\Builders\FetchNotificationsRequestBuilder;
use NustLmsApiLib\ApiHelper;

$fetchNotificationsRequest = FetchNotificationsRequestBuilder::init(
    1583361
)
    ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
    ->build();
```



