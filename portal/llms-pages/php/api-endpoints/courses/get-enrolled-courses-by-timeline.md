# Get Enrolled Courses by Timeline

Source: /#/php/x-redirect/JTI0ZSUyRkNvdXJzZXMlMkZnZXRFbnJvbGxlZENvdXJzZXNCeVRpbWVsaW5l

Returns all courses the user is enrolled in, filtered by timeline classification and sorted by a chosen field. Supports pagination via offset.
Moodle method: `core_course_get_enrolled_courses_by_timeline_classification`

```php
function getEnrolledCoursesByTimeline(GetEnrolledCoursesByTimelineRequest $body): ApiResponse
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/php/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetEnrolledCoursesByTimelineRequest`](/llms-pages/php/models/structures/get-enrolled-courses-by-timeline-request.md) | Body, Required | Parameters for the enrolled courses timeline request. |


# Response Type

**200**: Paginated list of enrolled courses.

This method returns an [`ApiResponse`](/llms-pages/php/sdk-infrastructure/utilities/apiresponse.md) instance. The `getResult()` method on this instance returns the response data which is of type [`EnrolledCoursesResponse`](/llms-pages/php/models/structures/enrolled-courses-response.md).


# Example Usage

```php
$body = GetEnrolledCoursesByTimelineRequestBuilder::init(
    0,
    50,
    CourseTimelineClassification::PAST,
    CourseTimelineSortField::ID
)->build();

$coursesApi = $client->getCoursesApi();
$apiResponse = $coursesApi->getEnrolledCoursesByTimeline($body);

// Extracting response status code
var_dump($apiResponse->getStatusCode());
// Extracting response headers
var_dump($apiResponse->getHeaders());

if ($apiResponse->isSuccess()) {
    echo 'EnrolledCoursesResponse:';
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



