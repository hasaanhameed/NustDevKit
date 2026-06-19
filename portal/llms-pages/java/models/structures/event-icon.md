# Event Icon

Source: /#/java/x-redirect/JTI0bSUyRkV2ZW50SWNvbg

Icon metadata for a calendar event.

*This model accepts additional fields of type Object.*


# Class Name

`EventIcon`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Key` | `String` | Required | Icon key name used to locate the icon asset. | String getKey() | setKey(String key) |
| `Component` | `String` | Required | Moodle component that owns the icon (e.g., 'assign'). | String getComponent() | setComponent(String component) |
| `Alttext` | `String` | Required | Accessible alt text for the icon image. | String getAlttext() | setAlttext(String alttext) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import java.io.IOException;
import m18000.m0.m0.m127.ApiHelper;
import m18000.m0.m0.m127.models.EventIcon;

EventIcon eventIcon = new EventIcon.Builder(
    "icon",
    "assign",
    "Activity event"
)
.additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
.build();
```



