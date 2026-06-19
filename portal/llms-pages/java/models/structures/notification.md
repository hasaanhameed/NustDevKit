# Notification

Source: /#/java/x-redirect/JTI0bSUyRk5vdGlmaWNhdGlvbg

A popup notification message delivered to a user.

*This model accepts additional fields of type Object.*


# Class Name

`Notification`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Id` | `int` | Required | Unique notification identifier. | int getId() | setId(int id) |
| `Useridfrom` | `int` | Required | User ID of the sender. | int getUseridfrom() | setUseridfrom(int useridfrom) |
| `Useridto` | `int` | Required | User ID of the recipient. | int getUseridto() | setUseridto(int useridto) |
| `Subject` | `String` | Required | Subject line of the notification. | String getSubject() | setSubject(String subject) |
| `Shortenedsubject` | `String` | Required | Shortened version of the notification subject for compact display. | String getShortenedsubject() | setShortenedsubject(String shortenedsubject) |
| `Text` | `String` | Required | Short HTML excerpt of the notification. | String getText() | setText(String text) |
| `Fullmessage` | `String` | Required | Full plain-text body of the notification. | String getFullmessage() | setFullmessage(String fullmessage) |
| `Fullmessageformat` | `int` | Required | Format identifier for fullmessagehtml (2 = Markdown source). | int getFullmessageformat() | setFullmessageformat(int fullmessageformat) |
| `Fullmessagehtml` | `String` | Required | Full HTML body of the notification email. | String getFullmessagehtml() | setFullmessagehtml(String fullmessagehtml) |
| `Smallmessage` | `String` | Required | Short plain-text preview of the notification. | String getSmallmessage() | setSmallmessage(String smallmessage) |
| `Contexturl` | `String` | Required | URL to the relevant context for this notification (e.g., a forum post). | String getContexturl() | setContexturl(String contexturl) |
| `Contexturlname` | `String` | Required | Human-readable label for the context URL link. | String getContexturlname() | setContexturlname(String contexturlname) |
| `Timecreated` | `int` | Required | Unix timestamp when the notification was created. | int getTimecreated() | setTimecreated(int timecreated) |
| `Timecreatedpretty` | `String` | Required | Human-readable relative time string (e.g., '19 days ago'). | String getTimecreatedpretty() | setTimecreatedpretty(String timecreatedpretty) |
| `Timeread` | `Integer` | Optional | Unix timestamp when the notification was read; null if unread. | Integer getTimeread() | setTimeread(Integer timeread) |
| `Read` | `boolean` | Required | Whether the notification has been read by the recipient. | boolean getRead() | setRead(boolean read) |
| `Deleted` | `boolean` | Required | Whether the notification has been deleted by the recipient. | boolean getDeleted() | setDeleted(boolean deleted) |
| `Iconurl` | `String` | Required | URL to the icon image representing the notification source. | String getIconurl() | setIconurl(String iconurl) |
| `Component` | `String` | Required | Moodle component that generated the notification (e.g., 'mod_forum'). | String getComponent() | setComponent(String component) |
| `Eventtype` | `String` | Required | Event type within the component that triggered the notification (e.g., 'posts'). | String getEventtype() | setEventtype(String eventtype) |
| `Customdata` | `String` | Required | JSON-encoded string with additional notification metadata (cmid, instance, discussionid, postid, etc.). | String getCustomdata() | setCustomdata(String customdata) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import java.io.IOException;
import m18000.m0.m0.m127.ApiHelper;
import m18000.m0.m0.m127.models.Notification;

Notification notification = new Notification.Builder(
    4857819,
    198956,
    162154,
    "CS-419-Deep Learning: Lab Sessional Finalization",
    "CS-419-Deep Learning: Lab Sessional Finalization",
    "<p>Areeba Rameen posted in CS-419-Deep Learning...</p>",
    "fullmessage8",
    2,
    "fullmessagehtml6",
    "Areeba Rameen posted in CS-419-Deep Learning...",
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
.timeread(102)
.additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
.build();
```



