# Course Section

Source: /#/php/x-redirect/JTI0bSUyRkNvdXJzZVNlY3Rpb24

A section (week/topic) of the course, containing its modules.

*This model accepts additional fields of type array.*


# Class Name

`CourseSection`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `id` | `int` | Required | Section ID. | getId(): int | setId(int id): void |
| `name` | `string` | Required | Section title (e.g. a week or topic name). | getName(): string | setName(string name): void |
| `section` | `int` | Required | Zero-based section number within the course. | getSection(): int | setSection(int section): void |
| `visible` | `?int` | Optional | Whether the section is visible (1) or hidden (0). | getVisible(): ?int | setVisible(?int visible): void |
| `summary` | `?string` | Optional | HTML summary shown at the top of the section. | getSummary(): ?string | setSummary(?string summary): void |
| `summaryformat` | `?int` | Optional | Moodle text format of the summary (1 = HTML). | getSummaryformat(): ?int | setSummaryformat(?int summaryformat): void |
| `uservisible` | `?bool` | Optional | Whether the section is visible to the current user. | getUservisible(): ?bool | setUservisible(?bool uservisible): void |
| `modules` | [`CourseModule[]`](/llms-pages/php/models/structures/course-module.md) | Required | The activities and resources in this section. | getModules(): array | setModules(array modules): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |


# Example

```php
use NustLmsApiLib\Models\Builders\CourseSectionBuilder;
use NustLmsApiLib\Models\Builders\CourseModuleBuilder;
use NustLmsApiLib\ApiHelper;

$courseSection = CourseSectionBuilder::init(
    33445,
    'Week 1',
    1,
    [
        CourseModuleBuilder::init(
            987654,
            'Lecture 01 — Introduction',
            'resource'
        )
            ->modplural('Files')
            ->instance(45678)
            ->description('<p>Course introduction and logistics.</p>')
            ->visible(1)
            ->uservisible(true)
            ->url('https://lms.nust.edu.pk/portal/mod/resource/view.php?id=987654')
            ->modicon('https://lms.nust.edu.pk/portal/theme/image.php/moove/core/1/f/pdf')
            ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
            ->build()
    ]
)
    ->visible(1)
    ->summary('<p>Introduction and course overview.</p>')
    ->summaryformat(1)
    ->uservisible(true)
    ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
    ->build();
```



