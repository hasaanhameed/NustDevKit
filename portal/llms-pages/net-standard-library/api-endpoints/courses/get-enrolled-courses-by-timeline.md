# Get Enrolled Courses by Timeline

Source: /#/net-standard-library/x-redirect/JTI0ZSUyRkNvdXJzZXMlMkZnZXRFbnJvbGxlZENvdXJzZXNCeVRpbWVsaW5l

Returns all courses the user is enrolled in, filtered by timeline classification and sorted by a chosen field. Supports pagination via offset.
Moodle method: `core_course_get_enrolled_courses_by_timeline_classification`

```csharp
GetEnrolledCoursesByTimelineAsync(
    int offset,
    int limit,
    Models.CourseTimelineClassification classification,
    Models.CourseTimelineSortField sort)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/net-standard-library/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `offset` | `int` | Query, Required | Zero-based pagination offset. |
| `limit` | `int` | Query, Required | Maximum number of courses to return. |
| `classification` | [`CourseTimelineClassification`](/llms-pages/net-standard-library/models/enumerations/course-timeline-classification.md) | Query, Required | Timeline classification filter for enrolled courses. |
| `sort` | [`CourseTimelineSortField`](/llms-pages/net-standard-library/models/enumerations/course-timeline-sort-field.md) | Query, Required | Field used to sort enrolled course results. |


# Response Type

**200**: Paginated list of enrolled courses.

This method returns an [`ApiResponse`](/llms-pages/net-standard-library/sdk-infrastructure/utilities/apiresponse.md) instance. The `Data` property of this instance returns the response data which is of type [Models.EnrolledCoursesResponse](/llms-pages/net-standard-library/models/structures/enrolled-courses-response.md).


# Example Usage

```csharp
int offset = 0;
int limit = 50;
CourseTimelineClassification classification = CourseTimelineClassification.Inprogress;
CourseTimelineSortField sort = CourseTimelineSortField.Idnumber;
try
{
    ApiResponse<EnrolledCoursesResponse> result = await coursesApi.GetEnrolledCoursesByTimelineAsync(
        offset,
        limit,
        classification,
        sort
    );
}
catch (ApiException e)
{
    Console.WriteLine(e.Message);
    if (e is MoodleErrorException)
    {
       // TODO: Handle MoodleErrorException exception here
    }
}
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleErrorException`](/llms-pages/net-standard-library/models/exceptions/moodle-error.md) |



