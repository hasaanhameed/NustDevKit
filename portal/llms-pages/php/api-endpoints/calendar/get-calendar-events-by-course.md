# Get Calendar Events by Course

Source: /#/php/x-redirect/JTI0ZSUyRkNhbGVuZGFyJTJGZ2V0Q2FsZW5kYXJFdmVudHNCeUNvdXJzZQ

Returns all action events (deadlines) for a single course — assignment, lab, and quiz submission due dates, and other dated activities.
Moodle method: `core_calendar_get_action_events_by_course`

```php
function getCalendarEventsByCourse(
    int $courseid,
    ?int $timesortfrom = null,
    ?int $timesortto = null,
    ?int $aftereventid = null,
    ?int $limitnum = null
): ApiResponse
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/php/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `courseid` | `int` | Query, Required | ID of the course to fetch events for. |
| `timesortfrom` | `?int` | Query, Optional | Only return events with timesort >= this Unix timestamp. |
| `timesortto` | `?int` | Query, Optional | Only return events with timesort <= this Unix timestamp. |
| `aftereventid` | `?int` | Query, Optional | Cursor-based pagination — return events after this event ID. |
| `limitnum` | `?int` | Query, Optional | Maximum number of events to return. |


# Response Type

**200**: Calendar events for the specified course.

This method returns an [`ApiResponse`](/llms-pages/php/sdk-infrastructure/utilities/apiresponse.md) instance. The `getResult()` method on this instance returns the response data which is of type [`CalendarEventsResponse`](/llms-pages/php/models/structures/calendar-events-response.md).


# Example Usage

```php
$courseid = 74;

$calendarApi = $client->getCalendarApi();
$apiResponse = $calendarApi->getCalendarEventsByCourse($courseid);

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



