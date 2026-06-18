# Site Notification

Source: /#/typescript/x-redirect/JTI0bSUyRlNpdGVOb3RpZmljYXRpb24

A site-level notification (structure varies by type).

*This model accepts additional fields of type unknown.*


# Interface Name

`SiteNotification`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `number \| undefined` | Optional | Unique identifier for the site notification. |
| `message` | `string \| undefined` | Optional | Notification message content. |
| `type` | `string \| undefined` | Optional | Notification type identifier. |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
import { SiteNotification } from 'nust-lms-apilib';

const siteNotification: SiteNotification = {
  id: 96,
  message: 'message8',
  type: 'type8',
  additionalProperties: {
    'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
  },
};
```



