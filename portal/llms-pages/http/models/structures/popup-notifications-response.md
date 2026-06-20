# Popup Notifications Response

Source: /#/http/x-redirect/JTI0bSUyRlBvcHVwTm90aWZpY2F0aW9uc1Jlc3BvbnNl

Response envelope for the popup-notifications endpoint.

*This model accepts additional fields of type Object.*


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notifications` | [`array<Notification>`](/llms-pages/http/models/structures/notification.md) | Required | List of popup notifications for the user. |
| `unreadcount` | `Number` | Required | Total number of unread notifications for the user. |
| `additionalProperties` | `Object` | Optional | - |


# Example (as JSON)

```json
{
  "notifications": [
    {
      "id": 4857819,
      "useridfrom": 234567,
      "useridto": 123456,
      "subject": "CS-101 Introduction to Computing: Lab 3 Submission Deadline",
      "shortenedsubject": "CS-101 Introduction to Computing: Lab 3 Submission Deadline",
      "text": "<p>John Doe posted in CS-101 Introduction to Computing...</p>",
      "fullmessage": "fullmessage8",
      "fullmessageformat": 2,
      "fullmessagehtml": "fullmessagehtml4",
      "smallmessage": "John Doe posted in CS-101 Introduction to Computing...",
      "contexturl": "https://lms.nust.edu.pk/portal/mod/forum/discuss.php?d=41767#p52342",
      "contexturlname": "Lab Sessional Finalization - (DL - Section D & E)",
      "timecreated": 1780045085,
      "timecreatedpretty": "19 days ago",
      "read": false,
      "deleted": false,
      "iconurl": "https://lms.nust.edu.pk/portal/theme/image.php/moove/mod_forum/1778048051/icon",
      "component": "mod_forum",
      "eventtype": "posts",
      "customdata": "{\"cmid\":\"1272420\",\"instance\":\"62569\",\"discussionid\":\"41767\"}",
      "timeread": 152,
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "unreadcount": 1,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```



