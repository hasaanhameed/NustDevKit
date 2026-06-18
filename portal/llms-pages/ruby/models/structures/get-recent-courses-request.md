# Get Recent Courses Request

Source: /#/ruby/x-redirect/JTI0bSUyRkdldFJlY2VudENvdXJzZXNSZXF1ZXN0

Request parameters for retrieving recently accessed courses.

*This model accepts additional fields of type Object.*


# Class Name

`GetRecentCoursesRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `Integer` | Required | Maximum number of courses to return.<br><br>**Default**: `10` |
| `additional_properties` | `Hash[String, Object]` | Optional | - |


# Example

```ruby
get_recent_courses_request = GetRecentCoursesRequest.new(
  limit: 10,
  additional_properties: {
    'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
  }
)
```



