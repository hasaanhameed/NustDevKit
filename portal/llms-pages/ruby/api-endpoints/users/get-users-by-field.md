# Get Users by Field

Source: /#/ruby/x-redirect/JTI0ZSUyRlVzZXJzJTJGZ2V0VXNlcnNCeUZpZWxk

Retrieves one or more user profiles by matching a specific profile field. Commonly used to look up the authenticated user's own profile by their ID.
Moodle method: `core_user_get_users_by_field`

```ruby
def get_users_by_field(body)
```


# Authentication

This endpoint requires [SessKey](/llms-pages/ruby/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetUsersByFieldRequest`](/llms-pages/ruby/models/structures/get-users-by-field-request.md) | Body, Required | Parameters specifying the profile field and values to match. |


# Response Type

**200**: List of matching user profiles.

This method returns an [`ApiResponse`](/llms-pages/ruby/sdk-infrastructure/utilities/apiresponse.md) instance. The `data` property of this instance returns the response data which is of type [`Array[UserProfile]`](/llms-pages/ruby/models/structures/user-profile.md).


# Example Usage

```ruby
body = GetUsersByFieldRequest.new(
  field: UserProfileField::ID,
  values: [
    '162154'
  ]
)

result = users_api.get_users_by_field(body)

if result.success?
  puts result.data
elsif result.error?
  warn result.errors
end
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleErrorException`](/llms-pages/ruby/models/exceptions/moodle-error.md) |



