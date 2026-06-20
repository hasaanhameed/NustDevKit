# Get Popup Notifications Request

Source: /#/php/x-redirect/JTI0bSUyRkdldFBvcHVwTm90aWZpY2F0aW9uc1JlcXVlc3Q

Request parameters for retrieving popup notifications for a user.

*This model accepts additional fields of type array.*


# Class Name

`GetPopupNotificationsRequest`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `useridto` | `string` | Required | ID of the recipient user, passed as a string. | getUseridto(): string | setUseridto(string useridto): void |
| `limit` | `int` | Required | Maximum number of notifications to return. | getLimit(): int | setLimit(int limit): void |
| `offset` | `int` | Required | Pagination offset.<br><br>**Default**: `0` | getOffset(): int | setOffset(int offset): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |


# Example

```php
use NustLmsApiLib\Models\Builders\GetPopupNotificationsRequestBuilder;
use NustLmsApiLib\ApiHelper;

$getPopupNotificationsRequest = GetPopupNotificationsRequestBuilder::init(
    '123456',
    20,
    0
)
    ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
    ->build();
```



