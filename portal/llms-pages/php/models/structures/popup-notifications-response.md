# Popup Notifications Response

Source: /#/php/x-redirect/JTI0bSUyRlBvcHVwTm90aWZpY2F0aW9uc1Jlc3BvbnNl

Response envelope for the popup-notifications endpoint.

*This model accepts additional fields of type array.*


# Class Name

`PopupNotificationsResponse`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `notifications` | [`Notification[]`](/llms-pages/php/models/structures/notification.md) | Required | List of popup notifications for the user. | getNotifications(): array | setNotifications(array notifications): void |
| `unreadcount` | `int` | Required | Total number of unread notifications for the user. | getUnreadcount(): int | setUnreadcount(int unreadcount): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |


# Example

```php
use NustLmsApiLib\Models\Builders\PopupNotificationsResponseBuilder;
use NustLmsApiLib\Models\Builders\NotificationBuilder;
use NustLmsApiLib\ApiHelper;

$popupNotificationsResponse = PopupNotificationsResponseBuilder::init(
    [
        NotificationBuilder::init(
            4857819,
            198956,
            162154,
            'CS-419-Deep Learning: Lab Sessional Finalization',
            'CS-419-Deep Learning: Lab Sessional Finalization',
            '<p>Areeba Rameen posted in CS-419-Deep Learning...</p>',
            'fullmessage8',
            2,
            'fullmessagehtml4',
            'Areeba Rameen posted in CS-419-Deep Learning...',
            'https://lms.nust.edu.pk/portal/mod/forum/discuss.php?d=41767#p52342',
            'Lab Sessional Finalization - (DL - Section D & E)',
            1780045085,
            '19 days ago',
            false,
            false,
            'https://lms.nust.edu.pk/portal/theme/image.php/moove/mod_forum/1778048051/icon',
            'mod_forum',
            'posts',
            '{"cmid":"1272420","instance":"62569","discussionid":"41767"}'
        )
            ->timeread(152)
            ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
            ->build()
    ],
    1
)
    ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
    ->build();
```



