# Popup Notifications Response

Source: /#/typescript/x-redirect/JTI0bSUyRlBvcHVwTm90aWZpY2F0aW9uc1Jlc3BvbnNl

Response envelope for the popup-notifications endpoint.

*This model accepts additional fields of type unknown.*


# Interface Name

`PopupNotificationsResponse`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notifications` | [`Notification[]`](/llms-pages/typescript/models/structures/notification.md) | Required | List of popup notifications for the user. |
| `unreadcount` | `number` | Required | Total number of unread notifications for the user. |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
import { PopupNotificationsResponse } from 'nust-lms-apilib';

const popupNotificationsResponse: PopupNotificationsResponse = {
  notifications: [
    {
      id: 4857819,
      useridfrom: 198956,
      useridto: 162154,
      subject: 'CS-419-Deep Learning: Lab Sessional Finalization',
      shortenedsubject: 'CS-419-Deep Learning: Lab Sessional Finalization',
      text: '<p>Areeba Rameen posted in CS-419-Deep Learning...</p>',
      fullmessage: 'fullmessage8',
      fullmessageformat: 2,
      fullmessagehtml: 'fullmessagehtml4',
      smallmessage: 'Areeba Rameen posted in CS-419-Deep Learning...',
      contexturl: 'https://lms.nust.edu.pk/portal/mod/forum/discuss.php?d=41767#p52342',
      contexturlname: 'Lab Sessional Finalization - (DL - Section D & E)',
      timecreated: 1780045085,
      timecreatedpretty: '19 days ago',
      read: false,
      deleted: false,
      iconurl: 'https://lms.nust.edu.pk/portal/theme/image.php/moove/mod_forum/1778048051/icon',
      component: 'mod_forum',
      eventtype: 'posts',
      customdata: '{"cmid":"1272420","instance":"62569","discussionid":"41767"}',
      timeread: 152,
      additionalProperties: {
        'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
      },
    }
  ],
  unreadcount: 1,
  additionalProperties: {
    'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
  },
};
```



