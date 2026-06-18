# Get Popup Notifications Request

Source: /#/typescript/x-redirect/JTI0bSUyRkdldFBvcHVwTm90aWZpY2F0aW9uc1JlcXVlc3Q

Request parameters for retrieving popup notifications for a user.

*This model accepts additional fields of type unknown.*


# Interface Name

`GetPopupNotificationsRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `useridto` | `string` | Required | ID of the recipient user, passed as a string. |
| `limit` | `number` | Required | Maximum number of notifications to return. |
| `offset` | `number` | Required | Pagination offset.<br><br>**Default**: `0` |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
import { GetPopupNotificationsRequest } from 'nust-lms-apilib';

const getPopupNotificationsRequest: GetPopupNotificationsRequest = {
  useridto: '162154',
  limit: 20,
  offset: 0,
  additionalProperties: {
    'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
  },
};
```



