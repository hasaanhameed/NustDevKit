# Event Subscription

Source: /#/java/x-redirect/JTI0bSUyRkV2ZW50U3Vic2NyaXB0aW9u

Subscription display settings for a calendar event.

*This model accepts additional fields of type Object.*


# Class Name

`EventSubscription`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Displayeventsource` | `boolean` | Required | Whether to display the event source label on the calendar. | boolean getDisplayeventsource() | setDisplayeventsource(boolean displayeventsource) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import com.nustdevkit.api.ApiHelper;
import com.nustdevkit.api.models.EventSubscription;
import java.io.IOException;

EventSubscription eventSubscription = new EventSubscription.Builder(
    false
)
.additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
.build();
```



