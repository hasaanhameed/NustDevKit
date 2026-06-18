# Calendar Event

Source: /#/go/x-redirect/JTI0bSUyRkNhbGVuZGFyRXZlbnQ

A calendar action event tied to a course activity (e.g., an assignment deadline).

*This model accepts additional fields of type interface{}.*


# Class Name

`CalendarEvent`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Id` | `int` | Required | Unique calendar event identifier. |
| `Name` | `string` | Required | Display name of the calendar event. |
| `Description` | `string` | Required | HTML description body of the event. |
| `Descriptionformat` | `int` | Required | Text format of the description (1 = HTML). |
| `Location` | `string` | Required | Physical or virtual location of the event; empty string if not specified. |
| `Categoryid` | `models.Optional[int]` | Optional | Course category ID; null if not a category event. |
| `Groupid` | `models.Optional[int]` | Optional | Group ID if the event is group-specific; null otherwise. |
| `Userid` | `models.Optional[int]` | Optional | User ID if the event is user-specific; null otherwise. |
| `Repeatid` | `models.Optional[int]` | Optional | ID of the repeat group for recurring events; null if not recurring. |
| `Eventcount` | `models.Optional[int]` | Optional | Total number of events in the repeat group; null if not applicable. |
| `Component` | `string` | Required | Moodle component that created the event (e.g., 'mod_assign'). |
| `Modulename` | `string` | Required | Short name of the Moodle activity module (e.g., 'assign'). |
| `Instance` | `int` | Required | The course module instance ID. |
| `Eventtype` | `string` | Required | Type of the event (e.g., 'due', 'open', 'close'). |
| `Timestart` | `int` | Required | Event start time as Unix timestamp. |
| `Timeduration` | `int` | Required | Duration in seconds; 0 for point-in-time events. |
| `Timesort` | `int` | Required | Sort timestamp used for ordering events. |
| `Visible` | `int` | Required | Visibility flag for a calendar event. 1 means the event is visible; 0 means it is hidden. |
| `Timemodified` | `int` | Required | Last modification time as Unix timestamp. |
| `Icon` | [`models.EventIcon`](/llms-pages/go/models/structures/event-icon.md) | Required | Icon metadata for a calendar event. |
| `Course` | [`models.Course`](/llms-pages/go/models/structures/course.md) | Required | An enrolled course. |
| `Subscription` | [`models.EventSubscription`](/llms-pages/go/models/structures/event-subscription.md) | Required | Subscription display settings for a calendar event. |
| `Canedit` | `bool` | Required | Whether the current user can edit this event. |
| `Candelete` | `bool` | Required | Whether the current user can delete this event. |
| `Deleteurl` | `string` | Required | URL to delete this calendar event. |
| `Editurl` | `string` | Required | URL to edit the underlying course module associated with this event. |
| `Viewurl` | `string` | Required | URL to view this event on the calendar. |
| `Formattedtime` | `string` | Required | HTML-formatted human-readable event time string. |
| `Isactionevent` | `bool` | Required | Whether this is an action event requiring user interaction. |
| `Iscourseevent` | `bool` | Required | Whether this event is associated with a specific course. |
| `Iscategoryevent` | `bool` | Required | Whether this event is associated with a course category. |
| `Groupname` | `models.Optional[string]` | Optional | Name of the group for group-specific events; null otherwise. |
| `Normalisedeventtype` | `string` | Required | Normalised event type identifier used for display grouping. |
| `Normalisedeventtypetext` | `string` | Required | Human-readable label for the normalised event type. |
| `Action` | [`*models.EventAction`](/llms-pages/go/models/structures/event-action.md) | Optional | Primary action button metadata for a calendar event. |
| `Url` | `string` | Required | Direct URL to the course activity associated with this event. |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
package main

import (
    "nustLmsApi/models"
)

func main() {
    calendarEvent := models.CalendarEvent{
        Id:                      149885,
        Name:                    "Lab 1 BSCS 13C is due",
        Description:             "<p dir=\"ltr\">Lab 1 BSCS 13C<br /></p>",
        Descriptionformat:       1,
        Location:                "",
        Categoryid:              models.NewOptional(models.ToPointer(164)),
        Groupid:                 models.NewOptional(models.ToPointer(74)),
        Userid:                  models.NewOptional(models.ToPointer(178)),
        Repeatid:                models.NewOptional(models.ToPointer(38)),
        Eventcount:              models.NewOptional(models.ToPointer(2)),
        Component:               "mod_assign",
        Modulename:              "assign",
        Instance:                999404,
        Eventtype:               "due",
        Timestart:               1706900340,
        Timeduration:            0,
        Timesort:                1706900340,
        Visible:                 106,
        Timemodified:            1779088440,
        Icon:                    models.EventIcon{
            Key:                   "icon",
            Component:             "assign",
            Alttext:               "Activity event",
            AdditionalProperties:  map[string]interface{}{
                "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
            },
        },
        Course:                  models.Course{
            Id:                    49900,
            Fullname:              "CS-212 Object Oriented Programming BSCS-13 2K23 ABC",
            Shortname:             "CS-212-Sp'24 BSCS-13 2K23 ABC",
            Idnumber:              "",
            Summary:               "",
            Summaryformat:         1,
            Startdate:             1706468400,
            Enddate:               1717362000,
            Visible:               true,
            Fullnamedisplay:       "CS-212 Object Oriented Programming BSCS-13 2K23 ABC",
            Viewurl:               "https://lms.nust.edu.pk/portal/course/view.php?id=49900",
            Progress:              21,
            Hasprogress:           true,
            Isfavourite:           false,
            Hidden:                false,
            Showshortname:         false,
            Coursecategory:        "2nd Semester (SP-2024)",
            AdditionalProperties:  map[string]interface{}{
                "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
            },
        },
        Subscription:            models.EventSubscription{
            Displayeventsource:    false,
            AdditionalProperties:  map[string]interface{}{
                "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
            },
        },
        Canedit:                 false,
        Candelete:               false,
        Deleteurl:               "https://lms.nust.edu.pk/portal/calendar/delete.php?id=149885&course=49900",
        Editurl:                 "https://lms.nust.edu.pk/portal/course/mod.php?update=999404&return=1&sesskey=XXXX",
        Viewurl:                 "https://lms.nust.edu.pk/portal/calendar/view.php?view=day&course=49900&time=1706900340",
        Formattedtime:           "<span class=\"dimmed_text\">Friday, 2 February, 11:59 PM</span>",
        Isactionevent:           true,
        Iscourseevent:           false,
        Iscategoryevent:         false,
        Normalisedeventtype:     "course",
        Normalisedeventtypetext: "Course event",
        Url:                     "https://lms.nust.edu.pk/portal/mod/assign/view.php?id=999404",
        AdditionalProperties:    map[string]interface{}{
            "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
        },
    }

}
```



