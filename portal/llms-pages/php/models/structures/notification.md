# Notification

Source: /#/php/x-redirect/JTI0bSUyRk5vdGlmaWNhdGlvbg

A popup notification message delivered to a user.

*This model accepts additional fields of type array.*


# Class Name

`Notification`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `id` | `int` | Required | Unique notification identifier. | getId(): int | setId(int id): void |
| `useridfrom` | `int` | Required | User ID of the sender. | getUseridfrom(): int | setUseridfrom(int useridfrom): void |
| `useridto` | `int` | Required | User ID of the recipient. | getUseridto(): int | setUseridto(int useridto): void |
| `subject` | `string` | Required | Subject line of the notification. | getSubject(): string | setSubject(string subject): void |
| `shortenedsubject` | `string` | Required | Shortened version of the notification subject for compact display. | getShortenedsubject(): string | setShortenedsubject(string shortenedsubject): void |
| `text` | `string` | Required | Short HTML excerpt of the notification. | getText(): string | setText(string text): void |
| `fullmessage` | `string` | Required | Full plain-text body of the notification. | getFullmessage(): string | setFullmessage(string fullmessage): void |
| `fullmessageformat` | `int` | Required | Format identifier for fullmessagehtml (2 = Markdown source). | getFullmessageformat(): int | setFullmessageformat(int fullmessageformat): void |
| `fullmessagehtml` | `string` | Required | Full HTML body of the notification email. | getFullmessagehtml(): string | setFullmessagehtml(string fullmessagehtml): void |
| `smallmessage` | `string` | Required | Short plain-text preview of the notification. | getSmallmessage(): string | setSmallmessage(string smallmessage): void |
| `contexturl` | `string` | Required | URL to the relevant context for this notification (e.g., a forum post). | getContexturl(): string | setContexturl(string contexturl): void |
| `contexturlname` | `string` | Required | Human-readable label for the context URL link. | getContexturlname(): string | setContexturlname(string contexturlname): void |
| `timecreated` | `int` | Required | Unix timestamp when the notification was created. | getTimecreated(): int | setTimecreated(int timecreated): void |
| `timecreatedpretty` | `string` | Required | Human-readable relative time string (e.g., '19 days ago'). | getTimecreatedpretty(): string | setTimecreatedpretty(string timecreatedpretty): void |
| `timeread` | `?int` | Optional | Unix timestamp when the notification was read; null if unread. | getTimeread(): ?int | setTimeread(?int timeread): void |
| `read` | `bool` | Required | Whether the notification has been read by the recipient. | getRead(): bool | setRead(bool read): void |
| `deleted` | `bool` | Required | Whether the notification has been deleted by the recipient. | getDeleted(): bool | setDeleted(bool deleted): void |
| `iconurl` | `string` | Required | URL to the icon image representing the notification source. | getIconurl(): string | setIconurl(string iconurl): void |
| `component` | `string` | Required | Moodle component that generated the notification (e.g., 'mod_forum'). | getComponent(): string | setComponent(string component): void |
| `eventtype` | `string` | Required | Event type within the component that triggered the notification (e.g., 'posts'). | getEventtype(): string | setEventtype(string eventtype): void |
| `customdata` | `string` | Required | JSON-encoded string with additional notification metadata (cmid, instance, discussionid, postid, etc.). | getCustomdata(): string | setCustomdata(string customdata): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |


# Example

```php
use NustLmsApiLib\Models\Builders\NotificationBuilder;
use NustLmsApiLib\ApiHelper;

$notification = NotificationBuilder::init(
    4857819,
    234567,
    123456,
    'CS-101 Introduction to Computing: Lab 3 Submission Deadline',
    'CS-101 Introduction to Computing: Lab 3 Submission Deadline',
    '<p>John Doe posted in CS-101 Introduction to Computing...</p>',
    'fullmessage8',
    2,
    'fullmessagehtml6',
    'John Doe posted in CS-101 Introduction to Computing...',
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
    ->timeread(102)
    ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
    ->build();
```



