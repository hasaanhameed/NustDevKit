# Get Core Recent Courses

Source: /#/http/x-redirect/JTI0ZSUyRkNvdXJzZXMlMkZnZXRDb3JlUmVjZW50Q291cnNlcw

Returns the courses the authenticated user has accessed most recently, ordered by last access time.
Moodle method: `core_course_get_recent_courses`

```http
GET /service/core_course_get_recent_courses
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/http/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `Number` | Query, Required | Maximum number of courses to return. |


# Response Type

**200**: List of recently accessed courses ordered by last access.

[`array<Recent Course>`](/llms-pages/http/models/structures/recent-course.md)


# Example Usage

```bash
curl -X GET -G \
  --url 'http://127.0.0.1:8000/service/core_course_get_recent_courses'  \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer AccessToken' \
  -d 'limit=10'
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleError_ErrorException`](/llms-pages/http/models/exceptions/moodle-error-error.md) |



