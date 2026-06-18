# Moodle Warning

Source: /#/python/x-redirect/JTI0bSUyRk1vb2RsZVdhcm5pbmc

A non-fatal warning returned alongside a successful response.

*This model accepts additional fields of type Any.*


# Class Name

`MoodleWarning`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item` | `str` | Optional | Item identifier related to the warning; empty string if not applicable. |
| `itemid` | `int` | Optional | Numeric item ID related to the warning; 0 if not applicable. |
| `warningcode` | `str` | Optional | Machine-readable warning code; empty string if no code. |
| `message` | `str` | Optional | Human-readable warning description. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |


# Example

```python
import jsonpickle

from nustlmsapi.models.moodle_warning import MoodleWarning

moodle_warning = MoodleWarning(
    item='item0',
    itemid=0,
    warningcode='warningcode2',
    message='message8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```



