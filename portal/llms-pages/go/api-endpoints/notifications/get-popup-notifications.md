# Get Popup Notifications

Source: /#/go/x-redirect/JTI0ZSUyRk5vdGlmaWNhdGlvbnMlMkZnZXRQb3B1cE5vdGlmaWNhdGlvbnM

Returns the most recent popup notifications sent to a user, with support for pagination. Also returns the total count of unread notifications.
Moodle method: `message_popup_get_popup_notifications`

```go
GetPopupNotifications(
    ctx context.Context,
    body models.GetPopupNotificationsRequest) (
    models.ApiResponse[models.PopupNotificationsResponse],
    error)
```


# Authentication

This endpoint requires [SessKey](/llms-pages/go/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`models.GetPopupNotificationsRequest`](/llms-pages/go/models/structures/get-popup-notifications-request.md) | Body, Required | Parameters for the popup notifications request. |


# Response Type

**200**: Popup notifications and total unread count.

This method returns an [`ApiResponse`](/llms-pages/go/sdk-infrastructure/utilities/apiresponse.md) instance. The `Data` property of this instance returns the response data which is of type [models.PopupNotificationsResponse](/llms-pages/go/models/structures/popup-notifications-response.md).


# Example Usage

```go
ctx := context.Background()

body := models.GetPopupNotificationsRequest{
    Useridto:              "162154",
    Limit:                 20,
    Offset:                0,
}

apiResponse, err := notificationsApi.GetPopupNotifications(ctx, body)
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



