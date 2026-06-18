# Fetch Notifications Request

Source: /#/java/x-redirect/JTI0bSUyRkZldGNoTm90aWZpY2F0aW9uc1JlcXVlc3Q

Request parameters for fetching site-level notifications.

*This model accepts additional fields of type Object.*


# Class Name

`FetchNotificationsRequest`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Contextid` | `int` | Required | Moodle context ID for which to fetch notifications. The user context ID can be found in the user profile image URL path segment. | int getContextid() | setContextid(int contextid) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import java.io.IOException;
import pk.edu.nust.lms.ApiHelper;
import pk.edu.nust.lms.models.FetchNotificationsRequest;

FetchNotificationsRequest fetchNotificationsRequest = new FetchNotificationsRequest.Builder(
    1583361
)
.additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
.build();
```



