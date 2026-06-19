# Custom Field

Source: /#/java/x-redirect/JTI0bSUyRkN1c3RvbUZpZWxk

A custom profile field value attached to a user.

*This model accepts additional fields of type Object.*


# Class Name

`CustomField`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Type` | `String` | Required | Data type of the custom field (e.g., 'text', 'select'). | String getType() | setType(String type) |
| `Value` | `String` | Required | Value stored in the custom field. | String getValue() | setValue(String value) |
| `Name` | `String` | Required | Display label of the custom field. | String getName() | setName(String name) |
| `Shortname` | `String` | Required | Machine-readable shortname identifier for the custom field. | String getShortname() | setShortname(String shortname) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import java.io.IOException;
import m18000.m0.m0.m127.ApiHelper;
import m18000.m0.m0.m127.models.CustomField;

CustomField customField = new CustomField.Builder(
    "text",
    "SEECS",
    "Institute",
    "institution"
)
.additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
.build();
```



