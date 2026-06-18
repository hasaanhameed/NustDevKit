# Notification

Source: /#/typescript/x-redirect/JTI0bSUyRk5vdGlmaWNhdGlvbg

A popup notification message delivered to a user.

*This model accepts additional fields of type unknown.*


# Interface Name

`Notification`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `number` | Required | Unique notification identifier. |
| `useridfrom` | `number` | Required | User ID of the sender. |
| `useridto` | `number` | Required | User ID of the recipient. |
| `subject` | `string` | Required | Subject line of the notification. |
| `shortenedsubject` | `string` | Required | Shortened version of the notification subject for compact display. |
| `text` | `string` | Required | Short HTML excerpt of the notification. |
| `fullmessage` | `string` | Required | Full plain-text body of the notification. |
| `fullmessageformat` | `number` | Required | Format identifier for fullmessagehtml (2 = Markdown source). |
| `fullmessagehtml` | `string` | Required | Full HTML body of the notification email. |
| `smallmessage` | `string` | Required | Short plain-text preview of the notification. |
| `contexturl` | `string` | Required | URL to the relevant context for this notification (e.g., a forum post). |
| `contexturlname` | `string` | Required | Human-readable label for the context URL link. |
| `timecreated` | `number` | Required | Unix timestamp when the notification was created. |
| `timecreatedpretty` | `string` | Required | Human-readable relative time string (e.g., '19 days ago'). |
| `timeread` | `number \| null \| undefined` | Optional | Unix timestamp when the notification was read; null if unread. |
| `read` | `boolean` | Required | Whether the notification has been read by the recipient. |
| `deleted` | `boolean` | Required | Whether the notification has been deleted by the recipient. |
| `iconurl` | `string` | Required | URL to the icon image representing the notification source. |
| `component` | `string` | Required | Moodle component that generated the notification (e.g., 'mod_forum'). |
| `eventtype` | `string` | Required | Event type within the component that triggered the notification (e.g., 'posts'). |
| `customdata` | `string` | Required | JSON-encoded string with additional notification metadata (cmid, instance, discussionid, postid, etc.). |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
import { Notification } from 'nust-lms-apilib';

const notification: Notification = {
  id: 4857819,
  useridfrom: 198956,
  useridto: 162154,
  subject: 'CS-419-Deep Learning: Lab Sessional Finalization',
  shortenedsubject: 'CS-419-Deep Learning: Lab Sessional Finalization',
  text: '<p>Areeba Rameen posted in CS-419-Deep Learning...</p>',
  fullmessage: 'fullmessage8',
  fullmessageformat: 2,
  fullmessagehtml: 'fullmessagehtml6',
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
  timeread: 102,
  additionalProperties: {
    'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
  },
};
```



