# Get Course Contents

Source: /#/ruby/x-redirect/JTI0ZSUyRkNvdXJzZXMlMkZnZXRDb3Vyc2VDb250ZW50cw

Returns the full content structure of a course — its sections (weeks/topics) and the modules within them (files, folders, pages, URLs, assignments, and other activities), including metadata for each uploaded file. This is the data the course page itself is built from.
Note: file URLs point at Moodle's `pluginfile.php` and require authentication (a webservice token or the active session) to download — the URL alone is not publicly fetchable.
Moodle method: `core_course_get_contents`

```ruby
def get_course_contents(courseid)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/ruby/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `courseid` | `Integer` | Query, Required | ID of the course whose contents to retrieve. |


# Response Type

**200**: Course sections, each with its modules and their uploaded files.

This method returns an [`ApiResponse`](/llms-pages/ruby/sdk-infrastructure/utilities/apiresponse.md) instance. The `data` property of this instance returns the response data which is of type [`Array[CourseSection]`](/llms-pages/ruby/models/structures/course-section.md).


# Example Usage

```ruby
courseid = 74

result = courses_api.get_course_contents(courseid)

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



