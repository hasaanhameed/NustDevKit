# Get Popup Notifications

Source: /#/java/x-redirect/JTI0ZSUyRk5vdGlmaWNhdGlvbnMlMkZnZXRQb3B1cE5vdGlmaWNhdGlvbnM

Returns the most recent popup notifications sent to a user, with support for pagination. Also returns the total count of unread notifications.
Moodle method: `message_popup_get_popup_notifications`

```java
CompletableFuture<ApiResponse<PopupNotificationsResponse>> getPopupNotificationsAsync(
    final String useridto,
    final int limit,
    final int offset)
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/java/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `useridto` | `String` | Query, Required | ID of the recipient user, passed as a string. |
| `limit` | `int` | Query, Required | Maximum number of notifications to return. |
| `offset` | `int` | Query, Required | Pagination offset. |


# Response Type

**200**: Popup notifications and total unread count.

This method returns an [`ApiResponse`](/llms-pages/java/sdk-infrastructure/utilities/apiresponse.md) instance. The `getResult()` getter of this instance returns the response data which is of type [`PopupNotificationsResponse`](/llms-pages/java/models/structures/popup-notifications-response.md).


# Example Usage

```java
String useridto = "useridto2";
int limit = 172;
int offset = 0;

notificationsApi.getPopupNotificationsAsync(useridto, limit, offset).thenAccept(result -> {
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



