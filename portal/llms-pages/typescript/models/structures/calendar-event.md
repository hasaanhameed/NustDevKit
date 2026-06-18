# Calendar Event

Source: /#/typescript/x-redirect/JTI0bSUyRkNhbGVuZGFyRXZlbnQ

A calendar action event tied to a course activity (e.g., an assignment deadline).

*This model accepts additional fields of type unknown.*


# Interface Name

`CalendarEvent`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `number` | Required | Unique calendar event identifier. |
| `name` | `string` | Required | Display name of the calendar event. |
| `description` | `string` | Required | HTML description body of the event. |
| `descriptionformat` | `number` | Required | Text format of the description (1 = HTML). |
| `location` | `string` | Required | Physical or virtual location of the event; empty string if not specified. |
| `categoryid` | `number \| null \| undefined` | Optional | Course category ID; null if not a category event. |
| `groupid` | `number \| null \| undefined` | Optional | Group ID if the event is group-specific; null otherwise. |
| `userid` | `number \| null \| undefined` | Optional | User ID if the event is user-specific; null otherwise. |
| `repeatid` | `number \| null \| undefined` | Optional | ID of the repeat group for recurring events; null if not recurring. |
| `eventcount` | `number \| null \| undefined` | Optional | Total number of events in the repeat group; null if not applicable. |
| `component` | `string` | Required | Moodle component that created the event (e.g., 'mod_assign'). |
| `modulename` | `string` | Required | Short name of the Moodle activity module (e.g., 'assign'). |
| `instance` | `number` | Required | The course module instance ID. |
| `eventtype` | `string` | Required | Type of the event (e.g., 'due', 'open', 'close'). |
| `timestart` | `number` | Required | Event start time as Unix timestamp. |
| `timeduration` | `number` | Required | Duration in seconds; 0 for point-in-time events. |
| `timesort` | `number` | Required | Sort timestamp used for ordering events. |
| `visible` | `number` | Required | Visibility flag for a calendar event. 1 means the event is visible; 0 means it is hidden. |
| `timemodified` | `number` | Required | Last modification time as Unix timestamp. |
| `icon` | [`EventIcon`](/llms-pages/typescript/models/structures/event-icon.md) | Required | Icon metadata for a calendar event. |
| `course` | [`Course`](/llms-pages/typescript/models/structures/course.md) | Required | An enrolled course. |
| `subscription` | [`EventSubscription`](/llms-pages/typescript/models/structures/event-subscription.md) | Required | Subscription display settings for a calendar event. |
| `canedit` | `boolean` | Required | Whether the current user can edit this event. |
| `candelete` | `boolean` | Required | Whether the current user can delete this event. |
| `deleteurl` | `string` | Required | URL to delete this calendar event. |
| `editurl` | `string` | Required | URL to edit the underlying course module associated with this event. |
| `viewurl` | `string` | Required | URL to view this event on the calendar. |
| `formattedtime` | `string` | Required | HTML-formatted human-readable event time string. |
| `isactionevent` | `boolean` | Required | Whether this is an action event requiring user interaction. |
| `iscourseevent` | `boolean` | Required | Whether this event is associated with a specific course. |
| `iscategoryevent` | `boolean` | Required | Whether this event is associated with a course category. |
| `groupname` | `string \| null \| undefined` | Optional | Name of the group for group-specific events; null otherwise. |
| `normalisedeventtype` | `string` | Required | Normalised event type identifier used for display grouping. |
| `normalisedeventtypetext` | `string` | Required | Human-readable label for the normalised event type. |
| `action` | [`EventAction \| undefined`](/llms-pages/typescript/models/structures/event-action.md) | Optional | Primary action button metadata for a calendar event. |
| `url` | `string` | Required | Direct URL to the course activity associated with this event. |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
import { CalendarEvent } from 'nust-lms-apilib';

const calendarEvent: CalendarEvent = {
  id: 149885,
  name: 'Lab 1 BSCS 13C is due',
  description: '<p dir="ltr">Lab 1 BSCS 13C<br /></p>',
  descriptionformat: 1,
  location: '',
  component: 'mod_assign',
  modulename: 'assign',
  instance: 999404,
  eventtype: 'due',
  timestart: 1706900340,
  timeduration: 0,
  timesort: 1706900340,
  visible: 106,
  timemodified: 1779088440,
  icon: {
    key: 'icon',
    component: 'assign',
    alttext: 'Activity event',
    additionalProperties: {
      'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
    },
  },
  course: {
    id: 49900,
    fullname: 'CS-212 Object Oriented Programming BSCS-13 2K23 ABC',
    shortname: 'CS-212-Sp\'24 BSCS-13 2K23 ABC',
    idnumber: '',
    summary: '',
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
    additionalProperties: {
      'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
    },
  },
  subscription: {
    displayeventsource: false,
    additionalProperties: {
      'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
    },
  },
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
  categoryid: 164,
  groupid: 74,
  userid: 178,
  repeatid: 38,
  eventcount: 2,
  additionalProperties: {
    'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
  },
};
```



