# Moodle Error

Source: /#/python/x-redirect/JTI0bSUyRk1vb2RsZUVycm9y

Error returned by the LMS on a failed operation.

*This model accepts additional fields of type Any.*


# Class Name

`MoodleErrorException`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errorcode` | `str` | Optional | Machine-readable error code identifier. |
| `message` | `str` | Optional | Human-readable error description. |
| `link` | `str` | Optional | Redirect URL for the user; empty string if not applicable. |
| `moreinfourl` | `str` | Optional | URL to additional error documentation; empty string if not available. |
| `debuginfo` | `str` | Optional | Additional debug information; empty string when not in debug mode. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |


# Example

```python
try:
    # make the API call
except MoodleErrorException as e:
    print(e)
except ApiException as e:
    print(e)
```



