# Get Core Recent Courses

Source: /#/ruby/x-redirect/JTI0ZSUyRkNvdXJzZXMlMkZnZXRDb3JlUmVjZW50Q291cnNlcw

Returns the courses the authenticated user has accessed most recently, ordered by last access time.
Moodle method: `core_course_get_recent_courses`

```ruby
def get_core_recent_courses(body)
```


# Authentication

This endpoint requires [SessKey](/llms-pages/ruby/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetRecentCoursesRequest`](/llms-pages/ruby/models/structures/get-recent-courses-request.md) | Body, Required | Parameters for the recent courses request. |


# Response Type

**200**: List of recently accessed courses ordered by last access.

This method returns an [`ApiResponse`](/llms-pages/ruby/sdk-infrastructure/utilities/apiresponse.md) instance. The `data` property of this instance returns the response data which is of type [`Array[RecentCourse]`](/llms-pages/ruby/models/structures/recent-course.md).


# Example Usage

```ruby
body = GetRecentCoursesRequest.new(
  limit: 10
)

result = courses_api.get_core_recent_courses(body)

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



