# Get Popup Notifications Request

Source: /#/java/x-redirect/JTI0bSUyRkdldFBvcHVwTm90aWZpY2F0aW9uc1JlcXVlc3Q

Request parameters for retrieving popup notifications for a user.

*This model accepts additional fields of type Object.*


# Class Name

`GetPopupNotificationsRequest`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Useridto` | `String` | Required | ID of the recipient user, passed as a string. | String getUseridto() | setUseridto(String useridto) |
| `Limit` | `int` | Required | Maximum number of notifications to return. | int getLimit() | setLimit(int limit) |
| `Offset` | `int` | Required | Pagination offset.<br><br>**Default**: `0` | int getOffset() | setOffset(int offset) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import com.nustdevkit.api.ApiHelper;
import com.nustdevkit.api.models.GetPopupNotificationsRequest;
import java.io.IOException;

GetPopupNotificationsRequest getPopupNotificationsRequest = new GetPopupNotificationsRequest.Builder(
    "123456",
    20,
    0
)
.additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
.build();
```



