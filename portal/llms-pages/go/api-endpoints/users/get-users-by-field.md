# Get Users by Field

Source: /#/go/x-redirect/JTI0ZSUyRlVzZXJzJTJGZ2V0VXNlcnNCeUZpZWxk

Retrieves one or more user profiles by matching a specific profile field. Commonly used to look up the authenticated user's own profile by their ID.
Moodle method: `core_user_get_users_by_field`

```go
GetUsersByField(
    ctx context.Context,
    body models.GetUsersByFieldRequest) (
    models.ApiResponse[[]models.UserProfile],
    error)
```


# Authentication

This endpoint requires [SessKey](/llms-pages/go/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`models.GetUsersByFieldRequest`](/llms-pages/go/models/structures/get-users-by-field-request.md) | Body, Required | Parameters specifying the profile field and values to match. |


# Response Type

**200**: List of matching user profiles.

This method returns an [`ApiResponse`](/llms-pages/go/sdk-infrastructure/utilities/apiresponse.md) instance. The `Data` property of this instance returns the response data which is of type [[]models.UserProfile](/llms-pages/go/models/structures/user-profile.md).


# Example Usage

```go
ctx := context.Background()

body := models.GetUsersByFieldRequest{
    Field:                 models.UserProfileField_Id,
    Values:                []string{
        "162154",
    },
}

apiResponse, err := usersApi.GetUsersByField(ctx, body)
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



