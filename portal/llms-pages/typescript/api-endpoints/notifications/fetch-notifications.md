# Fetch Notifications

Source: /#/typescript/x-redirect/JTI0ZSUyRk5vdGlmaWNhdGlvbnMlMkZmZXRjaE5vdGlmaWNhdGlvbnM

Returns pending site-level notifications for the given Moodle context. Returns an empty array when there are no pending notifications.
Moodle method: `core_fetch_notifications`

```ts
async fetchNotifications(
  body: FetchNotificationsRequest,
  requestOptions?: RequestOptions
): Promise<ApiResponse<SiteNotification[]>>
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/typescript/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`FetchNotificationsRequest`](/llms-pages/typescript/models/structures/fetch-notifications-request.md) | Body, Required | Parameters specifying the context to fetch notifications for. |
| `requestOptions` | `RequestOptions \| undefined` | Optional | Pass additional request options. |


# Response Type

**200**: Array of site notifications (empty array when none are pending).

This method returns an [`ApiResponse`](/llms-pages/typescript/sdk-infrastructure/utilities/apiresponse.md) instance. The `result` property of this instance returns the response data which is of type [`SiteNotification[]`](/llms-pages/typescript/models/structures/site-notification.md).


# Example Usage

```ts
const body: FetchNotificationsRequest = {
  contextid: 1583361,
};

try {
  const response = await notificationsApi.fetchNotifications(body);

  // Extracting fully parsed response body.
  console.log(response.result);

  // Extracting response status code.
  console.log(response.statusCode);
  // Extracting response headers.
  console.log(response.headers);
  // Extracting response body of type `string | Stream`
  console.log(response.body);
} catch (error) {
  if (error instanceof ApiError) {
    // Extracting response error status code.
    console.log(error.statusCode);
    // Extracting response error headers.
    console.log(error.headers);
    // Extracting response error body of type `string | Stream`.
    console.log(error.body);
    if (error instanceof MoodleError) {
      console.log(error.result);
    }
  }
}
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleError`](/llms-pages/typescript/models/exceptions/moodle-error.md) |



