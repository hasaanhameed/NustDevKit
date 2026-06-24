# Course Module

Source: /#/php/x-redirect/JTI0bSUyRkNvdXJzZU1vZHVsZQ

An item on the course page — an activity or resource (file, page, URL, assignment, ...).

*This model accepts additional fields of type array.*


# Class Name

`CourseModule`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `id` | `int` | Required | Course module ID (cmid). | getId(): int | setId(int id): void |
| `name` | `string` | Required | Display name of the module. | getName(): string | setName(string name): void |
| `modname` | `string` | Required | Module type, e.g. 'resource' (file), 'folder', 'url', 'page', 'label', 'assign', 'quiz', 'forum'. | getModname(): string | setModname(string modname): void |
| `modplural` | `?string` | Optional | Human-readable plural label for the module type. | getModplural(): ?string | setModplural(?string modplural): void |
| `instance` | `?int` | Optional | Instance ID of the activity within its module type. | getInstance(): ?int | setInstance(?int instance): void |
| `description` | `?string` | Optional | HTML description/intro for the module, when present. | getDescription(): ?string | setDescription(?string description): void |
| `visible` | `?int` | Optional | Whether the module is visible (1) or hidden (0). | getVisible(): ?int | setVisible(?int visible): void |
| `uservisible` | `?bool` | Optional | Whether the module is visible to the current user. | getUservisible(): ?bool | setUservisible(?bool uservisible): void |
| `url` | `?string` | Optional | Link to open the activity/resource, when applicable. | getUrl(): ?string | setUrl(?string url): void |
| `modicon` | `?string` | Optional | URL of the module's type icon. | getModicon(): ?string | setModicon(?string modicon): void |
| `contents` | [`?(CourseContentFile[])`](/llms-pages/php/models/structures/course-content-file.md) | Optional | Uploaded files/links for this module (present for resource/folder modules). | getContents(): ?array | setContents(?array contents): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |


# Example

```php
use NustLmsApiLib\Models\Builders\CourseModuleBuilder;
use NustLmsApiLib\ApiHelper;

$courseModule = CourseModuleBuilder::init(
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
    ->build();
```



