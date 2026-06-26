# Get Site Info

Source: /#/python/x-redirect/JTI0ZSUyRkFjY291bnQlMkZnZXRTaXRlSW5mbw

Returns your identity (user ID, username, full name, profile picture) and basic site information. Use this to discover your own `userid` — required by other endpoints such as popup notifications (`useridto`).
Moodle method: `core_webservice_get_site_info`

```python
def get_site_info(self)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/python/getting-started/sdk-quickstart/authorization.md)


# Response Type

**200**: Your account and site information.

This method returns an [`ApiResponse`](/llms-pages/python/sdk-infrastructure/utilities/apiresponse.md) instance. The `body` property of this instance returns the response data which is of type [`SiteInfo`](/llms-pages/python/models/structures/site-info.md).


# Example Usage

```python
result = account_api.get_site_info()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleErrorException`](/llms-pages/python/models/exceptions/moodle-error.md) |



