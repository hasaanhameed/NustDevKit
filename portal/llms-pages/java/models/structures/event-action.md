# Event Action

Source: /#/java/x-redirect/JTI0bSUyRkV2ZW50QWN0aW9u

Primary action button metadata for a calendar event.

*This model accepts additional fields of type Object.*


# Class Name

`EventAction`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Name` | `String` | Required | Display label for the primary action button. | String getName() | setName(String name) |
| `Url` | `String` | Required | URL the user should navigate to in order to perform the action. | String getUrl() | setUrl(String url) |
| `Itemcount` | `int` | Required | Number of items associated with this action. | int getItemcount() | setItemcount(int itemcount) |
| `Actionable` | `boolean` | Required | Whether the action can currently be taken by the user. | boolean getActionable() | setActionable(boolean actionable) |
| `Showitemcount` | `boolean` | Required | Whether to display the item count alongside the action label. | boolean getShowitemcount() | setShowitemcount(boolean showitemcount) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import java.io.IOException;
import pk.edu.nust.lms.ApiHelper;
import pk.edu.nust.lms.models.EventAction;

EventAction eventAction = new EventAction.Builder(
    "Add submission",
    "https://lms.nust.edu.pk/portal/mod/assign/view.php?id=999404&action=editsubmission",
    1,
    true,
    false
)
.additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
.build();
```



