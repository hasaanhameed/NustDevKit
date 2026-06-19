# Get Users by Field Request

Source: /#/java/x-redirect/JTI0bSUyRkdldFVzZXJzQnlGaWVsZFJlcXVlc3Q

Request parameters for retrieving user profiles by a profile field value.

*This model accepts additional fields of type Object.*


# Class Name

`GetUsersByFieldRequest`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Field` | [`UserProfileField`](/llms-pages/java/models/enumerations/user-profile-field.md) | Required | User profile field to match against when searching for users. | UserProfileField getField() | setField(UserProfileField field) |
| `Values` | `List<String>` | Required | List of field values to look up. All values must be provided as strings even when the field is numeric (e.g., "162154" for an integer ID). | List<String> getValues() | setValues(List<String> values) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
import java.io.IOException;
import java.util.Arrays;
import m18000.m0.m0.m127.ApiHelper;
import m18000.m0.m0.m127.models.GetUsersByFieldRequest;
import m18000.m0.m0.m127.models.UserProfileField;

GetUsersByFieldRequest getUsersByFieldRequest = new GetUsersByFieldRequest.Builder(
    UserProfileField.ID,
    Arrays.asList(
        "162154"
    )
)
.additionalProperty("exampleAdditionalProperty", ApiHelper.deserialize("{\"key1\":\"val1\",\"key2\":\"val2\"}"))
.build();
```



