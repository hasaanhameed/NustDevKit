# Get User Preferences

Source: /#/php/x-redirect/JTI0ZSUyRlVzZXJzJTJGZ2V0VXNlclByZWZlcmVuY2Vz

Returns all stored preference key/value pairs for the specified user. Optionally filter to a single preference by name.
Moodle method: `core_user_get_user_preferences`

```php
function getUserPreferences(int $userid, ?string $name = null): ApiResponse
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/php/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `userid` | `int` | Query, Required | ID of the user whose preferences to retrieve. |
| `name` | `?string` | Query, Optional | Specific preference name to retrieve. Omit to retrieve all preferences. |


# Response Type

**200**: User preferences list and optional warnings.

This method returns an [`ApiResponse`](/llms-pages/php/sdk-infrastructure/utilities/apiresponse.md) instance. The `getResult()` method on this instance returns the response data which is of type [`UserPreferencesResponse`](/llms-pages/php/models/structures/user-preferences-response.md).


# Example Usage

```php
$userid = 44;

$usersApi = $client->getUsersApi();
$apiResponse = $usersApi->getUserPreferences($userid);

// Extracting response status code
var_dump($apiResponse->getStatusCode());
// Extracting response headers
var_dump($apiResponse->getHeaders());

if ($apiResponse->isSuccess()) {
    echo 'UserPreferencesResponse:';
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



