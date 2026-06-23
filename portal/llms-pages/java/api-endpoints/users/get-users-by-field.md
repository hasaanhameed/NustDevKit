# Get Users by Field

Source: /#/java/x-redirect/JTI0ZSUyRlVzZXJzJTJGZ2V0VXNlcnNCeUZpZWxk

Retrieves one or more user profiles by matching a specific profile field. Commonly used to look up the authenticated user's own profile by their ID.
Moodle method: `core_user_get_users_by_field`

```java
CompletableFuture<ApiResponse<List<UserProfile>>> getUsersByFieldAsync(
    final UserProfileField field,
    final List<String> values)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/java/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field` | [`UserProfileField`](/llms-pages/java/models/enumerations/user-profile-field.md) | Query, Required | User profile field to match against when searching for users. |
| `values` | `List<String>` | Query, Required | List of field values to look up. All values must be provided as strings even when the field is numeric (e.g., "123456" for an integer ID). |


# Response Type

**200**: List of matching user profiles.

This method returns an [`ApiResponse`](/llms-pages/java/sdk-infrastructure/utilities/apiresponse.md) instance. The `getResult()` getter of this instance returns the response data which is of type [`List<UserProfile>`](/llms-pages/java/models/structures/user-profile.md).


# Example Usage

```java
UserProfileField field = UserProfileField.ID;
List<String> values = Arrays.asList(
    "values0",
    "values1",
    "values2"
);

usersApi.getUsersByFieldAsync(field, values).thenAccept(result -> {
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



