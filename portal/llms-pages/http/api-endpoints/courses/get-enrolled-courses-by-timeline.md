# Get Enrolled Courses by Timeline

Source: /#/http/x-redirect/JTI0ZSUyRkNvdXJzZXMlMkZnZXRFbnJvbGxlZENvdXJzZXNCeVRpbWVsaW5l

Returns all courses the user is enrolled in, filtered by timeline classification and sorted by a chosen field. Supports pagination via offset.
Moodle method: `core_course_get_enrolled_courses_by_timeline_classification`

```http
POST /service/core_course_get_enrolled_courses_by_timeline_classification
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/http/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Get Enrolled Courses by Timeline Request`](/llms-pages/http/models/structures/get-enrolled-courses-by-timeline-request.md) | Body, Required | Parameters for the enrolled courses timeline request. |


# Response Type

**200**: Paginated list of enrolled courses.

[`Enrolled Courses Response`](/llms-pages/http/models/structures/enrolled-courses-response.md)


# Example Usage

```bash
curl -X POST \
  --url 'http://127.0.0.1:8000/service/core_course_get_enrolled_courses_by_timeline_classification'  \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer AccessToken' \
  --data-raw '{
  "offset": 0,
  "limit": 50,
  "classification": "past",
  "sort": "id"
}'
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleError_ErrorException`](/llms-pages/http/models/exceptions/moodle-error-error.md) |



