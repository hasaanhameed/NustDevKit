# Get Calendar Events by Timesort Request

Source: /#/ruby/x-redirect/JTI0bSUyRkdldENhbGVuZGFyRXZlbnRzQnlUaW1lc29ydFJlcXVlc3Q

Request parameters for retrieving calendar action events sorted by time.

*This model accepts additional fields of type Object.*


# Class Name

`GetCalendarEventsByTimesortRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limitnum` | `Integer` | Required | Maximum number of events to return. |
| `timesortfrom` | `Integer` | Required | Only return events with timesort >= this Unix timestamp. Pass 0 for no lower bound. |
| `timesortto` | `Integer` | Optional | Only return events with timesort <= this Unix timestamp. Optional. |
| `aftereventid` | `Integer` | Optional | Return events whose ID is greater than this value (cursor pagination). Optional. |
| `additional_properties` | `Hash[String, Object]` | Optional | - |


# Example

```ruby
get_calendar_events_by_timesort_request = GetCalendarEventsByTimesortRequest.new(
  limitnum: 20,
  timesortfrom: 0,
  timesortto: 182,
  aftereventid: 180,
  additional_properties: {
    'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
  }
)
```



