# Enrolled Courses Response

Source: /#/php/x-redirect/JTI0bSUyRkVucm9sbGVkQ291cnNlc1Jlc3BvbnNl

Paginated enrolled-courses response.

*This model accepts additional fields of type array.*


# Class Name

`EnrolledCoursesResponse`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `courses` | [`Course[]`](/llms-pages/php/models/structures/course.md) | Required | List of enrolled courses for the current page. | getCourses(): array | setCourses(array courses): void |
| `nextoffset` | `int` | Required | Offset to pass on the next page request; -1 when no further pages exist. | getNextoffset(): int | setNextoffset(int nextoffset): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |


# Example

```php
use NustLmsApiLib\Models\Builders\EnrolledCoursesResponseBuilder;
use NustLmsApiLib\Models\Builders\CourseBuilder;
use NustLmsApiLib\ApiHelper;

$enrolledCoursesResponse = EnrolledCoursesResponseBuilder::init(
    [
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
            ->build()
    ],
    29
)
    ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
    ->build();
```



