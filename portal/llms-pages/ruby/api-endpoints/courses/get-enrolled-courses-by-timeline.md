# Get Enrolled Courses by Timeline

Source: /#/ruby/x-redirect/JTI0ZSUyRkNvdXJzZXMlMkZnZXRFbnJvbGxlZENvdXJzZXNCeVRpbWVsaW5l

Returns all courses the user is enrolled in, filtered by timeline classification and sorted by a chosen field. Supports pagination via offset.
Moodle method: `core_course_get_enrolled_courses_by_timeline_classification`

```ruby
def get_enrolled_courses_by_timeline(offset,
                                     limit,
                                     classification,
                                     sort)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/ruby/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `offset` | `Integer` | Query, Required | Zero-based pagination offset. |
| `limit` | `Integer` | Query, Required | Maximum number of courses to return. |
| `classification` | [`CourseTimelineClassification`](/llms-pages/ruby/models/enumerations/course-timeline-classification.md) | Query, Required | Timeline classification filter for enrolled courses. |
| `sort` | [`CourseTimelineSortField`](/llms-pages/ruby/models/enumerations/course-timeline-sort-field.md) | Query, Required | Field used to sort enrolled course results. |


# Response Type

**200**: Paginated list of enrolled courses.

This method returns an [`ApiResponse`](/llms-pages/ruby/sdk-infrastructure/utilities/apiresponse.md) instance. The `data` property of this instance returns the response data which is of type [`EnrolledCoursesResponse`](/llms-pages/ruby/models/structures/enrolled-courses-response.md).


# Example Usage

```ruby
offset = 0

limit = 50

classification = CourseTimelineClassification::INPROGRESS

sort = CourseTimelineSortField::IDNUMBER

result = courses_api.get_enrolled_courses_by_timeline(
  offset,
  limit,
  classification,
  sort
)

if result.success?
  puts result.data
elsif result.error?
  warn result.errors
end
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleErrorException`](/llms-pages/ruby/models/exceptions/moodle-error.md) |



