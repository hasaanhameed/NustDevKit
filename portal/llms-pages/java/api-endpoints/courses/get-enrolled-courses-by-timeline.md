# Get Enrolled Courses by Timeline

Source: /#/java/x-redirect/JTI0ZSUyRkNvdXJzZXMlMkZnZXRFbnJvbGxlZENvdXJzZXNCeVRpbWVsaW5l

Returns all courses the user is enrolled in, filtered by timeline classification and sorted by a chosen field. Supports pagination via offset.
Moodle method: `core_course_get_enrolled_courses_by_timeline_classification`

```java
CompletableFuture<ApiResponse<EnrolledCoursesResponse>> getEnrolledCoursesByTimelineAsync(
    final int offset,
    final int limit,
    final CourseTimelineClassification classification,
    final CourseTimelineSortField sort)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/java/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `offset` | `int` | Query, Required | Zero-based pagination offset. |
| `limit` | `int` | Query, Required | Maximum number of courses to return. |
| `classification` | [`CourseTimelineClassification`](/llms-pages/java/models/enumerations/course-timeline-classification.md) | Query, Required | Timeline classification filter for enrolled courses. |
| `sort` | [`CourseTimelineSortField`](/llms-pages/java/models/enumerations/course-timeline-sort-field.md) | Query, Required | Field used to sort enrolled course results. |


# Response Type

**200**: Paginated list of enrolled courses.

This method returns an [`ApiResponse`](/llms-pages/java/sdk-infrastructure/utilities/apiresponse.md) instance. The `getResult()` getter of this instance returns the response data which is of type [`EnrolledCoursesResponse`](/llms-pages/java/models/structures/enrolled-courses-response.md).


# Example Usage

```java
int offset = 0;
int limit = 50;
CourseTimelineClassification classification = CourseTimelineClassification.INPROGRESS;
CourseTimelineSortField sort = CourseTimelineSortField.IDNUMBER;

coursesApi.getEnrolledCoursesByTimelineAsync(offset, limit, classification, sort).thenAccept(result -> {
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



