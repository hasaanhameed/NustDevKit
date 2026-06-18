# Get Calendar Events by Course Request

Source: /#/ruby/x-redirect/JTI0bSUyRkdldENhbGVuZGFyRXZlbnRzQnlDb3Vyc2VSZXF1ZXN0

Request parameters for retrieving calendar action events for a specific course.

*This model accepts additional fields of type Object.*


# Class Name

`GetCalendarEventsByCourseRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `courseid` | `Integer` | Required | ID of the course to fetch events for. |
| `timesortfrom` | `Integer` | Optional | Only return events with timesort >= this Unix timestamp. Optional. |
| `timesortto` | `Integer` | Optional | Only return events with timesort <= this Unix timestamp. Optional. |
| `aftereventid` | `Integer` | Optional | Cursor-based pagination — return events after this event ID. Optional. |
| `limitnum` | `Integer` | Optional | Maximum number of events to return. Optional. |
| `additional_properties` | `Hash[String, Object]` | Optional | - |


# Example

```ruby
get_calendar_events_by_course_request = GetCalendarEventsByCourseRequest.new(
  courseid: 49906,
  timesortfrom: 188,
  timesortto: 184,
  aftereventid: 182,
  limitnum: 94,
  additional_properties: {
    'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
  }
)
```



