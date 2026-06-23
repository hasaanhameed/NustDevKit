# Get Users by Field

Source: /#/net-standard-library/x-redirect/JTI0ZSUyRlVzZXJzJTJGZ2V0VXNlcnNCeUZpZWxk

Retrieves one or more user profiles by matching a specific profile field. Commonly used to look up the authenticated user's own profile by their ID.
Moodle method: `core_user_get_users_by_field`

```csharp
GetUsersByFieldAsync(
    Models.UserProfileField field,
    List<string> values)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/net-standard-library/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field` | [`UserProfileField`](/llms-pages/net-standard-library/models/enumerations/user-profile-field.md) | Query, Required | User profile field to match against when searching for users. |
| `values` | `List<string>` | Query, Required | List of field values to look up. All values must be provided as strings even when the field is numeric (e.g., "123456" for an integer ID). |


# Response Type

**200**: List of matching user profiles.

This method returns an [`ApiResponse`](/llms-pages/net-standard-library/sdk-infrastructure/utilities/apiresponse.md) instance. The `Data` property of this instance returns the response data which is of type [List<Models.UserProfile>](/llms-pages/net-standard-library/models/structures/user-profile.md).


# Example Usage

```csharp
UserProfileField field = UserProfileField.Id;
List<string> values = new List<string>
{
    "values0",
    "values1",
    "values2",
};

try
{
    ApiResponse<List<UserProfile>> result = await usersApi.GetUsersByFieldAsync(
        field,
        values
    );
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



