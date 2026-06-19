# Auth Login 401 Error

Source: /#/java/x-redirect/JTI0bSUyRkF1dGglMjUyMExvZ2luJTI1MjA0MDElMjUyMEVycm9y

*This model accepts additional fields of type Object.*


# Class Name

`AuthLogin401ErrorException`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Detail` | `String` | Optional | - | String getDetail() | setDetail(String detail) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
try {
    // make the API call
} catch (AuthLogin401ErrorException e) {
    e.printStackTrace();
} catch (ApiException e) {
    e.printStackTrace();
}
```



