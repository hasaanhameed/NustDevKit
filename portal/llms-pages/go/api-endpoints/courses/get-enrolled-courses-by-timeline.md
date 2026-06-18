# Get Enrolled Courses by Timeline

Source: /#/go/x-redirect/JTI0ZSUyRkNvdXJzZXMlMkZnZXRFbnJvbGxlZENvdXJzZXNCeVRpbWVsaW5l

Returns all courses the user is enrolled in, filtered by timeline classification and sorted by a chosen field. Supports pagination via offset.
Moodle method: `core_course_get_enrolled_courses_by_timeline_classification`

```go
GetEnrolledCoursesByTimeline(
    ctx context.Context,
    body models.GetEnrolledCoursesByTimelineRequest) (
    models.ApiResponse[models.EnrolledCoursesResponse],
    error)
```


# Authentication

This endpoint requires [SessKey](/llms-pages/go/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`models.GetEnrolledCoursesByTimelineRequest`](/llms-pages/go/models/structures/get-enrolled-courses-by-timeline-request.md) | Body, Required | Parameters for the enrolled courses timeline request. |


# Response Type

**200**: Paginated list of enrolled courses.

This method returns an [`ApiResponse`](/llms-pages/go/sdk-infrastructure/utilities/apiresponse.md) instance. The `Data` property of this instance returns the response data which is of type [models.EnrolledCoursesResponse](/llms-pages/go/models/structures/enrolled-courses-response.md).


# Example Usage

```go
ctx := context.Background()

body := models.GetEnrolledCoursesByTimelineRequest{
    Offset:                0,
    Limit:                 50,
    Classification:        models.CourseTimelineClassification_Past,
    Sort:                  models.CourseTimelineSortField_Id,
}

apiResponse, err := coursesApi.GetEnrolledCoursesByTimeline(ctx, body)
if err != nil {
    switch typedErr := err.(type) {
        case *errors.MoodleError:
            log.Fatalln("MoodleErrorException: ", typedErr)
        default:
            log.Fatalln(err)
    }
} else {
    // Printing the result and response
    fmt.Println(apiResponse.Data)
    fmt.Println(apiResponse.Response.StatusCode)
}
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleErrorException`](/llms-pages/go/models/exceptions/moodle-error.md) |



