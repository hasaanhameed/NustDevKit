# Auth Login 401 Error

Source: /#/go/x-redirect/JTI0bSUyRkF1dGglMjUyMExvZ2luJTI1MjA0MDElMjUyMEVycm9y

*This model accepts additional fields of type interface{}.*


# Class Name

`AuthLogin401ErrorException`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Detail` | `*string` | Optional | - |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
if err != nil {
    switch typedErr := err.(type) {
    case *errors.AuthLogin401ErrorException:
        log.Fatalln(typedErr)
    default:
        log.Fatalln(err)
    }
}
```



