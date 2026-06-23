# Get User Preferences

Source: /#/python/x-redirect/JTI0ZSUyRlVzZXJzJTJGZ2V0VXNlclByZWZlcmVuY2Vz

Returns all stored preference key/value pairs for the specified user. Optionally filter to a single preference by name.
Moodle method: `core_user_get_user_preferences`

```python
def get_user_preferences(self,
                        userid,
                        name=None)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/python/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `userid` | `int` | Query, Required | ID of the user whose preferences to retrieve. |
| `name` | `str` | Query, Optional | Specific preference name to retrieve. Omit to retrieve all preferences. |


# Response Type

**200**: User preferences list and optional warnings.

This method returns an [`ApiResponse`](/llms-pages/python/sdk-infrastructure/utilities/apiresponse.md) instance. The `body` property of this instance returns the response data which is of type [`UserPreferencesResponse`](/llms-pages/python/models/structures/user-preferences-response.md).


# Example Usage

```python
userid = 44

result = users_api.get_user_preferences(userid)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleErrorException`](/llms-pages/python/models/exceptions/moodle-error.md) |



