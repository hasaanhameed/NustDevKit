# Popup Notifications Response

Source: /#/java/x-redirect/JTI0bSUyRlBvcHVwTm90aWZpY2F0aW9uc1Jlc3BvbnNl

Response envelope for the popup-notifications endpoint.

*This model accepts additional fields of type Object.*


# Class Name

`PopupNotificationsResponse`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Notifications` | [`List<Notification>`](/llms-pages/java/models/structures/notification.md) | Required | List of popup notifications for the user. | List<Notification> getNotifications() | setNotifications(List<Notification> notifications) |
| `Unreadcount` | `int` | Required | Total number of unread notifications for the user. | int getUnreadcount() | setUnreadcount(int unreadcount) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import java.io.IOException;
import java.util.Arrays;
import m18000.m0.m0.m127.ApiHelper;
import m18000.m0.m0.m127.models.Notification;
import m18000.m0.m0.m127.models.PopupNotificationsResponse;

PopupNotificationsResponse popupNotificationsResponse = new PopupNotificationsResponse.Builder(
    Arrays.asList(
        new Notification.Builder(
            4857819,
            234567,
            123456,
            "CS-101 Introduction to Computing: Lab 3 Submission Deadline",
            "CS-101 Introduction to Computing: Lab 3 Submission Deadline",
            "<p>John Doe posted in CS-101 Introduction to Computing...</p>",
            "fullmessage8",
            2,
            "fullmessagehtml4",
            "John Doe posted in CS-101 Introduction to Computing...",
            "https://lms.nust.edu.pk/portal/mod/forum/discuss.php?d=41767#p52342",
            "Lab Sessional Finalization - (DL - Section D & E)",
            1780045085,
            "19 days ago",
            false,
            false,
            "https://lms.nust.edu.pk/portal/theme/image.php/moove/mod_forum/1778048051/icon",
            "mod_forum",
            "posts",
            "{\"cmid\":\"1272420\",\"instance\":\"62569\",\"discussionid\":\"41767\"}"
        )
        .timeread(152)
        .additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
        .build()
    ),
    1
)
.additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
.build();
```



