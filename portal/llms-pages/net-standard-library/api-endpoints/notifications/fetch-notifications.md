# Fetch Notifications

Source: /#/net-standard-library/x-redirect/JTI0ZSUyRk5vdGlmaWNhdGlvbnMlMkZmZXRjaE5vdGlmaWNhdGlvbnM

Returns pending site-level notifications for the given Moodle context. Returns an empty array when there are no pending notifications.
Moodle method: `core_fetch_notifications`

```csharp
FetchNotificationsAsync(
    Models.FetchNotificationsRequest body)
```


# Authentication

This endpoint requires [SessKey](/llms-pages/net-standard-library/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`FetchNotificationsRequest`](/llms-pages/net-standard-library/models/structures/fetch-notifications-request.md) | Body, Required | Parameters specifying the context to fetch notifications for. |


# Response Type

**200**: Array of site notifications (empty array when none are pending).

This method returns an [`ApiResponse`](/llms-pages/net-standard-library/sdk-infrastructure/utilities/apiresponse.md) instance. The `Data` property of this instance returns the response data which is of type [List<Models.SiteNotification>](/llms-pages/net-standard-library/models/structures/site-notification.md).


# Example Usage

```csharp
FetchNotificationsRequest body = new FetchNotificationsRequest
{
    Contextid = 1583361,
};

try
{
    ApiResponse<List<SiteNotification>> result = await notificationsApi.FetchNotificationsAsync(body);
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



