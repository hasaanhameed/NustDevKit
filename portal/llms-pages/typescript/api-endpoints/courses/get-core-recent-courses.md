# Get Core Recent Courses

Source: /#/typescript/x-redirect/JTI0ZSUyRkNvdXJzZXMlMkZnZXRDb3JlUmVjZW50Q291cnNlcw

Returns the courses the authenticated user has accessed most recently, ordered by last access time.
Moodle method: `core_course_get_recent_courses`

```ts
async getCoreRecentCourses(
  body: GetRecentCoursesRequest,
  requestOptions?: RequestOptions
): Promise<ApiResponse<RecentCourse[]>>
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/typescript/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetRecentCoursesRequest`](/llms-pages/typescript/models/structures/get-recent-courses-request.md) | Body, Required | Parameters for the recent courses request. |
| `requestOptions` | `RequestOptions \| undefined` | Optional | Pass additional request options. |


# Response Type

**200**: List of recently accessed courses ordered by last access.

This method returns an [`ApiResponse`](/llms-pages/typescript/sdk-infrastructure/utilities/apiresponse.md) instance. The `result` property of this instance returns the response data which is of type [`RecentCourse[]`](/llms-pages/typescript/models/structures/recent-course.md).


# Example Usage

```ts
const body: GetRecentCoursesRequest = {
  limit: 10,
};

try {
  const response = await coursesApi.getCoreRecentCourses(body);

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



