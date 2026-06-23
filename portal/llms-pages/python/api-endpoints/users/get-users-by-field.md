# Get Users by Field

Source: /#/python/x-redirect/JTI0ZSUyRlVzZXJzJTJGZ2V0VXNlcnNCeUZpZWxk

Retrieves one or more user profiles by matching a specific profile field. Commonly used to look up the authenticated user's own profile by their ID.
Moodle method: `core_user_get_users_by_field`

```python
def get_users_by_field(self,
                      field,
                      values)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/python/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field` | [`UserProfileField`](/llms-pages/python/models/enumerations/user-profile-field.md) | Query, Required | User profile field to match against when searching for users. |
| `values` | `List[str]` | Query, Required | List of field values to look up. All values must be provided as strings even when the field is numeric (e.g., "123456" for an integer ID). |


# Response Type

**200**: List of matching user profiles.

This method returns an [`ApiResponse`](/llms-pages/python/sdk-infrastructure/utilities/apiresponse.md) instance. The `body` property of this instance returns the response data which is of type [`List[UserProfile]`](/llms-pages/python/models/structures/user-profile.md).


# Example Usage

```python
field = UserProfileField.ID

values = [
    'values0',
    'values1',
    'values2'
]

result = users_api.get_users_by_field(
    field,
    values
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleErrorException`](/llms-pages/python/models/exceptions/moodle-error.md) |



