# Recent Course Fields

Source: /#/ruby/x-redirect/JTI0bSUyRlJlY2VudENvdXJzZUZpZWxkcw

Additional fields specific to recently accessed courses.

*This model accepts additional fields of type Object.*


# Class Name

`RecentCourseFields`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `timeaccess` | `Integer` | Required | Unix timestamp of the user's most recent access to this course. |
| `additional_properties` | `Hash[String, Object]` | Optional | - |


# Example

```ruby
recent_course_fields = RecentCourseFields.new(
  timeaccess: 1781632422,
  additional_properties: {
    'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
  }
)
```



