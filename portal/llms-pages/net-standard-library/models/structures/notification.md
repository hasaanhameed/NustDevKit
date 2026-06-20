# Notification

Source: /#/net-standard-library/x-redirect/JTI0bSUyRk5vdGlmaWNhdGlvbg

A popup notification message delivered to a user.

*This model accepts additional fields of type object.*


# Class Name

`Notification`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Id` | `int` | Required | Unique notification identifier. |
| `Useridfrom` | `int` | Required | User ID of the sender. |
| `Useridto` | `int` | Required | User ID of the recipient. |
| `Subject` | `string` | Required | Subject line of the notification. |
| `Shortenedsubject` | `string` | Required | Shortened version of the notification subject for compact display. |
| `Text` | `string` | Required | Short HTML excerpt of the notification. |
| `Fullmessage` | `string` | Required | Full plain-text body of the notification. |
| `Fullmessageformat` | `int` | Required | Format identifier for fullmessagehtml (2 = Markdown source). |
| `Fullmessagehtml` | `string` | Required | Full HTML body of the notification email. |
| `Smallmessage` | `string` | Required | Short plain-text preview of the notification. |
| `Contexturl` | `string` | Required | URL to the relevant context for this notification (e.g., a forum post). |
| `Contexturlname` | `string` | Required | Human-readable label for the context URL link. |
| `Timecreated` | `int` | Required | Unix timestamp when the notification was created. |
| `Timecreatedpretty` | `string` | Required | Human-readable relative time string (e.g., '19 days ago'). |
| `Timeread` | `int?` | Optional | Unix timestamp when the notification was read; null if unread. |
| `Read` | `bool` | Required | Whether the notification has been read by the recipient. |
| `Deleted` | `bool` | Required | Whether the notification has been deleted by the recipient. |
| `Iconurl` | `string` | Required | URL to the icon image representing the notification source. |
| `Component` | `string` | Required | Moodle component that generated the notification (e.g., 'mod_forum'). |
| `Eventtype` | `string` | Required | Event type within the component that triggered the notification (e.g., 'posts'). |
| `Customdata` | `string` | Required | JSON-encoded string with additional notification metadata (cmid, instance, discussionid, postid, etc.). |
| `AdditionalProperties` | `object this[string key]` | Optional | - |


# Example

```csharp
using NustLmsApi.Standard.Models;
using NustLmsApi.Standard.Utilities;

Notification notification = new Notification
{
    Id = 4857819,
    Useridfrom = 234567,
    Useridto = 123456,
    Subject = "CS-101 Introduction to Computing: Lab 3 Submission Deadline",
    Shortenedsubject = "CS-101 Introduction to Computing: Lab 3 Submission Deadline",
    Text = "<p>John Doe posted in CS-101 Introduction to Computing...</p>",
    Fullmessage = "fullmessage8",
    Fullmessageformat = 2,
    Fullmessagehtml = "fullmessagehtml6",
    Smallmessage = "John Doe posted in CS-101 Introduction to Computing...",
    Contexturl = "https://lms.nust.edu.pk/portal/mod/forum/discuss.php?d=41767#p52342",
    Contexturlname = "Lab Sessional Finalization - (DL - Section D & E)",
    Timecreated = 1780045085,
    Timecreatedpretty = "19 days ago",
    Read = false,
    Deleted = false,
    Iconurl = "https://lms.nust.edu.pk/portal/theme/image.php/moove/mod_forum/1778048051/icon",
    Component = "mod_forum",
    Eventtype = "posts",
    Customdata = "{\"cmid\":\"1272420\",\"instance\":\"62569\",\"discussionid\":\"41767\"}",
    Timeread = 102,
    ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
};
```



