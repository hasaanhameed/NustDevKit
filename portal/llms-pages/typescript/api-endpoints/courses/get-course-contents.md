# Get Course Contents

Source: /#/typescript/x-redirect/JTI0ZSUyRkNvdXJzZXMlMkZnZXRDb3Vyc2VDb250ZW50cw

Returns the full content structure of a course — its sections (weeks/topics) and the modules within them (files, folders, pages, URLs, assignments, and other activities), including metadata for each uploaded file. This is the data the course page itself is built from.
Note: file URLs point at Moodle's `pluginfile.php` and require authentication (a webservice token or the active session) to download — the URL alone is not publicly fetchable.
Moodle method: `core_course_get_contents`

```ts
async getCourseContents(
  courseid: number,
  requestOptions?: RequestOptions
): Promise<ApiResponse<CourseSection[]>>
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/typescript/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `courseid` | `number` | Query, Required | ID of the course whose contents to retrieve. |
| `requestOptions` | `RequestOptions \| undefined` | Optional | Pass additional request options. |


# Response Type

**200**: Course sections, each with its modules and their uploaded files.

This method returns an [`ApiResponse`](/llms-pages/typescript/sdk-infrastructure/utilities/apiresponse.md) instance. The `result` property of this instance returns the response data which is of type [`CourseSection[]`](/llms-pages/typescript/models/structures/course-section.md).


# Example Usage

```ts
const courseid = 74;

try {
  const response = await coursesApi.getCourseContents(courseid);

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



