# Get Enrolled Courses by Timeline

Source: /#/net-standard-library/x-redirect/JTI0ZSUyRkNvdXJzZXMlMkZnZXRFbnJvbGxlZENvdXJzZXNCeVRpbWVsaW5l

Returns all courses the user is enrolled in, filtered by timeline classification and sorted by a chosen field. Supports pagination via offset.
Moodle method: `core_course_get_enrolled_courses_by_timeline_classification`

```csharp
GetEnrolledCoursesByTimelineAsync(
    Models.GetEnrolledCoursesByTimelineRequest body)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/net-standard-library/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetEnrolledCoursesByTimelineRequest`](/llms-pages/net-standard-library/models/structures/get-enrolled-courses-by-timeline-request.md) | Body, Required | Parameters for the enrolled courses timeline request. |


# Response Type

**200**: Paginated list of enrolled courses.

This method returns an [`ApiResponse`](/llms-pages/net-standard-library/sdk-infrastructure/utilities/apiresponse.md) instance. The `Data` property of this instance returns the response data which is of type [Models.EnrolledCoursesResponse](/llms-pages/net-standard-library/models/structures/enrolled-courses-response.md).


# Example Usage

```csharp
GetEnrolledCoursesByTimelineRequest body = new GetEnrolledCoursesByTimelineRequest
{
    Offset = 0,
    Limit = 50,
    Classification = CourseTimelineClassification.Past,
    Sort = CourseTimelineSortField.Id,
};

try
{
    ApiResponse<EnrolledCoursesResponse> result = await coursesApi.GetEnrolledCoursesByTimelineAsync(body);
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



