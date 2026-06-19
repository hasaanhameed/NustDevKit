# Get Users by Field

Source: /#/php/x-redirect/JTI0ZSUyRlVzZXJzJTJGZ2V0VXNlcnNCeUZpZWxk

Retrieves one or more user profiles by matching a specific profile field. Commonly used to look up the authenticated user's own profile by their ID.
Moodle method: `core_user_get_users_by_field`

```php
function getUsersByField(GetUsersByFieldRequest $body): ApiResponse
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/php/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetUsersByFieldRequest`](/llms-pages/php/models/structures/get-users-by-field-request.md) | Body, Required | Parameters specifying the profile field and values to match. |


# Response Type

**200**: List of matching user profiles.

This method returns an [`ApiResponse`](/llms-pages/php/sdk-infrastructure/utilities/apiresponse.md) instance. The `getResult()` method on this instance returns the response data which is of type [`UserProfile[]`](/llms-pages/php/models/structures/user-profile.md).


# Example Usage

```php
$body = GetUsersByFieldRequestBuilder::init(
    UserProfileField::ID,
    [
        '162154'
    ]
)->build();

$usersApi = $client->getUsersApi();
$apiResponse = $usersApi->getUsersByField($body);

// Extracting response status code
var_dump($apiResponse->getStatusCode());
// Extracting response headers
var_dump($apiResponse->getHeaders());

if ($apiResponse->isSuccess()) {
    echo 'UserProfile[]:';
    var_dump($apiResponse->getResult());
} else {
    $error = $apiResponse->getResult();
    var_dump($error);
}
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleErrorException`](/llms-pages/php/models/exceptions/moodle-error.md) |



