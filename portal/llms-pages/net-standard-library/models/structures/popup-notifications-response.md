# Popup Notifications Response

Source: /#/net-standard-library/x-redirect/JTI0bSUyRlBvcHVwTm90aWZpY2F0aW9uc1Jlc3BvbnNl

Response envelope for the popup-notifications endpoint.

*This model accepts additional fields of type object.*


# Class Name

`PopupNotificationsResponse`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Notifications` | [`List<Notification>`](/llms-pages/net-standard-library/models/structures/notification.md) | Required | List of popup notifications for the user. |
| `Unreadcount` | `int` | Required | Total number of unread notifications for the user. |
| `AdditionalProperties` | `object this[string key]` | Optional | - |


# Example

```csharp
using NustLmsApi.Standard.Models;
using NustLmsApi.Standard.Utilities;
using System.Collections.Generic;

PopupNotificationsResponse popupNotificationsResponse = new PopupNotificationsResponse
{
    Notifications = new List<Notification>
    {
        new Notification
        {
            Id = 4857819,
            Useridfrom = 234567,
            Useridto = 123456,
            Subject = "CS-101 Introduction to Computing: Lab 3 Submission Deadline",
            Shortenedsubject = "CS-101 Introduction to Computing: Lab 3 Submission Deadline",
            Text = "<p>John Doe posted in CS-101 Introduction to Computing...</p>",
            Fullmessage = "fullmessage8",
            Fullmessageformat = 2,
            Fullmessagehtml = "fullmessagehtml4",
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
            Timeread = 152,
            ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
        },
    },
    Unreadcount = 1,
    ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
};
```



