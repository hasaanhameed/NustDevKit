# Get Recent Courses Request

Source: /#/net-standard-library/x-redirect/JTI0bSUyRkdldFJlY2VudENvdXJzZXNSZXF1ZXN0

Request parameters for retrieving recently accessed courses.

*This model accepts additional fields of type object.*


# Class Name

`GetRecentCoursesRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Limit` | `int` | Required | Maximum number of courses to return.<br><br>**Default**: `10` |
| `AdditionalProperties` | `object this[string key]` | Optional | - |


# Example

```csharp
using NustLmsApi.Standard.Models;
using NustLmsApi.Standard.Utilities;

GetRecentCoursesRequest getRecentCoursesRequest = new GetRecentCoursesRequest
{
    Limit = 10,
    ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
};
```



