# Calendar Event

Source: /#/java/x-redirect/JTI0bSUyRkNhbGVuZGFyRXZlbnQ

A calendar action event. On NUST LMS these represent deadlines — the due date for an assignment, lab, quiz, or other submission tied to a course activity.

*This model accepts additional fields of type Object.*


# Class Name

`CalendarEvent`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Id` | `int` | Required | Unique calendar event identifier. | int getId() | setId(int id) |
| `Name` | `String` | Required | Display name of the calendar event. | String getName() | setName(String name) |
| `Description` | `String` | Required | HTML description body of the event. | String getDescription() | setDescription(String description) |
| `Descriptionformat` | `int` | Required | Text format of the description (1 = HTML). | int getDescriptionformat() | setDescriptionformat(int descriptionformat) |
| `Location` | `String` | Required | Physical or virtual location of the event; empty string if not specified. | String getLocation() | setLocation(String location) |
| `Categoryid` | `Integer` | Optional | Course category ID; null if not a category event. | Integer getCategoryid() | setCategoryid(Integer categoryid) |
| `Groupid` | `Integer` | Optional | Group ID if the event is group-specific; null otherwise. | Integer getGroupid() | setGroupid(Integer groupid) |
| `Userid` | `Integer` | Optional | User ID if the event is user-specific; null otherwise. | Integer getUserid() | setUserid(Integer userid) |
| `Repeatid` | `Integer` | Optional | ID of the repeat group for recurring events; null if not recurring. | Integer getRepeatid() | setRepeatid(Integer repeatid) |
| `Eventcount` | `Integer` | Optional | Total number of events in the repeat group; null if not applicable. | Integer getEventcount() | setEventcount(Integer eventcount) |
| `Component` | `String` | Required | Moodle component that created the event (e.g., 'mod_assign'). | String getComponent() | setComponent(String component) |
| `Modulename` | `String` | Required | Short name of the Moodle activity module (e.g., 'assign'). | String getModulename() | setModulename(String modulename) |
| `Instance` | `int` | Required | The course module instance ID. | int getInstance() | setInstance(int instance) |
| `Eventtype` | `String` | Required | Type of the event (e.g., 'due', 'open', 'close'). | String getEventtype() | setEventtype(String eventtype) |
| `Timestart` | `int` | Required | Event start time as Unix timestamp. | int getTimestart() | setTimestart(int timestart) |
| `Timeduration` | `int` | Required | Duration in seconds; 0 for point-in-time events. | int getTimeduration() | setTimeduration(int timeduration) |
| `Timesort` | `int` | Required | Sort timestamp used for ordering events. | int getTimesort() | setTimesort(int timesort) |
| `Visible` | `int` | Required | Visibility flag for a calendar event. 1 means the event is visible; 0 means it is hidden. | int getVisible() | setVisible(int visible) |
| `Timemodified` | `int` | Required | Last modification time as Unix timestamp. | int getTimemodified() | setTimemodified(int timemodified) |
| `Icon` | [`EventIcon`](/llms-pages/java/models/structures/event-icon.md) | Required | Icon metadata for a calendar event. | EventIcon getIcon() | setIcon(EventIcon icon) |
| `Course` | [`Course`](/llms-pages/java/models/structures/course.md) | Required | An enrolled course. | Course getCourse() | setCourse(Course course) |
| `Subscription` | [`EventSubscription`](/llms-pages/java/models/structures/event-subscription.md) | Required | Subscription display settings for a calendar event. | EventSubscription getSubscription() | setSubscription(EventSubscription subscription) |
| `Canedit` | `boolean` | Required | Whether the current user can edit this event. | boolean getCanedit() | setCanedit(boolean canedit) |
| `Candelete` | `boolean` | Required | Whether the current user can delete this event. | boolean getCandelete() | setCandelete(boolean candelete) |
| `Deleteurl` | `String` | Required | URL to delete this calendar event. | String getDeleteurl() | setDeleteurl(String deleteurl) |
| `Editurl` | `String` | Required | URL to edit the underlying course module associated with this event. | String getEditurl() | setEditurl(String editurl) |
| `Viewurl` | `String` | Required | URL to view this event on the calendar. | String getViewurl() | setViewurl(String viewurl) |
| `Formattedtime` | `String` | Required | HTML-formatted human-readable event time string. | String getFormattedtime() | setFormattedtime(String formattedtime) |
| `Isactionevent` | `boolean` | Required | Whether this is an action event requiring user interaction. | boolean getIsactionevent() | setIsactionevent(boolean isactionevent) |
| `Iscourseevent` | `boolean` | Required | Whether this event is associated with a specific course. | boolean getIscourseevent() | setIscourseevent(boolean iscourseevent) |
| `Iscategoryevent` | `boolean` | Required | Whether this event is associated with a course category. | boolean getIscategoryevent() | setIscategoryevent(boolean iscategoryevent) |
| `Groupname` | `String` | Optional | Name of the group for group-specific events; null otherwise. | String getGroupname() | setGroupname(String groupname) |
| `Normalisedeventtype` | `String` | Required | Normalised event type identifier used for display grouping. | String getNormalisedeventtype() | setNormalisedeventtype(String normalisedeventtype) |
| `Normalisedeventtypetext` | `String` | Required | Human-readable label for the normalised event type. | String getNormalisedeventtypetext() | setNormalisedeventtypetext(String normalisedeventtypetext) |
| `Action` | [`EventAction`](/llms-pages/java/models/structures/event-action.md) | Optional | Primary action button metadata for a calendar event. | EventAction getAction() | setAction(EventAction action) |
| `Url` | `String` | Required | Direct URL to the course activity associated with this event. | String getUrl() | setUrl(String url) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import java.io.IOException;
import m18000.m0.m0.m127.ApiHelper;
import m18000.m0.m0.m127.models.CalendarEvent;
import m18000.m0.m0.m127.models.Course;
import m18000.m0.m0.m127.models.EventIcon;
import m18000.m0.m0.m127.models.EventSubscription;

CalendarEvent calendarEvent = new CalendarEvent.Builder(
    149885,
    "Lab 1 BSCS 13C is due",
    "<p dir=\"ltr\">Lab 1 BSCS 13C<br /></p>",
    1,
    null,
    "mod_assign",
    "assign",
    999404,
    "due",
    1706900340,
    0,
    1706900340,
    106,
    1779088440,
    new EventIcon.Builder(
        "icon",
        "assign",
        "Activity event"
    )
    .additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
    .build(),
    new Course.Builder(
        49900,
        "CS-212 Object Oriented Programming BSCS-13 2K23 ABC",
        "CS-212-Sp'24 BSCS-13 2K23 ABC",
        null,
        null,
        1,
        1706468400,
        1717362000,
        true,
        "CS-212 Object Oriented Programming BSCS-13 2K23 ABC",
        "https://lms.nust.edu.pk/portal/course/view.php?id=49900",
        21,
        true,
        false,
        false,
        false,
        "2nd Semester (SP-2024)"
    )
    .additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
    .build(),
    new EventSubscription.Builder(
        false
    )
    .additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
    .build(),
    false,
    false,
    "https://lms.nust.edu.pk/portal/calendar/delete.php?id=149885&course=49900",
    "https://lms.nust.edu.pk/portal/course/mod.php?update=999404&return=1&sesskey=XXXX",
    "https://lms.nust.edu.pk/portal/calendar/view.php?view=day&course=49900&time=1706900340",
    "<span class=\"dimmed_text\">Friday, 2 February, 11:59 PM</span>",
    true,
    false,
    false,
    "course",
    "Course event",
    "https://lms.nust.edu.pk/portal/mod/assign/view.php?id=999404"
)
.categoryid(164)
.groupid(74)
.userid(178)
.repeatid(38)
.eventcount(2)
.additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
.build();
```



