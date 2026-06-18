# Calendar Events Response

Source: /#/java/x-redirect/JTI0bSUyRkNhbGVuZGFyRXZlbnRzUmVzcG9uc2U

A list of calendar events with pagination boundary IDs.

*This model accepts additional fields of type Object.*


# Class Name

`CalendarEventsResponse`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Events` | [`List<CalendarEvent>`](/llms-pages/java/models/structures/calendar-event.md) | Required | List of calendar action events for the current result set. | List<CalendarEvent> getEvents() | setEvents(List<CalendarEvent> events) |
| `Firstid` | `int` | Required | Event ID of the first item in the result set. | int getFirstid() | setFirstid(int firstid) |
| `Lastid` | `int` | Required | Event ID of the last item in the result set. | int getLastid() | setLastid(int lastid) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import java.io.IOException;
import java.util.Arrays;
import pk.edu.nust.lms.ApiHelper;
import pk.edu.nust.lms.models.CalendarEvent;
import pk.edu.nust.lms.models.CalendarEventsResponse;
import pk.edu.nust.lms.models.Course;
import pk.edu.nust.lms.models.EventIcon;
import pk.edu.nust.lms.models.EventSubscription;

CalendarEventsResponse calendarEventsResponse = new CalendarEventsResponse.Builder(
    Arrays.asList(
        new CalendarEvent.Builder(
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
            96,
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
        .categoryid(154)
        .groupid(84)
        .userid(88)
        .repeatid(28)
        .eventcount(248)
        .additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
        .build()
    ),
    149885,
    151886
)
.additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
.build();
```



