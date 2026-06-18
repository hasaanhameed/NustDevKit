# Calendar Event

Source: /#/http/x-redirect/JTI0bSUyRkNhbGVuZGFyRXZlbnQ

A calendar action event tied to a course activity (e.g., an assignment deadline).

*This model accepts additional fields of type Object.*


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `Number` | Required | Unique calendar event identifier. |
| `name` | `String` | Required | Display name of the calendar event. |
| `description` | `String` | Required | HTML description body of the event. |
| `descriptionformat` | `Number` | Required | Text format of the description (1 = HTML). |
| `location` | `String` | Required | Physical or virtual location of the event; empty string if not specified. |
| `categoryid` | `Number` | Optional | Course category ID; null if not a category event. |
| `groupid` | `Number` | Optional | Group ID if the event is group-specific; null otherwise. |
| `userid` | `Number` | Optional | User ID if the event is user-specific; null otherwise. |
| `repeatid` | `Number` | Optional | ID of the repeat group for recurring events; null if not recurring. |
| `eventcount` | `Number` | Optional | Total number of events in the repeat group; null if not applicable. |
| `component` | `String` | Required | Moodle component that created the event (e.g., 'mod_assign'). |
| `modulename` | `String` | Required | Short name of the Moodle activity module (e.g., 'assign'). |
| `instance` | `Number` | Required | The course module instance ID. |
| `eventtype` | `String` | Required | Type of the event (e.g., 'due', 'open', 'close'). |
| `timestart` | `Number` | Required | Event start time as Unix timestamp. |
| `timeduration` | `Number` | Required | Duration in seconds; 0 for point-in-time events. |
| `timesort` | `Number` | Required | Sort timestamp used for ordering events. |
| `visible` | `Number` | Required | Visibility flag for a calendar event. 1 means the event is visible; 0 means it is hidden. |
| `timemodified` | `Number` | Required | Last modification time as Unix timestamp. |
| `icon` | [`Event Icon`](/llms-pages/http/models/structures/event-icon.md) | Required | Icon metadata for a calendar event. |
| `course` | [`Course`](/llms-pages/http/models/structures/course.md) | Required | An enrolled course. |
| `subscription` | [`Event Subscription`](/llms-pages/http/models/structures/event-subscription.md) | Required | Subscription display settings for a calendar event. |
| `canedit` | `Boolean` | Required | Whether the current user can edit this event. |
| `candelete` | `Boolean` | Required | Whether the current user can delete this event. |
| `deleteurl` | `String` | Required | URL to delete this calendar event. |
| `editurl` | `String` | Required | URL to edit the underlying course module associated with this event. |
| `viewurl` | `String` | Required | URL to view this event on the calendar. |
| `formattedtime` | `String` | Required | HTML-formatted human-readable event time string. |
| `isactionevent` | `Boolean` | Required | Whether this is an action event requiring user interaction. |
| `iscourseevent` | `Boolean` | Required | Whether this event is associated with a specific course. |
| `iscategoryevent` | `Boolean` | Required | Whether this event is associated with a course category. |
| `groupname` | `String` | Optional | Name of the group for group-specific events; null otherwise. |
| `normalisedeventtype` | `String` | Required | Normalised event type identifier used for display grouping. |
| `normalisedeventtypetext` | `String` | Required | Human-readable label for the normalised event type. |
| `action` | [`Event Action`](/llms-pages/http/models/structures/event-action.md) | Optional | Primary action button metadata for a calendar event. |
| `url` | `String` | Required | Direct URL to the course activity associated with this event. |
| `additionalProperties` | `Object` | Optional | - |


# Example (as JSON)

```json
{
  "id": 149885,
  "name": "Lab 1 BSCS 13C is due",
  "description": "<p dir=\"ltr\">Lab 1 BSCS 13C<br /></p>",
  "descriptionformat": 1,
  "location": null,
  "component": "mod_assign",
  "modulename": "assign",
  "instance": 999404,
  "eventtype": "due",
  "timestart": 1706900340,
  "timeduration": 0,
  "timesort": 1706900340,
  "visible": 192,
  "timemodified": 1779088440,
  "icon": {
    "key": "icon",
    "component": "assign",
    "alttext": "Activity event",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "course": {
    "id": 49900,
    "fullname": "CS-212 Object Oriented Programming BSCS-13 2K23 ABC",
    "shortname": "CS-212-Sp'24 BSCS-13 2K23 ABC",
    "idnumber": null,
    "summary": null,
    "summaryformat": 1,
    "startdate": 1706468400,
    "enddate": 1717362000,
    "visible": true,
    "fullnamedisplay": "CS-212 Object Oriented Programming BSCS-13 2K23 ABC",
    "viewurl": "https://lms.nust.edu.pk/portal/course/view.php?id=49900",
    "progress": 21,
    "hasprogress": true,
    "isfavourite": false,
    "hidden": false,
    "showshortname": false,
    "coursecategory": "2nd Semester (SP-2024)",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "subscription": {
    "displayeventsource": false,
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "canedit": false,
  "candelete": false,
  "deleteurl": "https://lms.nust.edu.pk/portal/calendar/delete.php?id=149885&course=49900",
  "editurl": "https://lms.nust.edu.pk/portal/course/mod.php?update=999404&return=1&sesskey=XXXX",
  "viewurl": "https://lms.nust.edu.pk/portal/calendar/view.php?view=day&course=49900&time=1706900340",
  "formattedtime": "<span class=\"dimmed_text\">Friday, 2 February, 11:59 PM</span>",
  "isactionevent": true,
  "iscourseevent": false,
  "iscategoryevent": false,
  "normalisedeventtype": "course",
  "normalisedeventtypetext": "Course event",
  "url": "https://lms.nust.edu.pk/portal/mod/assign/view.php?id=999404",
  "categoryid": 6,
  "groupid": 244,
  "userid": 248,
  "repeatid": 124,
  "eventcount": 88,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```



