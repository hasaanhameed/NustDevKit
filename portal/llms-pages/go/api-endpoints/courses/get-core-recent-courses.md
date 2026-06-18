# Get Core Recent Courses

Source: /#/go/x-redirect/JTI0ZSUyRkNvdXJzZXMlMkZnZXRDb3JlUmVjZW50Q291cnNlcw

Returns the courses the authenticated user has accessed most recently, ordered by last access time.
Moodle method: `core_course_get_recent_courses`

```go
GetCoreRecentCourses(
    ctx context.Context,
    body models.GetRecentCoursesRequest) (
    models.ApiResponse[[]models.RecentCourse],
    error)
```


# Authentication

This endpoint requires [SessKey](/llms-pages/go/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`models.GetRecentCoursesRequest`](/llms-pages/go/models/structures/get-recent-courses-request.md) | Body, Required | Parameters for the recent courses request. |


# Response Type

**200**: List of recently accessed courses ordered by last access.

This method returns an [`ApiResponse`](/llms-pages/go/sdk-infrastructure/utilities/apiresponse.md) instance. The `Data` property of this instance returns the response data which is of type [[]models.RecentCourse](/llms-pages/go/models/structures/recent-course.md).


# Example Usage

```go
ctx := context.Background()

body := models.GetRecentCoursesRequest{
    Limit:                 10,
}

apiResponse, err := coursesApi.GetCoreRecentCourses(ctx, body)
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



