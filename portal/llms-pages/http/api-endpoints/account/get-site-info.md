# Get Site Info

Source: /#/http/x-redirect/JTI0ZSUyRkFjY291bnQlMkZnZXRTaXRlSW5mbw

Returns your identity (user ID, username, full name, profile picture) and basic site information. Use this to discover your own `userid` — required by other endpoints such as popup notifications (`useridto`).
Moodle method: `core_webservice_get_site_info`

```http
GET /service/core_webservice_get_site_info
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/http/getting-started/sdk-quickstart/authorization.md)


# Response Type

**200**: Your account and site information.

[`Site Info`](/llms-pages/http/models/structures/site-info.md)


# Example Usage

```bash
curl -X GET \
  --url 'http://127.0.0.1:8000/service/core_webservice_get_site_info'  \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer AccessToken'
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleError_ErrorException`](/llms-pages/http/models/exceptions/moodle-error-error.md) |



