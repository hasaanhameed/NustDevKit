# Calendar Events Response

Source: /#/go/x-redirect/JTI0bSUyRkNhbGVuZGFyRXZlbnRzUmVzcG9uc2U

A list of calendar events with pagination boundary IDs.

*This model accepts additional fields of type interface{}.*


# Class Name

`CalendarEventsResponse`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Events` | [`[]models.CalendarEvent`](/llms-pages/go/models/structures/calendar-event.md) | Required | List of calendar action events for the current result set. |
| `Firstid` | `int` | Required | Event ID of the first item in the result set. |
| `Lastid` | `int` | Required | Event ID of the last item in the result set. |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
package main

import (
    "nustLmsApi/models"
)

func main() {
    calendarEventsResponse := models.CalendarEventsResponse{
        Events:                []models.CalendarEvent{
            models.CalendarEvent{
                Id:                      149885,
                Name:                    "Lab 1 BSCS 13C is due",
                Description:             "<p dir=\"ltr\">Lab 1 BSCS 13C<br /></p>",
                Descriptionformat:       1,
                Location:                "",
                Categoryid:              models.NewOptional(models.ToPointer(154)),
                Groupid:                 models.NewOptional(models.ToPointer(84)),
                Userid:                  models.NewOptional(models.ToPointer(88)),
                Repeatid:                models.NewOptional(models.ToPointer(28)),
                Eventcount:              models.NewOptional(models.ToPointer(248)),
                Component:               "mod_assign",
                Modulename:              "assign",
                Instance:                999404,
                Eventtype:               "due",
                Timestart:               1706900340,
                Timeduration:            0,
                Timesort:                1706900340,
                Visible:                 96,
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
            },
        },
        Firstid:               149885,
        Lastid:                151886,
        AdditionalProperties:  map[string]interface{}{
            "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
        },
    }

}
```



