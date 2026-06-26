# Get Site Info

Source: /#/java/x-redirect/JTI0ZSUyRkFjY291bnQlMkZnZXRTaXRlSW5mbw

Returns your identity (user ID, username, full name, profile picture) and basic site information. Use this to discover your own `userid` — required by other endpoints such as popup notifications (`useridto`).
Moodle method: `core_webservice_get_site_info`

```java
CompletableFuture<ApiResponse<SiteInfo>> getSiteInfoAsync()
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/java/getting-started/sdk-quickstart/authorization.md)


# Response Type

**200**: Your account and site information.

This method returns an [`ApiResponse`](/llms-pages/java/sdk-infrastructure/utilities/apiresponse.md) instance. The `getResult()` getter of this instance returns the response data which is of type [`SiteInfo`](/llms-pages/java/models/structures/site-info.md).


# Example Usage

```java
accountApi.getSiteInfoAsync().thenAccept(result -> {
    // TODO success callback handler
    System.out.println(result);
}).exceptionally(exception -> {
    Throwable cause = exception.getCause();

    if (cause instanceof MoodleErrorException) {
        MoodleErrorException moodleErrorException = (MoodleErrorException) cause;
        moodleErrorException.printStackTrace();
    } else {
        // fallback for unexpected errors
        exception.printStackTrace();
    }

    return null;
});
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleErrorException`](/llms-pages/java/models/exceptions/moodle-error.md) |



