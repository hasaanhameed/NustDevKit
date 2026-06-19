# Get Users by Field

Source: /#/typescript/x-redirect/JTI0ZSUyRlVzZXJzJTJGZ2V0VXNlcnNCeUZpZWxk

Retrieves one or more user profiles by matching a specific profile field. Commonly used to look up the authenticated user's own profile by their ID.
Moodle method: `core_user_get_users_by_field`

```ts
async getUsersByField(
  body: GetUsersByFieldRequest,
  requestOptions?: RequestOptions
): Promise<ApiResponse<UserProfile[]>>
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/typescript/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetUsersByFieldRequest`](/llms-pages/typescript/models/structures/get-users-by-field-request.md) | Body, Required | Parameters specifying the profile field and values to match. |
| `requestOptions` | `RequestOptions \| undefined` | Optional | Pass additional request options. |


# Response Type

**200**: List of matching user profiles.

This method returns an [`ApiResponse`](/llms-pages/typescript/sdk-infrastructure/utilities/apiresponse.md) instance. The `result` property of this instance returns the response data which is of type [`UserProfile[]`](/llms-pages/typescript/models/structures/user-profile.md).


# Example Usage

```ts
const body: GetUsersByFieldRequest = {
  field: UserProfileField.Id,
  values: [
    '162154'
  ],
};

try {
  const response = await usersApi.getUsersByField(body);

  // Extracting fully parsed response body.
  console.log(response.result);

  // Extracting response status code.
  console.log(response.statusCode);
  // Extracting response headers.
  console.log(response.headers);
  // Extracting response body of type `string | Stream`
  console.log(response.body);
} catch (error) {
  if (error instanceof ApiError) {
    // Extracting response error status code.
    console.log(error.statusCode);
    // Extracting response error headers.
    console.log(error.headers);
    // Extracting response error body of type `string | Stream`.
    console.log(error.body);
    if (error instanceof MoodleError) {
      console.log(error.result);
    }
  }
}
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleError`](/llms-pages/typescript/models/exceptions/moodle-error.md) |



