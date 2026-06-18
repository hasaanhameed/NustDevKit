# Fetch Notifications Request

Source: /#/typescript/x-redirect/JTI0bSUyRkZldGNoTm90aWZpY2F0aW9uc1JlcXVlc3Q

Request parameters for fetching site-level notifications.

*This model accepts additional fields of type unknown.*


# Interface Name

`FetchNotificationsRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `contextid` | `number` | Required | Moodle context ID for which to fetch notifications. The user context ID can be found in the user profile image URL path segment. |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
import { FetchNotificationsRequest } from 'nust-lms-apilib';

const fetchNotificationsRequest: FetchNotificationsRequest = {
  contextid: 1583361,
  additionalProperties: {
    'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
  },
};
```



