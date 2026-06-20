# Calendar Event

Source: /#/ruby/x-redirect/JTI0bSUyRkNhbGVuZGFyRXZlbnQ

A calendar action event. On NUST LMS these represent deadlines — the due date for an assignment, lab, quiz, or other submission tied to a course activity.

*This model accepts additional fields of type Object.*


# Class Name

`CalendarEvent`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `Integer` | Required | Unique calendar event identifier. |
| `name` | `String` | Required | Display name of the calendar event. |
| `description` | `String` | Required | HTML description body of the event. |
| `descriptionformat` | `Integer` | Required | Text format of the description (1 = HTML). |
| `location` | `String` | Required | Physical or virtual location of the event; empty string if not specified. |
| `categoryid` | `Integer` | Optional | Course category ID; null if not a category event. |
| `groupid` | `Integer` | Optional | Group ID if the event is group-specific; null otherwise. |
| `userid` | `Integer` | Optional | User ID if the event is user-specific; null otherwise. |
| `repeatid` | `Integer` | Optional | ID of the repeat group for recurring events; null if not recurring. |
| `eventcount` | `Integer` | Optional | Total number of events in the repeat group; null if not applicable. |
| `component` | `String` | Required | Moodle component that created the event (e.g., 'mod_assign'). |
| `modulename` | `String` | Required | Short name of the Moodle activity module (e.g., 'assign'). |
| `instance` | `Integer` | Required | The course module instance ID. |
| `eventtype` | `String` | Required | Type of the event (e.g., 'due', 'open', 'close'). |
| `timestart` | `Integer` | Required | Event start time as Unix timestamp. |
| `timeduration` | `Integer` | Required | Duration in seconds; 0 for point-in-time events. |
| `timesort` | `Integer` | Required | Sort timestamp used for ordering events. |
| `visible` | `Integer` | Required | Visibility flag for a calendar event. 1 means the event is visible; 0 means it is hidden. |
| `timemodified` | `Integer` | Required | Last modification time as Unix timestamp. |
| `icon` | [`EventIcon`](/llms-pages/ruby/models/structures/event-icon.md) | Required | Icon metadata for a calendar event. |
| `course` | [`Course`](/llms-pages/ruby/models/structures/course.md) | Required | An enrolled course. |
| `subscription` | [`EventSubscription`](/llms-pages/ruby/models/structures/event-subscription.md) | Required | Subscription display settings for a calendar event. |
| `canedit` | `TrueClass \| FalseClass` | Required | Whether the current user can edit this event. |
| `candelete` | `TrueClass \| FalseClass` | Required | Whether the current user can delete this event. |
| `deleteurl` | `String` | Required | URL to delete this calendar event. |
| `editurl` | `String` | Required | URL to edit the underlying course module associated with this event. |
| `viewurl` | `String` | Required | URL to view this event on the calendar. |
| `formattedtime` | `String` | Required | HTML-formatted human-readable event time string. |
| `isactionevent` | `TrueClass \| FalseClass` | Required | Whether this is an action event requiring user interaction. |
| `iscourseevent` | `TrueClass \| FalseClass` | Required | Whether this event is associated with a specific course. |
| `iscategoryevent` | `TrueClass \| FalseClass` | Required | Whether this event is associated with a course category. |
| `groupname` | `String` | Optional | Name of the group for group-specific events; null otherwise. |
| `normalisedeventtype` | `String` | Required | Normalised event type identifier used for display grouping. |
| `normalisedeventtypetext` | `String` | Required | Human-readable label for the normalised event type. |
| `action` | [`EventAction`](/llms-pages/ruby/models/structures/event-action.md) | Optional | Primary action button metadata for a calendar event. |
| `url` | `String` | Required | Direct URL to the course activity associated with this event. |
| `additional_properties` | `Hash[String, Object]` | Optional | - |


# Example

```ruby
calendar_event = CalendarEvent.new(
  id: 149885,
  name: 'Lab 1 BSCS 13C is due',
  description: '<p dir="ltr">Lab 1 BSCS 13C<br /></p>',
  descriptionformat: 1,
  location: nil,
  component: 'mod_assign',
  modulename: 'assign',
  instance: 999404,
  eventtype: 'due',
  timestart: 1706900340,
  timeduration: 0,
  timesort: 1706900340,
  visible: 226,
  timemodified: 1779088440,
  icon: EventIcon.new(
    key: 'icon',
    component: 'assign',
    alttext: 'Activity event',
    additional_properties: {
      'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
    }
  ),
  course: Course.new(
    id: 49900,
    fullname: 'CS-212 Object Oriented Programming BSCS-13 2K23 ABC',
    shortname: 'CS-212-Sp\'24 BSCS-13 2K23 ABC',
    idnumber: nil,
    summary: nil,
    summaryformat: 1,
    startdate: 1706468400,
    enddate: 1717362000,
    visible: true,
    fullnamedisplay: 'CS-212 Object Oriented Programming BSCS-13 2K23 ABC',
    viewurl: 'https://lms.nust.edu.pk/portal/course/view.php?id=49900',
    progress: 21,
    hasprogress: true,
    isfavourite: false,
    hidden: false,
    showshortname: false,
    coursecategory: '2nd Semester (SP-2024)',
    additional_properties: {
      'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
    }
  ),
  subscription: EventSubscription.new(
    displayeventsource: false,
    additional_properties: {
      'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
    }
  ),
  canedit: false,
  candelete: false,
  deleteurl: 'https://lms.nust.edu.pk/portal/calendar/delete.php?id=149885&course=49900',
  editurl: 'https://lms.nust.edu.pk/portal/course/mod.php?update=999404&return=1&sesskey=XXXX',
  viewurl: 'https://lms.nust.edu.pk/portal/calendar/view.php?view=day&course=49900&time=1706900340',
  formattedtime: '<span class="dimmed_text">Friday, 2 February, 11:59 PM</span>',
  isactionevent: true,
  iscourseevent: false,
  iscategoryevent: false,
  normalisedeventtype: 'course',
  normalisedeventtypetext: 'Course event',
  url: 'https://lms.nust.edu.pk/portal/mod/assign/view.php?id=999404',
  categoryid: 228,
  groupid: 210,
  userid: 214,
  repeatid: 158,
  eventcount: 122,
  additional_properties: {
    'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
  }
)
```



