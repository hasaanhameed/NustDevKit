# Get Users by Field

Source: /#/java/x-redirect/JTI0ZSUyRlVzZXJzJTJGZ2V0VXNlcnNCeUZpZWxk

Retrieves one or more user profiles by matching a specific profile field. Commonly used to look up the authenticated user's own profile by their ID.
Moodle method: `core_user_get_users_by_field`

```java
CompletableFuture<ApiResponse<List<UserProfile>>> getUsersByFieldAsync(
    final GetUsersByFieldRequest body)
```


# Authentication

This endpoint requires [SessKey](/llms-pages/java/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetUsersByFieldRequest`](/llms-pages/java/models/structures/get-users-by-field-request.md) | Body, Required | Parameters specifying the profile field and values to match. |


# Response Type

**200**: List of matching user profiles.

This method returns an [`ApiResponse`](/llms-pages/java/sdk-infrastructure/utilities/apiresponse.md) instance. The `getResult()` getter of this instance returns the response data which is of type [`List<UserProfile>`](/llms-pages/java/models/structures/user-profile.md).


# Example Usage

```java
GetUsersByFieldRequest body = new GetUsersByFieldRequest.Builder(
    UserProfileField.ID,
    Arrays.asList(
        "162154"
    )
)
.build();

usersApi.getUsersByFieldAsync(body).thenAccept(result -> {
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



