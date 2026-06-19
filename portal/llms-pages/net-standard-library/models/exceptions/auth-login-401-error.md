# Auth Login 401 Error

Source: /#/net-standard-library/x-redirect/JTI0bSUyRkF1dGglMjUyMExvZ2luJTI1MjA0MDElMjUyMEVycm9y

*This model accepts additional fields of type object.*


# Class Name

`AuthLogin401ErrorException`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Detail` | `string` | Optional | - |
| `AdditionalProperties` | `object this[string key]` | Optional | - |


# Example

```csharp
try
{
    // make the API call
}
catch (ApiException e)
{
    if (e is AuthLogin401ErrorException)
    {
        // TODO: Handle AuthLogin401ErrorException
        Console.WriteLine(e.Message);
    }
}
```



