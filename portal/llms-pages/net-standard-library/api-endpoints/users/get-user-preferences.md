# Get User Preferences

Source: /#/net-standard-library/x-redirect/JTI0ZSUyRlVzZXJzJTJGZ2V0VXNlclByZWZlcmVuY2Vz

Returns all stored preference key/value pairs for the specified user. Optionally filter to a single preference by name.
Moodle method: `core_user_get_user_preferences`

```csharp
GetUserPreferencesAsync(
    int userid,
    string name = null)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/net-standard-library/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `userid` | `int` | Query, Required | ID of the user whose preferences to retrieve. |
| `name` | `string` | Query, Optional | Specific preference name to retrieve. Omit to retrieve all preferences. |


# Response Type

**200**: User preferences list and optional warnings.

This method returns an [`ApiResponse`](/llms-pages/net-standard-library/sdk-infrastructure/utilities/apiresponse.md) instance. The `Data` property of this instance returns the response data which is of type [Models.UserPreferencesResponse](/llms-pages/net-standard-library/models/structures/user-preferences-response.md).


# Example Usage

```csharp
int userid = 44;
try
{
    ApiResponse<UserPreferencesResponse> result = await usersApi.GetUserPreferencesAsync(userid);
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



