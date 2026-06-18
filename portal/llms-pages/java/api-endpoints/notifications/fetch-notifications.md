# Fetch Notifications

Source: /#/java/x-redirect/JTI0ZSUyRk5vdGlmaWNhdGlvbnMlMkZmZXRjaE5vdGlmaWNhdGlvbnM

Returns pending site-level notifications for the given Moodle context. Returns an empty array when there are no pending notifications.
Moodle method: `core_fetch_notifications`

```java
CompletableFuture<ApiResponse<List<SiteNotification>>> fetchNotificationsAsync(
    final FetchNotificationsRequest body)
```


# Authentication

This endpoint requires [SessKey](/llms-pages/java/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`FetchNotificationsRequest`](/llms-pages/java/models/structures/fetch-notifications-request.md) | Body, Required | Parameters specifying the context to fetch notifications for. |


# Response Type

**200**: Array of site notifications (empty array when none are pending).

This method returns an [`ApiResponse`](/llms-pages/java/sdk-infrastructure/utilities/apiresponse.md) instance. The `getResult()` getter of this instance returns the response data which is of type [`List<SiteNotification>`](/llms-pages/java/models/structures/site-notification.md).


# Example Usage

```java
FetchNotificationsRequest body = new FetchNotificationsRequest.Builder(
    1583361
)
.build();

notificationsApi.fetchNotificationsAsync(body).thenAccept(result -> {
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



