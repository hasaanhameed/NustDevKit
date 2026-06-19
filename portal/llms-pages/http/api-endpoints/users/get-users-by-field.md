# Get Users by Field

Source: /#/http/x-redirect/JTI0ZSUyRlVzZXJzJTJGZ2V0VXNlcnNCeUZpZWxk

Retrieves one or more user profiles by matching a specific profile field. Commonly used to look up the authenticated user's own profile by their ID.
Moodle method: `core_user_get_users_by_field`

```http
POST /service/core_user_get_users_by_field
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/http/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Get Users by Field Request`](/llms-pages/http/models/structures/get-users-by-field-request.md) | Body, Required | Parameters specifying the profile field and values to match. |


# Response Type

**200**: List of matching user profiles.

[`array<User Profile>`](/llms-pages/http/models/structures/user-profile.md)


# Example Usage

```bash
curl -X POST \
  --url 'http://127.0.0.1:8000/service/core_user_get_users_by_field'  \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer AccessToken' \
  --data-raw '{
  "field": "id",
  "values": [
    "162154"
  ]
}'
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleError_ErrorException`](/llms-pages/http/models/exceptions/moodle-error-error.md) |



