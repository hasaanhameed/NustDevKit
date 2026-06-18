# Recent Course

Source: /#/php/x-redirect/JTI0bSUyRlJlY2VudENvdXJzZQ

A recently accessed course, extending Course with the last-access timestamp.

*This model accepts additional fields of type array.*


# Class Name

`RecentCourse`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `id` | `int` | Required | Unique course identifier. | getId(): int | setId(int id): void |
| `fullname` | `string` | Required | Full display name of the course. | getFullname(): string | setFullname(string fullname): void |
| `shortname` | `string` | Required | Short course code or abbreviated name. | getShortname(): string | setShortname(string shortname): void |
| `idnumber` | `string` | Required | Institution-assigned course ID number; empty string if not set. | getIdnumber(): string | setIdnumber(string idnumber): void |
| `summary` | `string` | Required | HTML summary of the course. | getSummary(): string | setSummary(string summary): void |
| `summaryformat` | `int` | Required | Format of the summary field (1 = HTML). | getSummaryformat(): int | setSummaryformat(int summaryformat): void |
| `startdate` | `int` | Required | Course start date as Unix timestamp. | getStartdate(): int | setStartdate(int startdate): void |
| `enddate` | `int` | Required | Course end date as Unix timestamp. 0 means no end date. | getEnddate(): int | setEnddate(int enddate): void |
| `visible` | `bool` | Required | Whether the course is visible to enrolled students. | getVisible(): bool | setVisible(bool visible): void |
| `fullnamedisplay` | `string` | Required | Display name of the course (may differ from fullname for context). | getFullnamedisplay(): string | setFullnamedisplay(string fullnamedisplay): void |
| `viewurl` | `string` | Required | URL to the course page on the LMS portal. | getViewurl(): string | setViewurl(string viewurl): void |
| `progress` | `int` | Required | Student's completion progress as a percentage.<br><br>**Constraints**: `>= 0`, `<= 100` | getProgress(): int | setProgress(int progress): void |
| `hasprogress` | `bool` | Required | Whether completion tracking is enabled for this course. | getHasprogress(): bool | setHasprogress(bool hasprogress): void |
| `isfavourite` | `bool` | Required | Whether the user has marked this course as a favourite. | getIsfavourite(): bool | setIsfavourite(bool isfavourite): void |
| `hidden` | `bool` | Required | Whether the user has hidden this course from their dashboard. | getHidden(): bool | setHidden(bool hidden): void |
| `showshortname` | `bool` | Required | Whether the short name is displayed alongside the full name. | getShowshortname(): bool | setShowshortname(bool showshortname): void |
| `coursecategory` | `string` | Required | Name of the category this course belongs to. | getCoursecategory(): string | setCoursecategory(string coursecategory): void |
| `timeaccess` | `int` | Required | Unix timestamp of the user's most recent access to this course. | getTimeaccess(): int | setTimeaccess(int timeaccess): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |


# Example

```php
use NustLmsApiLib\Models\Builders\RecentCourseBuilder;
use NustLmsApiLib\ApiHelper;

$recentCourse = RecentCourseBuilder::init(
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
    '2nd Semester (SP-2024)',
    1781632422
)
    ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
    ->build();
```



