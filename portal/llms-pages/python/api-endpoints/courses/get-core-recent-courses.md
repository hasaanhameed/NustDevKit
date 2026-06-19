# Get Core Recent Courses

Source: /#/python/x-redirect/JTI0ZSUyRkNvdXJzZXMlMkZnZXRDb3JlUmVjZW50Q291cnNlcw

Returns the courses the authenticated user has accessed most recently, ordered by last access time.
Moodle method: `core_course_get_recent_courses`

```python
def get_core_recent_courses(self,
                           body)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/python/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetRecentCoursesRequest`](/llms-pages/python/models/structures/get-recent-courses-request.md) | Body, Required | Parameters for the recent courses request. |


# Response Type

**200**: List of recently accessed courses ordered by last access.

This method returns an [`ApiResponse`](/llms-pages/python/sdk-infrastructure/utilities/apiresponse.md) instance. The `body` property of this instance returns the response data which is of type [`List[RecentCourse]`](/llms-pages/python/models/structures/recent-course.md).


# Example Usage

```python
body = GetRecentCoursesRequest(
    limit=10
)

result = courses_api.get_core_recent_courses(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleErrorException`](/llms-pages/python/models/exceptions/moodle-error.md) |



