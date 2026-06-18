# Moodle Error

Source: /#/go/x-redirect/JTI0bSUyRk1vb2RsZUVycm9y

Error returned by the LMS on a failed operation.

*This model accepts additional fields of type interface{}.*


# Class Name

`MoodleErrorException`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Errorcode` | `*string` | Optional | Machine-readable error code identifier. |
| `Message` | `*string` | Optional | Human-readable error description. |
| `Link` | `*string` | Optional | Redirect URL for the user; empty string if not applicable. |
| `Moreinfourl` | `*string` | Optional | URL to additional error documentation; empty string if not available. |
| `Debuginfo` | `*string` | Optional | Additional debug information; empty string when not in debug mode. |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
if err != nil {
    switch typedErr := err.(type) {
    case *errors.MoodleErrorException:
        log.Fatalln(typedErr)
    default:
        log.Fatalln(err)
    }
}
```



