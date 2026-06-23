# Get Enrolled Courses by Timeline

Source: /#/python/x-redirect/JTI0ZSUyRkNvdXJzZXMlMkZnZXRFbnJvbGxlZENvdXJzZXNCeVRpbWVsaW5l

Returns all courses the user is enrolled in, filtered by timeline classification and sorted by a chosen field. Supports pagination via offset.
Moodle method: `core_course_get_enrolled_courses_by_timeline_classification`

```python
def get_enrolled_courses_by_timeline(self,
                                    offset,
                                    limit,
                                    classification,
                                    sort)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/python/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `offset` | `int` | Query, Required | Zero-based pagination offset. |
| `limit` | `int` | Query, Required | Maximum number of courses to return. |
| `classification` | [`CourseTimelineClassification`](/llms-pages/python/models/enumerations/course-timeline-classification.md) | Query, Required | Timeline classification filter for enrolled courses. |
| `sort` | [`CourseTimelineSortField`](/llms-pages/python/models/enumerations/course-timeline-sort-field.md) | Query, Required | Field used to sort enrolled course results. |


# Response Type

**200**: Paginated list of enrolled courses.

This method returns an [`ApiResponse`](/llms-pages/python/sdk-infrastructure/utilities/apiresponse.md) instance. The `body` property of this instance returns the response data which is of type [`EnrolledCoursesResponse`](/llms-pages/python/models/structures/enrolled-courses-response.md).


# Example Usage

```python
offset = 0

limit = 50

classification = CourseTimelineClassification.INPROGRESS

sort = CourseTimelineSortField.IDNUMBER

result = courses_api.get_enrolled_courses_by_timeline(
    offset,
    limit,
    classification,
    sort
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleErrorException`](/llms-pages/python/models/exceptions/moodle-error.md) |



