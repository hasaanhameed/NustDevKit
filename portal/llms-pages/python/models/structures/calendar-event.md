# Calendar Event

Source: /#/python/x-redirect/JTI0bSUyRkNhbGVuZGFyRXZlbnQ

A calendar action event tied to a course activity (e.g., an assignment deadline).

*This model accepts additional fields of type Any.*


# Class Name

`CalendarEvent`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | Unique calendar event identifier. |
| `name` | `str` | Required | Display name of the calendar event. |
| `description` | `str` | Required | HTML description body of the event. |
| `descriptionformat` | `int` | Required | Text format of the description (1 = HTML). |
| `location` | `str` | Required | Physical or virtual location of the event; empty string if not specified. |
| `categoryid` | `int` | Optional | Course category ID; null if not a category event. |
| `groupid` | `int` | Optional | Group ID if the event is group-specific; null otherwise. |
| `userid` | `int` | Optional | User ID if the event is user-specific; null otherwise. |
| `repeatid` | `int` | Optional | ID of the repeat group for recurring events; null if not recurring. |
| `eventcount` | `int` | Optional | Total number of events in the repeat group; null if not applicable. |
| `component` | `str` | Required | Moodle component that created the event (e.g., 'mod_assign'). |
| `modulename` | `str` | Required | Short name of the Moodle activity module (e.g., 'assign'). |
| `instance` | `int` | Required | The course module instance ID. |
| `eventtype` | `str` | Required | Type of the event (e.g., 'due', 'open', 'close'). |
| `timestart` | `int` | Required | Event start time as Unix timestamp. |
| `timeduration` | `int` | Required | Duration in seconds; 0 for point-in-time events. |
| `timesort` | `int` | Required | Sort timestamp used for ordering events. |
| `visible` | `int` | Required | Visibility flag for a calendar event. 1 means the event is visible; 0 means it is hidden. |
| `timemodified` | `int` | Required | Last modification time as Unix timestamp. |
| `icon` | [`EventIcon`](/llms-pages/python/models/structures/event-icon.md) | Required | Icon metadata for a calendar event. |
| `course` | [`Course`](/llms-pages/python/models/structures/course.md) | Required | An enrolled course. |
| `subscription` | [`EventSubscription`](/llms-pages/python/models/structures/event-subscription.md) | Required | Subscription display settings for a calendar event. |
| `canedit` | `bool` | Required | Whether the current user can edit this event. |
| `candelete` | `bool` | Required | Whether the current user can delete this event. |
| `deleteurl` | `str` | Required | URL to delete this calendar event. |
| `editurl` | `str` | Required | URL to edit the underlying course module associated with this event. |
| `viewurl` | `str` | Required | URL to view this event on the calendar. |
| `formattedtime` | `str` | Required | HTML-formatted human-readable event time string. |
| `isactionevent` | `bool` | Required | Whether this is an action event requiring user interaction. |
| `iscourseevent` | `bool` | Required | Whether this event is associated with a specific course. |
| `iscategoryevent` | `bool` | Required | Whether this event is associated with a course category. |
| `groupname` | `str` | Optional | Name of the group for group-specific events; null otherwise. |
| `normalisedeventtype` | `str` | Required | Normalised event type identifier used for display grouping. |
| `normalisedeventtypetext` | `str` | Required | Human-readable label for the normalised event type. |
| `action` | [`EventAction`](/llms-pages/python/models/structures/event-action.md) | Optional | Primary action button metadata for a calendar event. |
| `url` | `str` | Required | Direct URL to the course activity associated with this event. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |


# Example

```python
import jsonpickle

from nustlmsapi.models.calendar_event import CalendarEvent
from nustlmsapi.models.course import Course
from nustlmsapi.models.event_icon import EventIcon
from nustlmsapi.models.event_subscription import EventSubscription

calendar_event = CalendarEvent(
    id=149885,
    name='Lab 1 BSCS 13C is due',
    description='<p dir="ltr">Lab 1 BSCS 13C<br /></p>',
    descriptionformat=1,
    location=None,
    component='mod_assign',
    modulename='assign',
    instance=999404,
    eventtype='due',
    timestart=1706900340,
    timeduration=0,
    timesort=1706900340,
    visible=226,
    timemodified=1779088440,
    icon=EventIcon(
        key='icon',
        component='assign',
        alttext='Activity event',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    course=Course(
        id=49900,
        fullname='CS-212 Object Oriented Programming BSCS-13 2K23 ABC',
        shortname='CS-212-Sp\'24 BSCS-13 2K23 ABC',
        idnumber=None,
        summary=None,
        summaryformat=1,
        startdate=1706468400,
        enddate=1717362000,
        visible=True,
        fullnamedisplay='CS-212 Object Oriented Programming BSCS-13 2K23 ABC',
        viewurl='https://lms.nust.edu.pk/portal/course/view.php?id=49900',
        progress=21,
        hasprogress=True,
        isfavourite=False,
        hidden=False,
        showshortname=False,
        coursecategory='2nd Semester (SP-2024)',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    subscription=EventSubscription(
        displayeventsource=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    canedit=False,
    candelete=False,
    deleteurl='https://lms.nust.edu.pk/portal/calendar/delete.php?id=149885&course=49900',
    editurl='https://lms.nust.edu.pk/portal/course/mod.php?update=999404&return=1&sesskey=XXXX',
    viewurl='https://lms.nust.edu.pk/portal/calendar/view.php?view=day&course=49900&time=1706900340',
    formattedtime='<span class="dimmed_text">Friday, 2 February, 11:59 PM</span>',
    isactionevent=True,
    iscourseevent=False,
    iscategoryevent=False,
    normalisedeventtype='course',
    normalisedeventtypetext='Course event',
    url='https://lms.nust.edu.pk/portal/mod/assign/view.php?id=999404',
    categoryid=228,
    groupid=210,
    userid=214,
    repeatid=158,
    eventcount=122,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```



