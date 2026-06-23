# Get Calendar Events by Course

Source: /#/typescript/x-redirect/JTI0ZSUyRkNhbGVuZGFyJTJGZ2V0Q2FsZW5kYXJFdmVudHNCeUNvdXJzZQ

Returns all action events (deadlines) for a single course — assignment, lab, and quiz submission due dates, and other dated activities.
Moodle method: `core_calendar_get_action_events_by_course`

```ts
async getCalendarEventsByCourse(
  courseid: number,
  timesortfrom?: number,
  timesortto?: number,
  aftereventid?: number,
  limitnum?: number,
  requestOptions?: RequestOptions
): Promise<ApiResponse<CalendarEventsResponse>>
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/typescript/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `courseid` | `number` | Query, Required | ID of the course to fetch events for. |
| `timesortfrom` | `number \| undefined` | Query, Optional | Only return events with timesort >= this Unix timestamp. |
| `timesortto` | `number \| undefined` | Query, Optional | Only return events with timesort <= this Unix timestamp. |
| `aftereventid` | `number \| undefined` | Query, Optional | Cursor-based pagination — return events after this event ID. |
| `limitnum` | `number \| undefined` | Query, Optional | Maximum number of events to return. |
| `requestOptions` | `RequestOptions \| undefined` | Optional | Pass additional request options. |


# Response Type

**200**: Calendar events for the specified course.

This method returns an [`ApiResponse`](/llms-pages/typescript/sdk-infrastructure/utilities/apiresponse.md) instance. The `result` property of this instance returns the response data which is of type [`CalendarEventsResponse`](/llms-pages/typescript/models/structures/calendar-events-response.md).


# Example Usage

```ts
const courseid = 74;

try {
  const response = await calendarApi.getCalendarEventsByCourse(courseid);

  // Extracting fully parsed response body.
  console.log(response.result);

  // Extracting response status code.
  console.log(response.statusCode);
  // Extracting response headers.
  console.log(response.headers);
  // Extracting response body of type `string | Stream`
  console.log(response.body);
} catch (error) {
  if (error instanceof ApiError) {
    // Extracting response error status code.
    console.log(error.statusCode);
    // Extracting response error headers.
    console.log(error.headers);
    // Extracting response error body of type `string | Stream`.
    console.log(error.body);
    if (error instanceof MoodleError) {
      console.log(error.result);
    }
  }
}
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleError`](/llms-pages/typescript/models/exceptions/moodle-error.md) |



