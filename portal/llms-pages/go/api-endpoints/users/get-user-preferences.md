# Get User Preferences

Source: /#/go/x-redirect/JTI0ZSUyRlVzZXJzJTJGZ2V0VXNlclByZWZlcmVuY2Vz

Returns all stored preference key/value pairs for the specified user. Optionally filter to a single preference by name.
Moodle method: `core_user_get_user_preferences`

```go
GetUserPreferences(
    ctx context.Context,
    body models.GetUserPreferencesRequest) (
    models.ApiResponse[models.UserPreferencesResponse],
    error)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/go/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`models.GetUserPreferencesRequest`](/llms-pages/go/models/structures/get-user-preferences-request.md) | Body, Required | Parameters specifying which user's preferences to retrieve. |


# Response Type

**200**: User preferences list and optional warnings.

This method returns an [`ApiResponse`](/llms-pages/go/sdk-infrastructure/utilities/apiresponse.md) instance. The `Data` property of this instance returns the response data which is of type [models.UserPreferencesResponse](/llms-pages/go/models/structures/user-preferences-response.md).


# Example Usage

```go
ctx := context.Background()

body := models.GetUserPreferencesRequest{
    Userid:                162154,
}

apiResponse, err := usersApi.GetUserPreferences(ctx, body)
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



