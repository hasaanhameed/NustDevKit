# Get Calendar Events by Course

Source: /#/php/x-redirect/JTI0ZSUyRkNhbGVuZGFyJTJGZ2V0Q2FsZW5kYXJFdmVudHNCeUNvdXJzZQ

Returns all action events (assignments, quizzes, etc.) for a single course.
Moodle method: `core_calendar_get_action_events_by_course`

```php
function getCalendarEventsByCourse(GetCalendarEventsByCourseRequest $body): ApiResponse
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/php/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetCalendarEventsByCourseRequest`](/llms-pages/php/models/structures/get-calendar-events-by-course-request.md) | Body, Required | Parameters for the course-specific calendar events request. |


# Response Type

**200**: Calendar events for the specified course.

This method returns an [`ApiResponse`](/llms-pages/php/sdk-infrastructure/utilities/apiresponse.md) instance. The `getResult()` method on this instance returns the response data which is of type [`CalendarEventsResponse`](/llms-pages/php/models/structures/calendar-events-response.md).


# Example Usage

```php
$body = GetCalendarEventsByCourseRequestBuilder::init(
    49906
)->build();

$calendarApi = $client->getCalendarApi();
$apiResponse = $calendarApi->getCalendarEventsByCourse($body);

// Extracting response status code
var_dump($apiResponse->getStatusCode());
// Extracting response headers
var_dump($apiResponse->getHeaders());

if ($apiResponse->isSuccess()) {
    echo 'CalendarEventsResponse:';
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



