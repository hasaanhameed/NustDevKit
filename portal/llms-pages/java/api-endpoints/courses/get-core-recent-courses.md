# Get Core Recent Courses

Source: /#/java/x-redirect/JTI0ZSUyRkNvdXJzZXMlMkZnZXRDb3JlUmVjZW50Q291cnNlcw

Returns the courses the authenticated user has accessed most recently, ordered by last access time.
Moodle method: `core_course_get_recent_courses`

```java
CompletableFuture<ApiResponse<List<RecentCourse>>> getCoreRecentCoursesAsync(
    final GetRecentCoursesRequest body)
```


# Authentication

This endpoint requires [SessKey](/llms-pages/java/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetRecentCoursesRequest`](/llms-pages/java/models/structures/get-recent-courses-request.md) | Body, Required | Parameters for the recent courses request. |


# Response Type

**200**: List of recently accessed courses ordered by last access.

This method returns an [`ApiResponse`](/llms-pages/java/sdk-infrastructure/utilities/apiresponse.md) instance. The `getResult()` getter of this instance returns the response data which is of type [`List<RecentCourse>`](/llms-pages/java/models/structures/recent-course.md).


# Example Usage

```java
GetRecentCoursesRequest body = new GetRecentCoursesRequest.Builder(
    10
)
.build();

coursesApi.getCoreRecentCoursesAsync(body).thenAccept(result -> {
    // TODO success callback handler
    System.out.println(result);
}).exceptionally(exception -> {
    Throwable cause = exception.getCause();

    if (cause instanceof MoodleErrorException) {
        MoodleErrorException moodleErrorException = (MoodleErrorException) cause;
        moodleErrorException.printStackTrace();
    } else {
        // fallback for unexpected errors
        exception.printStackTrace();
    }

    return null;
});
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleErrorException`](/llms-pages/java/models/exceptions/moodle-error.md) |



