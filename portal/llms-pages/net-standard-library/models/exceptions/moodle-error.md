# Moodle Error

Source: /#/net-standard-library/x-redirect/JTI0bSUyRk1vb2RsZUVycm9y

Error returned by the LMS on a failed operation.

*This model accepts additional fields of type object.*


# Class Name

`MoodleErrorException`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Errorcode` | `string` | Optional | Machine-readable error code identifier. |
| `MessageProperty` | `string` | Optional | Human-readable error description. |
| `Link` | `string` | Optional | Redirect URL for the user; empty string if not applicable. |
| `Moreinfourl` | `string` | Optional | URL to additional error documentation; empty string if not available. |
| `Debuginfo` | `string` | Optional | Additional debug information; empty string when not in debug mode. |
| `AdditionalProperties` | `object this[string key]` | Optional | - |


# Example

```csharp
try
{
    // make the API call
}
catch (ApiException e)
{
    if (e is MoodleErrorException)
    {
        // TODO: Handle MoodleErrorException
        Console.WriteLine(e.Message);
    }
}
```



