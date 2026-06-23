# Get Enrolled Courses by Timeline

Source: /#/go/x-redirect/JTI0ZSUyRkNvdXJzZXMlMkZnZXRFbnJvbGxlZENvdXJzZXNCeVRpbWVsaW5l

Returns all courses the user is enrolled in, filtered by timeline classification and sorted by a chosen field. Supports pagination via offset.
Moodle method: `core_course_get_enrolled_courses_by_timeline_classification`

```go
GetEnrolledCoursesByTimeline(
    ctx context.Context,
    offset int,
    limit int,
    classification models.CourseTimelineClassification,
    sort models.CourseTimelineSortField) (
    models.ApiResponse[models.EnrolledCoursesResponse],
    error)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/go/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `offset` | `int` | Query, Required | Zero-based pagination offset. |
| `limit` | `int` | Query, Required | Maximum number of courses to return. |
| `classification` | [`models.CourseTimelineClassification`](/llms-pages/go/models/enumerations/course-timeline-classification.md) | Query, Required | Timeline classification filter for enrolled courses. |
| `sort` | [`models.CourseTimelineSortField`](/llms-pages/go/models/enumerations/course-timeline-sort-field.md) | Query, Required | Field used to sort enrolled course results. |


# Response Type

**200**: Paginated list of enrolled courses.

This method returns an [`ApiResponse`](/llms-pages/go/sdk-infrastructure/utilities/apiresponse.md) instance. The `Data` property of this instance returns the response data which is of type [models.EnrolledCoursesResponse](/llms-pages/go/models/structures/enrolled-courses-response.md).


# Example Usage

```go
ctx := context.Background()

offset := 0

limit := 50

classification := models.CourseTimelineClassification_Inprogress

sort := models.CourseTimelineSortField_Idnumber

apiResponse, err := coursesApi.GetEnrolledCoursesByTimeline(ctx, offset, limit, classification, sort)
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



