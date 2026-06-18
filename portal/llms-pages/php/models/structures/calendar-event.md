# Calendar Event

Source: /#/php/x-redirect/JTI0bSUyRkNhbGVuZGFyRXZlbnQ

A calendar action event tied to a course activity (e.g., an assignment deadline).

*This model accepts additional fields of type array.*


# Class Name

`CalendarEvent`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `id` | `int` | Required | Unique calendar event identifier. | getId(): int | setId(int id): void |
| `name` | `string` | Required | Display name of the calendar event. | getName(): string | setName(string name): void |
| `description` | `string` | Required | HTML description body of the event. | getDescription(): string | setDescription(string description): void |
| `descriptionformat` | `int` | Required | Text format of the description (1 = HTML). | getDescriptionformat(): int | setDescriptionformat(int descriptionformat): void |
| `location` | `string` | Required | Physical or virtual location of the event; empty string if not specified. | getLocation(): string | setLocation(string location): void |
| `categoryid` | `?int` | Optional | Course category ID; null if not a category event. | getCategoryid(): ?int | setCategoryid(?int categoryid): void |
| `groupid` | `?int` | Optional | Group ID if the event is group-specific; null otherwise. | getGroupid(): ?int | setGroupid(?int groupid): void |
| `userid` | `?int` | Optional | User ID if the event is user-specific; null otherwise. | getUserid(): ?int | setUserid(?int userid): void |
| `repeatid` | `?int` | Optional | ID of the repeat group for recurring events; null if not recurring. | getRepeatid(): ?int | setRepeatid(?int repeatid): void |
| `eventcount` | `?int` | Optional | Total number of events in the repeat group; null if not applicable. | getEventcount(): ?int | setEventcount(?int eventcount): void |
| `component` | `string` | Required | Moodle component that created the event (e.g., 'mod_assign'). | getComponent(): string | setComponent(string component): void |
| `modulename` | `string` | Required | Short name of the Moodle activity module (e.g., 'assign'). | getModulename(): string | setModulename(string modulename): void |
| `instance` | `int` | Required | The course module instance ID. | getInstance(): int | setInstance(int instance): void |
| `eventtype` | `string` | Required | Type of the event (e.g., 'due', 'open', 'close'). | getEventtype(): string | setEventtype(string eventtype): void |
| `timestart` | `int` | Required | Event start time as Unix timestamp. | getTimestart(): int | setTimestart(int timestart): void |
| `timeduration` | `int` | Required | Duration in seconds; 0 for point-in-time events. | getTimeduration(): int | setTimeduration(int timeduration): void |
| `timesort` | `int` | Required | Sort timestamp used for ordering events. | getTimesort(): int | setTimesort(int timesort): void |
| `visible` | `int` | Required | Visibility flag for a calendar event. 1 means the event is visible; 0 means it is hidden. | getVisible(): int | setVisible(int visible): void |
| `timemodified` | `int` | Required | Last modification time as Unix timestamp. | getTimemodified(): int | setTimemodified(int timemodified): void |
| `icon` | [`EventIcon`](/llms-pages/php/models/structures/event-icon.md) | Required | Icon metadata for a calendar event. | getIcon(): EventIcon | setIcon(EventIcon icon): void |
| `course` | [`Course`](/llms-pages/php/models/structures/course.md) | Required | An enrolled course. | getCourse(): Course | setCourse(Course course): void |
| `subscription` | [`EventSubscription`](/llms-pages/php/models/structures/event-subscription.md) | Required | Subscription display settings for a calendar event. | getSubscription(): EventSubscription | setSubscription(EventSubscription subscription): void |
| `canedit` | `bool` | Required | Whether the current user can edit this event. | getCanedit(): bool | setCanedit(bool canedit): void |
| `candelete` | `bool` | Required | Whether the current user can delete this event. | getCandelete(): bool | setCandelete(bool candelete): void |
| `deleteurl` | `string` | Required | URL to delete this calendar event. | getDeleteurl(): string | setDeleteurl(string deleteurl): void |
| `editurl` | `string` | Required | URL to edit the underlying course module associated with this event. | getEditurl(): string | setEditurl(string editurl): void |
| `viewurl` | `string` | Required | URL to view this event on the calendar. | getViewurl(): string | setViewurl(string viewurl): void |
| `formattedtime` | `string` | Required | HTML-formatted human-readable event time string. | getFormattedtime(): string | setFormattedtime(string formattedtime): void |
| `isactionevent` | `bool` | Required | Whether this is an action event requiring user interaction. | getIsactionevent(): bool | setIsactionevent(bool isactionevent): void |
| `iscourseevent` | `bool` | Required | Whether this event is associated with a specific course. | getIscourseevent(): bool | setIscourseevent(bool iscourseevent): void |
| `iscategoryevent` | `bool` | Required | Whether this event is associated with a course category. | getIscategoryevent(): bool | setIscategoryevent(bool iscategoryevent): void |
| `groupname` | `?string` | Optional | Name of the group for group-specific events; null otherwise. | getGroupname(): ?string | setGroupname(?string groupname): void |
| `normalisedeventtype` | `string` | Required | Normalised event type identifier used for display grouping. | getNormalisedeventtype(): string | setNormalisedeventtype(string normalisedeventtype): void |
| `normalisedeventtypetext` | `string` | Required | Human-readable label for the normalised event type. | getNormalisedeventtypetext(): string | setNormalisedeventtypetext(string normalisedeventtypetext): void |
| `action` | [`?EventAction`](/llms-pages/php/models/structures/event-action.md) | Optional | Primary action button metadata for a calendar event. | getAction(): ?EventAction | setAction(?EventAction action): void |
| `url` | `string` | Required | Direct URL to the course activity associated with this event. | getUrl(): string | setUrl(string url): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |


# Example

```php
use NustLmsApiLib\Models\Builders\CalendarEventBuilder;
use NustLmsApiLib\Models\Builders\EventIconBuilder;
use NustLmsApiLib\ApiHelper;
use NustLmsApiLib\Models\Builders\CourseBuilder;
use NustLmsApiLib\Models\Builders\EventSubscriptionBuilder;

$calendarEvent = CalendarEventBuilder::init(
    149885,
    'Lab 1 BSCS 13C is due',
    '<p dir="ltr">Lab 1 BSCS 13C<br /></p>',
    1,
    '',
    'mod_assign',
    'assign',
    999404,
    'due',
    1706900340,
    0,
    1706900340,
    106,
    1779088440,
    EventIconBuilder::init(
        'icon',
        'assign',
        'Activity event'
    )
        ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
        ->build(),
    CourseBuilder::init(
        49900,
        'CS-212 Object Oriented Programming BSCS-13 2K23 ABC',
        'CS-212-Sp\'24 BSCS-13 2K23 ABC',
        '',
        '',
        1,
        1706468400,
        1717362000,
        true,
        'CS-212 Object Oriented Programming BSCS-13 2K23 ABC',
        'https://lms.nust.edu.pk/portal/course/view.php?id=49900',
        21,
        true,
        false,
        false,
        false,
        '2nd Semester (SP-2024)'
    )
        ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
        ->build(),
    EventSubscriptionBuilder::init(
        false
    )
        ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
        ->build(),
    false,
    false,
    'https://lms.nust.edu.pk/portal/calendar/delete.php?id=149885&course=49900',
    'https://lms.nust.edu.pk/portal/course/mod.php?update=999404&return=1&sesskey=XXXX',
    'https://lms.nust.edu.pk/portal/calendar/view.php?view=day&course=49900&time=1706900340',
    '<span class="dimmed_text">Friday, 2 February, 11:59 PM</span>',
    true,
    false,
    false,
    'course',
    'Course event',
    'https://lms.nust.edu.pk/portal/mod/assign/view.php?id=999404'
)
    ->categoryid(164)
    ->groupid(74)
    ->userid(178)
    ->repeatid(38)
    ->eventcount(2)
    ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
    ->build();
```



