# Get Popup Notifications

Source: /#/java/x-redirect/JTI0ZSUyRk5vdGlmaWNhdGlvbnMlMkZnZXRQb3B1cE5vdGlmaWNhdGlvbnM

Returns the most recent popup notifications sent to a user, with support for pagination. Also returns the total count of unread notifications.
Moodle method: `message_popup_get_popup_notifications`

```java
CompletableFuture<ApiResponse<PopupNotificationsResponse>> getPopupNotificationsAsync(
    final GetPopupNotificationsRequest body)
```


# Authentication

This endpoint requires [SessKey](/llms-pages/java/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetPopupNotificationsRequest`](/llms-pages/java/models/structures/get-popup-notifications-request.md) | Body, Required | Parameters for the popup notifications request. |


# Response Type

**200**: Popup notifications and total unread count.

This method returns an [`ApiResponse`](/llms-pages/java/sdk-infrastructure/utilities/apiresponse.md) instance. The `getResult()` getter of this instance returns the response data which is of type [`PopupNotificationsResponse`](/llms-pages/java/models/structures/popup-notifications-response.md).


# Example Usage

```java
GetPopupNotificationsRequest body = new GetPopupNotificationsRequest.Builder(
    "162154",
    20,
    0
)
.build();

notificationsApi.getPopupNotificationsAsync(body).thenAccept(result -> {
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



