# Get Popup Notifications

Source: /#/php/x-redirect/JTI0ZSUyRk5vdGlmaWNhdGlvbnMlMkZnZXRQb3B1cE5vdGlmaWNhdGlvbnM

Returns the most recent popup notifications sent to a user, with support for pagination. Also returns the total count of unread notifications.
Moodle method: `message_popup_get_popup_notifications`

```php
function getPopupNotifications(string $useridto, int $limit, int $offset): ApiResponse
```


# Authentication

This endpoint requires [BearerAuth](/llms-pages/php/getting-started/sdk-quickstart/authorization.md)


# Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `useridto` | `string` | Query, Required | ID of the recipient user (yourself), passed as a string. Get your numeric user ID from `GET /service/core_webservice_get_site_info`. |
| `limit` | `int` | Query, Required | Maximum number of notifications to return. |
| `offset` | `int` | Query, Required | Pagination offset. |


# Response Type

**200**: Popup notifications and total unread count.

This method returns an [`ApiResponse`](/llms-pages/php/sdk-infrastructure/utilities/apiresponse.md) instance. The `getResult()` method on this instance returns the response data which is of type [`PopupNotificationsResponse`](/llms-pages/php/models/structures/popup-notifications-response.md).


# Example Usage

```php
$useridto = 'useridto2';

$limit = 172;

$offset = 0;

$notificationsApi = $client->getNotificationsApi();
$apiResponse = $notificationsApi->getPopupNotifications(
    $useridto,
    $limit,
    $offset
);

// Extracting response status code
var_dump($apiResponse->getStatusCode());
// Extracting response headers
var_dump($apiResponse->getHeaders());

if ($apiResponse->isSuccess()) {
    echo 'PopupNotificationsResponse:';
    var_dump($apiResponse->getResult());
} else {
    $error = $apiResponse->getResult();
    var_dump($error);
}
```


# Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request or Moodle exception. | [`MoodleErrorException`](/llms-pages/php/models/exceptions/moodle-error.md) |



