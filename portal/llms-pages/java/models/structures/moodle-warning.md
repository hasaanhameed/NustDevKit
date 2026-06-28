# Moodle Warning

Source: /#/java/x-redirect/JTI0bSUyRk1vb2RsZVdhcm5pbmc

A non-fatal warning returned alongside a successful response.

*This model accepts additional fields of type Object.*


# Class Name

`MoodleWarning`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Item` | `String` | Optional | Item identifier related to the warning; empty string if not applicable. | String getItem() | setItem(String item) |
| `Itemid` | `Integer` | Optional | Numeric item ID related to the warning; 0 if not applicable. | Integer getItemid() | setItemid(Integer itemid) |
| `Warningcode` | `String` | Optional | Machine-readable warning code; empty string if no code. | String getWarningcode() | setWarningcode(String warningcode) |
| `Message` | `String` | Optional | Human-readable warning description. | String getMessage() | setMessage(String message) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import com.nustdevkit.api.ApiHelper;
import com.nustdevkit.api.models.MoodleWarning;
import java.io.IOException;

MoodleWarning moodleWarning = new MoodleWarning.Builder()
    .item("item6")
    .itemid(0)
    .warningcode("warningcode6")
    .message("message4")
.additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
    .build();
```



