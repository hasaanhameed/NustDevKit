# Get Site Info

Source: /#/ruby/x-redirect/JTI0ZSUyRkFjY291bnQlMkZnZXRTaXRlSW5mbw

Returns your identity (user ID, username, full name, profile picture) and basic site information. Use this to discover your own `userid` — required by other endpoints such as popup notifications (`useridto`).
Moodle method: `core_webservice_get_site_info`

```ruby
def get_site_info
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/ruby/getting-started/sdk-quickstart/authorization.md)


# Response Type

**200**: Your account and site information.

This method returns an [`ApiResponse`](/llms-pages/ruby/sdk-infrastructure/utilities/apiresponse.md) instance. The `data` property of this instance returns the response data which is of type [`SiteInfo`](/llms-pages/ruby/models/structures/site-info.md).


# Example Usage

```ruby
result = account_api.get_site_info

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



