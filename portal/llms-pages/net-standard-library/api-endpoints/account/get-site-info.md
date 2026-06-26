# Get Site Info

Source: /#/net-standard-library/x-redirect/JTI0ZSUyRkFjY291bnQlMkZnZXRTaXRlSW5mbw

Returns your identity (user ID, username, full name, profile picture) and basic site information. Use this to discover your own `userid` — required by other endpoints such as popup notifications (`useridto`).
Moodle method: `core_webservice_get_site_info`

```csharp
GetSiteInfoAsync()
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/net-standard-library/getting-started/sdk-quickstart/authorization.md)


# Response Type

**200**: Your account and site information.

This method returns an [`ApiResponse`](/llms-pages/net-standard-library/sdk-infrastructure/utilities/apiresponse.md) instance. The `Data` property of this instance returns the response data which is of type [Models.SiteInfo](/llms-pages/net-standard-library/models/structures/site-info.md).


# Example Usage

```csharp
try
{
    ApiResponse<SiteInfo> result = await accountApi.GetSiteInfoAsync();
}
catch (ApiException e)
{
    Console.WriteLine(e.Message);
    if (e is MoodleErrorException)
    {
       // TODO: Handle MoodleErrorException exception here
    }
}
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleErrorException`](/llms-pages/net-standard-library/models/exceptions/moodle-error.md) |



