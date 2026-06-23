# Get Enrolled Courses by Timeline

Source: /#/typescript/x-redirect/JTI0ZSUyRkNvdXJzZXMlMkZnZXRFbnJvbGxlZENvdXJzZXNCeVRpbWVsaW5l

Returns all courses the user is enrolled in, filtered by timeline classification and sorted by a chosen field. Supports pagination via offset.
Moodle method: `core_course_get_enrolled_courses_by_timeline_classification`

```ts
async getEnrolledCoursesByTimeline(
  offset: number,
  limit: number,
  classification: CourseTimelineClassification,
  sort: CourseTimelineSortField,
  requestOptions?: RequestOptions
): Promise<ApiResponse<EnrolledCoursesResponse>>
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/typescript/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `offset` | `number` | Query, Required | Zero-based pagination offset. |
| `limit` | `number` | Query, Required | Maximum number of courses to return. |
| `classification` | [`CourseTimelineClassification`](/llms-pages/typescript/models/enumerations/course-timeline-classification.md) | Query, Required | Timeline classification filter for enrolled courses. |
| `sort` | [`CourseTimelineSortField`](/llms-pages/typescript/models/enumerations/course-timeline-sort-field.md) | Query, Required | Field used to sort enrolled course results. |
| `requestOptions` | `RequestOptions \| undefined` | Optional | Pass additional request options. |


# Response Type

**200**: Paginated list of enrolled courses.

This method returns an [`ApiResponse`](/llms-pages/typescript/sdk-infrastructure/utilities/apiresponse.md) instance. The `result` property of this instance returns the response data which is of type [`EnrolledCoursesResponse`](/llms-pages/typescript/models/structures/enrolled-courses-response.md).


# Example Usage

```ts
const offset = 0;

const limit = 50;

const classification = CourseTimelineClassification.Inprogress;

const sort = CourseTimelineSortField.Idnumber;

try {
  const response = await coursesApi.getEnrolledCoursesByTimeline(
    offset,
    limit,
    classification,
    sort
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



