# Get Site Info

Source: /#/go/x-redirect/JTI0ZSUyRkFjY291bnQlMkZnZXRTaXRlSW5mbw

Returns your identity (user ID, username, full name, profile picture) and basic site information. Use this to discover your own `userid` — required by other endpoints such as popup notifications (`useridto`).
Moodle method: `core_webservice_get_site_info`

```go
GetSiteInfo(
    ctx context.Context) (
    models.ApiResponse[models.SiteInfo],
    error)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/go/getting-started/sdk-quickstart/authorization.md)


# Response Type

**200**: Your account and site information.

This method returns an [`ApiResponse`](/llms-pages/go/sdk-infrastructure/utilities/apiresponse.md) instance. The `Data` property of this instance returns the response data which is of type [models.SiteInfo](/llms-pages/go/models/structures/site-info.md).


# Example Usage

```go
ctx := context.Background()

apiResponse, err := accountApi.GetSiteInfo(ctx)
if err != nil {
    switch typedErr := err.(type) {
        case *errors.MoodleError:
            log.Fatalln("MoodleErrorException: ", typedErr)
        default:
            log.Fatalln(err)
    }
} else {
    // Printing the result and response
    fmt.Println(apiResponse.Data)
    fmt.Println(apiResponse.Response.StatusCode)
}
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleErrorException`](/llms-pages/go/models/exceptions/moodle-error.md) |



