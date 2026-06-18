# Site Notification

Source: /#/java/x-redirect/JTI0bSUyRlNpdGVOb3RpZmljYXRpb24

A site-level notification (structure varies by type).

*This model accepts additional fields of type Object.*


# Class Name

`SiteNotification`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Id` | `Integer` | Optional | Unique identifier for the site notification. | Integer getId() | setId(Integer id) |
| `Message` | `String` | Optional | Notification message content. | String getMessage() | setMessage(String message) |
| `Type` | `String` | Optional | Notification type identifier. | String getType() | setType(String type) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import java.io.IOException;
import pk.edu.nust.lms.ApiHelper;
import pk.edu.nust.lms.models.SiteNotification;

SiteNotification siteNotification = new SiteNotification.Builder()
    .id(96)
    .message("message8")
    .type("type8")
.additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
    .build();
```



