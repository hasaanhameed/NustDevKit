# Get Enrolled Courses by Timeline Request

Source: /#/ruby/x-redirect/JTI0bSUyRkdldEVucm9sbGVkQ291cnNlc0J5VGltZWxpbmVSZXF1ZXN0

Request parameters for retrieving enrolled courses filtered by timeline classification.

*This model accepts additional fields of type Object.*


# Class Name

`GetEnrolledCoursesByTimelineRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `offset` | `Integer` | Required | Zero-based pagination offset.<br><br>**Default**: `0` |
| `limit` | `Integer` | Required | Maximum number of courses to return.<br><br>**Default**: `50` |
| `classification` | [`CourseTimelineClassification`](/llms-pages/ruby/models/enumerations/course-timeline-classification.md) | Required | Timeline classification filter for enrolled courses. |
| `sort` | [`CourseTimelineSortField`](/llms-pages/ruby/models/enumerations/course-timeline-sort-field.md) | Required | Field used to sort enrolled course results. |
| `additional_properties` | `Hash[String, Object]` | Optional | - |


# Example

```ruby
get_enrolled_courses_by_timeline_request = GetEnrolledCoursesByTimelineRequest.new(
  offset: 0,
  limit: 50,
  classification: CourseTimelineClassification::ALLINCLUDINGHIDDEN,
  sort: CourseTimelineSortField::IDNUMBER,
  additional_properties: {
    'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
  }
)
```



