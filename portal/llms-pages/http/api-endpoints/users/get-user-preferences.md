# Get User Preferences

Source: /#/http/x-redirect/JTI0ZSUyRlVzZXJzJTJGZ2V0VXNlclByZWZlcmVuY2Vz

Returns all stored preference key/value pairs for the specified user. Optionally filter to a single preference by name.
Moodle method: `core_user_get_user_preferences`

```http
GET /service/core_user_get_user_preferences
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/http/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `userid` | `Number` | Query, Required | ID of the user whose preferences to retrieve. |
| `name` | `String` | Query, Optional | Specific preference name to retrieve. Omit to retrieve all preferences. |


# Response Type

**200**: User preferences list and optional warnings.

[`User Preferences Response`](/llms-pages/http/models/structures/user-preferences-response.md)


# Example Usage

```bash
curl -X GET -G \
  --url 'http://127.0.0.1:8000/service/core_user_get_user_preferences'  \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer AccessToken' \
  -d 'userid=44'
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleError_ErrorException`](/llms-pages/http/models/exceptions/moodle-error-error.md) |



