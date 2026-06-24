# Get Course Contents

Source: /#/python/x-redirect/JTI0ZSUyRkNvdXJzZXMlMkZnZXRDb3Vyc2VDb250ZW50cw

Returns the full content structure of a course — its sections (weeks/topics) and the modules within them (files, folders, pages, URLs, assignments, and other activities), including metadata for each uploaded file. This is the data the course page itself is built from.
Note: file URLs point at Moodle's `pluginfile.php` and require authentication (a webservice token or the active session) to download — the URL alone is not publicly fetchable.
Moodle method: `core_course_get_contents`

```python
def get_course_contents(self,
                       courseid)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/python/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `courseid` | `int` | Query, Required | ID of the course whose contents to retrieve. |


# Response Type

**200**: Course sections, each with its modules and their uploaded files.

This method returns an [`ApiResponse`](/llms-pages/python/sdk-infrastructure/utilities/apiresponse.md) instance. The `body` property of this instance returns the response data which is of type [`List[CourseSection]`](/llms-pages/python/models/structures/course-section.md).


# Example Usage

```python
courseid = 74

result = courses_api.get_course_contents(courseid)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleErrorException`](/llms-pages/python/models/exceptions/moodle-error.md) |



