# Notification

Source: /#/ruby/x-redirect/JTI0bSUyRk5vdGlmaWNhdGlvbg

A popup notification message delivered to a user.

*This model accepts additional fields of type Object.*


# Class Name

`Notification`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `Integer` | Required | Unique notification identifier. |
| `useridfrom` | `Integer` | Required | User ID of the sender. |
| `useridto` | `Integer` | Required | User ID of the recipient. |
| `subject` | `String` | Required | Subject line of the notification. |
| `shortenedsubject` | `String` | Required | Shortened version of the notification subject for compact display. |
| `text` | `String` | Required | Short HTML excerpt of the notification. |
| `fullmessage` | `String` | Required | Full plain-text body of the notification. |
| `fullmessageformat` | `Integer` | Required | Format identifier for fullmessagehtml (2 = Markdown source). |
| `fullmessagehtml` | `String` | Required | Full HTML body of the notification email. |
| `smallmessage` | `String` | Required | Short plain-text preview of the notification. |
| `contexturl` | `String` | Required | URL to the relevant context for this notification (e.g., a forum post). |
| `contexturlname` | `String` | Required | Human-readable label for the context URL link. |
| `timecreated` | `Integer` | Required | Unix timestamp when the notification was created. |
| `timecreatedpretty` | `String` | Required | Human-readable relative time string (e.g., '19 days ago'). |
| `timeread` | `Integer` | Optional | Unix timestamp when the notification was read; null if unread. |
| `read` | `TrueClass \| FalseClass` | Required | Whether the notification has been read by the recipient. |
| `deleted` | `TrueClass \| FalseClass` | Required | Whether the notification has been deleted by the recipient. |
| `iconurl` | `String` | Required | URL to the icon image representing the notification source. |
| `component` | `String` | Required | Moodle component that generated the notification (e.g., 'mod_forum'). |
| `eventtype` | `String` | Required | Event type within the component that triggered the notification (e.g., 'posts'). |
| `customdata` | `String` | Required | JSON-encoded string with additional notification metadata (cmid, instance, discussionid, postid, etc.). |
| `additional_properties` | `Hash[String, Object]` | Optional | - |


# Example

```ruby
notification = Notification.new(
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
  additional_properties: {
    'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
  }
)
```



