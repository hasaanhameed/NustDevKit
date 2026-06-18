# Calendar Events Response

Source: /#/net-standard-library/x-redirect/JTI0bSUyRkNhbGVuZGFyRXZlbnRzUmVzcG9uc2U

A list of calendar events with pagination boundary IDs.

*This model accepts additional fields of type object.*


# Class Name

`CalendarEventsResponse`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Events` | [`List<CalendarEvent>`](/llms-pages/net-standard-library/models/structures/calendar-event.md) | Required | List of calendar action events for the current result set. |
| `Firstid` | `int` | Required | Event ID of the first item in the result set. |
| `Lastid` | `int` | Required | Event ID of the last item in the result set. |
| `AdditionalProperties` | `object this[string key]` | Optional | - |


# Example

```csharp
using NustLmsApi.Standard.Models;
using NustLmsApi.Standard.Utilities;
using System.Collections.Generic;

CalendarEventsResponse calendarEventsResponse = new CalendarEventsResponse
{
    Events = new List<CalendarEvent>
    {
        new CalendarEvent
        {
            Id = 149885,
            Name = "Lab 1 BSCS 13C is due",
            Description = "<p dir=\"ltr\">Lab 1 BSCS 13C<br /></p>",
            Descriptionformat = 1,
            Location = null,
            Component = "mod_assign",
            Modulename = "assign",
            Instance = 999404,
            Eventtype = "due",
            Timestart = 1706900340,
            Timeduration = 0,
            Timesort = 1706900340,
            Visible = 96,
            Timemodified = 1779088440,
            Icon = new EventIcon
            {
                Key = "icon",
                Component = "assign",
                Alttext = "Activity event",
                ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
            },
            Course = new Course
            {
                Id = 49900,
                Fullname = "CS-212 Object Oriented Programming BSCS-13 2K23 ABC",
                Shortname = "CS-212-Sp'24 BSCS-13 2K23 ABC",
                Idnumber = null,
                Summary = null,
                Summaryformat = 1,
                Startdate = 1706468400,
                Enddate = 1717362000,
                Visible = true,
                Fullnamedisplay = "CS-212 Object Oriented Programming BSCS-13 2K23 ABC",
                Viewurl = "https://lms.nust.edu.pk/portal/course/view.php?id=49900",
                Progress = 21,
                Hasprogress = true,
                Isfavourite = false,
                Hidden = false,
                Showshortname = false,
                Coursecategory = "2nd Semester (SP-2024)",
                ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
            },
            Subscription = new EventSubscription
            {
                Displayeventsource = false,
                ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
            },
            Canedit = false,
            Candelete = false,
            Deleteurl = "https://lms.nust.edu.pk/portal/calendar/delete.php?id=149885&course=49900",
            Editurl = "https://lms.nust.edu.pk/portal/course/mod.php?update=999404&return=1&sesskey=XXXX",
            Viewurl = "https://lms.nust.edu.pk/portal/calendar/view.php?view=day&course=49900&time=1706900340",
            Formattedtime = "<span class=\"dimmed_text\">Friday, 2 February, 11:59 PM</span>",
            Isactionevent = true,
            Iscourseevent = false,
            Iscategoryevent = false,
            Normalisedeventtype = "course",
            Normalisedeventtypetext = "Course event",
            Url = "https://lms.nust.edu.pk/portal/mod/assign/view.php?id=999404",
            Categoryid = 154,
            Groupid = 84,
            Userid = 88,
            Repeatid = 28,
            Eventcount = 248,
            ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
        },
    },
    Firstid = 149885,
    Lastid = 151886,
    ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
};
```



