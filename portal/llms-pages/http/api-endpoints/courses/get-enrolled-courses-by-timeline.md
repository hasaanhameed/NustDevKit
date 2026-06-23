# Get Enrolled Courses by Timeline

Source: /#/http/x-redirect/JTI0ZSUyRkNvdXJzZXMlMkZnZXRFbnJvbGxlZENvdXJzZXNCeVRpbWVsaW5l

Returns all courses the user is enrolled in, filtered by timeline classification and sorted by a chosen field. Supports pagination via offset.
Moodle method: `core_course_get_enrolled_courses_by_timeline_classification`

```http
GET /service/core_course_get_enrolled_courses_by_timeline_classification
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/http/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `offset` | `Number` | Query, Required | Zero-based pagination offset. |
| `limit` | `Number` | Query, Required | Maximum number of courses to return. |
| `classification` | [`Course Timeline Classification`](/llms-pages/http/models/enumerations/course-timeline-classification.md) | Query, Required | Timeline classification filter for enrolled courses. |
| `sort` | [`Course Timeline Sort Field`](/llms-pages/http/models/enumerations/course-timeline-sort-field.md) | Query, Required | Field used to sort enrolled course results. |


# Response Type

**200**: Paginated list of enrolled courses.

[`Enrolled Courses Response`](/llms-pages/http/models/structures/enrolled-courses-response.md)


# Example Usage

```bash
curl -X GET -G \
  --url 'http://127.0.0.1:8000/service/core_course_get_enrolled_courses_by_timeline_classification'  \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer AccessToken' \
  -d 'offset=0' \
  -d 'limit=50' \
  -d 'classification=inprogress' \
  -d 'sort=idnumber'
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleError_ErrorException`](/llms-pages/http/models/exceptions/moodle-error-error.md) |



