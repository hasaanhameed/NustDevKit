# Moodle Error

Source: /#/java/x-redirect/JTI0bSUyRk1vb2RsZUVycm9y

Error returned by the LMS on a failed operation.

*This model accepts additional fields of type Object.*


# Class Name

`MoodleErrorException`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `Errorcode` | `String` | Optional | Machine-readable error code identifier. | String getErrorcode() | setErrorcode(String errorcode) |
| `Message` | `String` | Optional | Human-readable error description. | String getMessageField() | setMessageField(String messageField) |
| `Link` | `String` | Optional | Redirect URL for the user; empty string if not applicable. | String getLink() | setLink(String link) |
| `Moreinfourl` | `String` | Optional | URL to additional error documentation; empty string if not available. | String getMoreinfourl() | setMoreinfourl(String moreinfourl) |
| `Debuginfo` | `String` | Optional | Additional debug information; empty string when not in debug mode. | String getDebuginfo() | setDebuginfo(String debuginfo) |
| `AdditionalProperties` | `Map<String, Object>` | Optional | - | Object getAdditionalProperty(String key) | additionalProperty(String key, Object value) |


# Example

```java
try {
    // make the API call
} catch (MoodleErrorException e) {
    e.printStackTrace();
} catch (ApiException e) {
    e.printStackTrace();
}
```



