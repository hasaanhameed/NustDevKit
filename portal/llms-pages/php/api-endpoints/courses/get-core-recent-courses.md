# Get Core Recent Courses

Source: /#/php/x-redirect/JTI0ZSUyRkNvdXJzZXMlMkZnZXRDb3JlUmVjZW50Q291cnNlcw

Returns the courses the authenticated user has accessed most recently, ordered by last access time.
Moodle method: `core_course_get_recent_courses`

```php
function getCoreRecentCourses(GetRecentCoursesRequest $body): ApiResponse
```


# Authentication

This endpoint requires [SessKey](/llms-pages/php/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetRecentCoursesRequest`](/llms-pages/php/models/structures/get-recent-courses-request.md) | Body, Required | Parameters for the recent courses request. |


# Response Type

**200**: List of recently accessed courses ordered by last access.

This method returns an [`ApiResponse`](/llms-pages/php/sdk-infrastructure/utilities/apiresponse.md) instance. The `getResult()` method on this instance returns the response data which is of type [`RecentCourse[]`](/llms-pages/php/models/structures/recent-course.md).


# Example Usage

```php
$body = GetRecentCoursesRequestBuilder::init(
    10
)->build();

$coursesApi = $client->getCoursesApi();
$apiResponse = $coursesApi->getCoreRecentCourses($body);

// Extracting response status code
var_dump($apiResponse->getStatusCode());
// Extracting response headers
var_dump($apiResponse->getHeaders());

if ($apiResponse->isSuccess()) {
    echo 'RecentCourse[]:';
    var_dump($apiResponse->getResult());
} else {
    $error = $apiResponse->getResult();
    var_dump($error);
}
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleErrorException`](/llms-pages/php/models/exceptions/moodle-error.md) |



