# Get User Preferences

Source: /#/http/x-redirect/JTI0ZSUyRlVzZXJzJTJGZ2V0VXNlclByZWZlcmVuY2Vz

Returns all stored preference key/value pairs for the specified user. Optionally filter to a single preference by name.
Moodle method: `core_user_get_user_preferences`

```http
POST /service/core_user_get_user_preferences
```


# Authentication

This endpoint requires [SessKey](/llms-pages/http/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Get User Preferences Request`](/llms-pages/http/models/structures/get-user-preferences-request.md) | Body, Required | Parameters specifying which user's preferences to retrieve. |


# Response Type

**200**: User preferences list and optional warnings.

[`User Preferences Response`](/llms-pages/http/models/structures/user-preferences-response.md)


# Example Usage

```bash
curl -X POST \
  --url 'https://lms.nust.edu.pk/portal/service/core_user_get_user_preferences?sesskey=sesskey'  \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  --data-raw '{
  "userid": 162154
}'
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleError_ErrorException`](/llms-pages/http/models/exceptions/moodle-error-error.md) |



