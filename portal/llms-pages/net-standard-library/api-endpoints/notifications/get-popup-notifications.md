# Get Popup Notifications

Source: /#/net-standard-library/x-redirect/JTI0ZSUyRk5vdGlmaWNhdGlvbnMlMkZnZXRQb3B1cE5vdGlmaWNhdGlvbnM

Returns the most recent popup notifications sent to a user, with support for pagination. Also returns the total count of unread notifications.
Moodle method: `message_popup_get_popup_notifications`

```csharp
GetPopupNotificationsAsync(
    Models.GetPopupNotificationsRequest body)
```


# Authentication

This endpoint requires [SessKey](/llms-pages/net-standard-library/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetPopupNotificationsRequest`](/llms-pages/net-standard-library/models/structures/get-popup-notifications-request.md) | Body, Required | Parameters for the popup notifications request. |


# Response Type

**200**: Popup notifications and total unread count.

This method returns an [`ApiResponse`](/llms-pages/net-standard-library/sdk-infrastructure/utilities/apiresponse.md) instance. The `Data` property of this instance returns the response data which is of type [Models.PopupNotificationsResponse](/llms-pages/net-standard-library/models/structures/popup-notifications-response.md).


# Example Usage

```csharp
GetPopupNotificationsRequest body = new GetPopupNotificationsRequest
{
    Useridto = "162154",
    Limit = 20,
    Offset = 0,
};

try
{
    ApiResponse<PopupNotificationsResponse> result = await notificationsApi.GetPopupNotificationsAsync(body);
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



