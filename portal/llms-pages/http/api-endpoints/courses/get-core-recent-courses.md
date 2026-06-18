# Get Core Recent Courses

Source: /#/http/x-redirect/JTI0ZSUyRkNvdXJzZXMlMkZnZXRDb3JlUmVjZW50Q291cnNlcw

Returns the courses the authenticated user has accessed most recently, ordered by last access time.
Moodle method: `core_course_get_recent_courses`

```http
POST /service/core_course_get_recent_courses
```


# Authentication

This endpoint requires [SessKey](/llms-pages/http/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Get Recent Courses Request`](/llms-pages/http/models/structures/get-recent-courses-request.md) | Body, Required | Parameters for the recent courses request. |


# Response Type

**200**: List of recently accessed courses ordered by last access.

[`array<Recent Course>`](/llms-pages/http/models/structures/recent-course.md)


# Example Usage

```bash
curl -X POST \
  --url 'https://lms.nust.edu.pk/portal/service/core_course_get_recent_courses?sesskey=sesskey'  \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  --data-raw '{
  "limit": 10
}'
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleError_ErrorException`](/llms-pages/http/models/exceptions/moodle-error-error.md) |



