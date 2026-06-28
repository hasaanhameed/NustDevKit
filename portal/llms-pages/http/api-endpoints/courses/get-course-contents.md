# Get Course Contents

Source: /#/http/x-redirect/JTI0ZSUyRkNvdXJzZXMlMkZnZXRDb3Vyc2VDb250ZW50cw

Returns the full content structure of a course — its sections (weeks/topics) and the modules within them (files, folders, pages, URLs, assignments, and other activities), including metadata for each uploaded file. This is the data the course page itself is built from.
Note: file URLs point at Moodle's `pluginfile.php` and require authentication (a webservice token or the active session) to download — the URL alone is not publicly fetchable.
Moodle method: `core_course_get_contents`

```http
GET /service/core_course_get_contents
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/http/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `courseid` | `Number` | Query, Required | ID of the course whose contents to retrieve. |


# Response Type

**200**: Course sections, each with its modules and their uploaded files.

[`array<Course Section>`](/llms-pages/http/models/structures/course-section.md)


# Example Usage

```bash
curl -X GET -G \
  --url 'https://api.nustdevkit.com/service/core_course_get_contents'  \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer AccessToken' \
  -d 'courseid=74'
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleError_ErrorException`](/llms-pages/http/models/exceptions/moodle-error-error.md) |



