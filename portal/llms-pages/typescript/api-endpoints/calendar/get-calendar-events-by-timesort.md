# Get Calendar Events by Timesort

Source: /#/typescript/x-redirect/JTI0ZSUyRkNhbGVuZGFyJTJGZ2V0Q2FsZW5kYXJFdmVudHNCeVRpbWVzb3J0

Returns action events (deadlines) across all enrolled courses, ordered by their sort timestamp. On NUST LMS these are submission due dates for assignments, labs, quizzes, and similar dated activities. Use `timesortfrom` to filter to upcoming deadlines only.
Moodle method: `core_calendar_get_action_events_by_timesort`

```ts
async getCalendarEventsByTimesort(
  limitnum: number,
  timesortfrom: number,
  timesortto?: number,
  aftereventid?: number,
  requestOptions?: RequestOptions
): Promise<ApiResponse<CalendarEventsResponse>>
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/typescript/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limitnum` | `number` | Query, Required | Maximum number of events to return (e.g. 20 for one page of results). |
| `timesortfrom` | `number` | Query, Required | Unix timestamp (seconds since epoch). Only events with a sort time at or after this value are returned. Pass `0` for no lower bound (all upcoming and past events). To see only upcoming deadlines, pass the current epoch time (e.g. the output of `Date.now() / 1000 \| 0` in JS or `int(time.time())` in Python). |
| `timesortto` | `number \| undefined` | Query, Optional | Only return events with timesort <= this Unix timestamp. |
| `aftereventid` | `number \| undefined` | Query, Optional | Return events whose ID is greater than this value (cursor pagination). |
| `requestOptions` | `RequestOptions \| undefined` | Optional | Pass additional request options. |


# Response Type

**200**: Calendar events sorted by timesort.

This method returns an [`ApiResponse`](/llms-pages/typescript/sdk-infrastructure/utilities/apiresponse.md) instance. The `result` property of this instance returns the response data which is of type [`CalendarEventsResponse`](/llms-pages/typescript/models/structures/calendar-events-response.md).


# Example Usage

```ts
const limitnum = 20;

const timesortfrom = 0;

try {
  const response = await calendarApi.getCalendarEventsByTimesort(
    limitnum,
    timesortfrom
  );

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



