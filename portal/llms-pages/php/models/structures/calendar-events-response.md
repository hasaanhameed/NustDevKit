# Calendar Events Response

Source: /#/php/x-redirect/JTI0bSUyRkNhbGVuZGFyRXZlbnRzUmVzcG9uc2U

A list of calendar events with pagination boundary IDs.

*This model accepts additional fields of type array.*


# Class Name

`CalendarEventsResponse`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `events` | [`CalendarEvent[]`](/llms-pages/php/models/structures/calendar-event.md) | Required | List of calendar action events for the current result set. | getEvents(): array | setEvents(array events): void |
| `firstid` | `int` | Required | Event ID of the first item in the result set. | getFirstid(): int | setFirstid(int firstid): void |
| `lastid` | `int` | Required | Event ID of the last item in the result set. | getLastid(): int | setLastid(int lastid): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |


# Example

```php
use NustLmsApiLib\Models\Builders\CalendarEventsResponseBuilder;
use NustLmsApiLib\Models\Builders\CalendarEventBuilder;
use NustLmsApiLib\Models\Builders\EventIconBuilder;
use NustLmsApiLib\ApiHelper;
use NustLmsApiLib\Models\Builders\CourseBuilder;
use NustLmsApiLib\Models\Builders\EventSubscriptionBuilder;

$calendarEventsResponse = CalendarEventsResponseBuilder::init(
    [
        CalendarEventBuilder::init(
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
            96,
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
            ->categoryid(154)
            ->groupid(84)
            ->userid(88)
            ->repeatid(28)
            ->eventcount(248)
            ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
            ->build()
    ],
    149885,
    151886
)
    ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
    ->build();
```



