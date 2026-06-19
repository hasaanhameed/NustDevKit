# Get Core Recent Courses

Source: /#/net-standard-library/x-redirect/JTI0ZSUyRkNvdXJzZXMlMkZnZXRDb3JlUmVjZW50Q291cnNlcw

Returns the courses the authenticated user has accessed most recently, ordered by last access time.
Moodle method: `core_course_get_recent_courses`

```csharp
GetCoreRecentCoursesAsync(
    Models.GetRecentCoursesRequest body)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/net-standard-library/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetRecentCoursesRequest`](/llms-pages/net-standard-library/models/structures/get-recent-courses-request.md) | Body, Required | Parameters for the recent courses request. |


# Response Type

**200**: List of recently accessed courses ordered by last access.

This method returns an [`ApiResponse`](/llms-pages/net-standard-library/sdk-infrastructure/utilities/apiresponse.md) instance. The `Data` property of this instance returns the response data which is of type [List<Models.RecentCourse>](/llms-pages/net-standard-library/models/structures/recent-course.md).


# Example Usage

```csharp
GetRecentCoursesRequest body = new GetRecentCoursesRequest
{
    Limit = 10,
};

try
{
    ApiResponse<List<RecentCourse>> result = await coursesApi.GetCoreRecentCoursesAsync(body);
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



