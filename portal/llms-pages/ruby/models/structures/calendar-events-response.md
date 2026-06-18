# Calendar Events Response

Source: /#/ruby/x-redirect/JTI0bSUyRkNhbGVuZGFyRXZlbnRzUmVzcG9uc2U

A list of calendar events with pagination boundary IDs.

*This model accepts additional fields of type Object.*


# Class Name

`CalendarEventsResponse`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `events` | [`Array[CalendarEvent]`](/llms-pages/ruby/models/structures/calendar-event.md) | Required | List of calendar action events for the current result set. |
| `firstid` | `Integer` | Required | Event ID of the first item in the result set. |
| `lastid` | `Integer` | Required | Event ID of the last item in the result set. |
| `additional_properties` | `Hash[String, Object]` | Optional | - |


# Example

```ruby
calendar_events_response = CalendarEventsResponse.new(
  events: [
    CalendarEvent.new(
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
      visible: 96,
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
      categoryid: 154,
      groupid: 84,
      userid: 88,
      repeatid: 28,
      eventcount: 248,
      additional_properties: {
        'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
      }
    )
  ],
  firstid: 149885,
  lastid: 151886,
  additional_properties: {
    'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
  }
)
```



