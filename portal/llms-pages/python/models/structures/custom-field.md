# Custom Field

Source: /#/python/x-redirect/JTI0bSUyRkN1c3RvbUZpZWxk

A custom profile field value attached to a user.

*This model accepts additional fields of type Any.*


# Class Name

`CustomField`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Required | Data type of the custom field (e.g., 'text', 'select'). |
| `value` | `str` | Required | Value stored in the custom field. |
| `name` | `str` | Required | Display label of the custom field. |
| `shortname` | `str` | Required | Machine-readable shortname identifier for the custom field. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |


# Example

```python
import jsonpickle

from nustlmsapi.models.custom_field import CustomField

custom_field = CustomField(
    mtype='text',
    value='SEECS',
    name='Institute',
    shortname='institution',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```



