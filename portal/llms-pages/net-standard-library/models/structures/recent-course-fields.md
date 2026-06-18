# Recent Course Fields

Source: /#/net-standard-library/x-redirect/JTI0bSUyRlJlY2VudENvdXJzZUZpZWxkcw

Additional fields specific to recently accessed courses.

*This model accepts additional fields of type object.*


# Class Name

`RecentCourseFields`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Timeaccess` | `int` | Required | Unix timestamp of the user's most recent access to this course. |
| `AdditionalProperties` | `object this[string key]` | Optional | - |


# Example

```csharp
using NustLmsApi.Standard.Models;
using NustLmsApi.Standard.Utilities;

RecentCourseFields recentCourseFields = new RecentCourseFields
{
    Timeaccess = 1781632422,
    ["exampleAdditionalProperty"] = ApiHelper.JsonDeserialize<object>("{\"key1\":\"val1\",\"key2\":\"val2\"}"),
};
```



