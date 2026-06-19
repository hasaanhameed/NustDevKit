# Get Calendar Events by Timesort

Source: /#/typescript/x-redirect/JTI0ZSUyRkNhbGVuZGFyJTJGZ2V0Q2FsZW5kYXJFdmVudHNCeVRpbWVzb3J0

Returns action events across all enrolled courses, ordered by their sort timestamp. Use `timesortfrom` to filter to upcoming events only.
Moodle method: `core_calendar_get_action_events_by_timesort`

```ts
async getCalendarEventsByTimesort(
  body: GetCalendarEventsByTimesortRequest,
  requestOptions?: RequestOptions
): Promise<ApiResponse<CalendarEventsResponse>>
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/typescript/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetCalendarEventsByTimesortRequest`](/llms-pages/typescript/models/structures/get-calendar-events-by-timesort-request.md) | Body, Required | Parameters for the time-sorted calendar events request. |
| `requestOptions` | `RequestOptions \| undefined` | Optional | Pass additional request options. |


# Response Type

**200**: Calendar events sorted by timesort.

This method returns an [`ApiResponse`](/llms-pages/typescript/sdk-infrastructure/utilities/apiresponse.md) instance. The `result` property of this instance returns the response data which is of type [`CalendarEventsResponse`](/llms-pages/typescript/models/structures/calendar-events-response.md).


# Example Usage

```ts
const body: GetCalendarEventsByTimesortRequest = {
  limitnum: 20,
  timesortfrom: 0,
};

try {
  const response = await calendarApi.getCalendarEventsByTimesort(body);

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



