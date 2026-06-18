# Moodle Error

Source: /#/php/x-redirect/JTI0bSUyRk1vb2RsZUVycm9y

Error returned by the LMS on a failed operation.

*This model accepts additional fields of type array.*


# Class Name

`MoodleErrorException`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `errorcode` | `?string` | Optional | Machine-readable error code identifier. | getErrorcode(): ?string | setErrorcode(?string errorcode): void |
| `message` | `?string` | Optional | Human-readable error description. | getMessage(): ?string | setMessage(?string message): void |
| `link` | `?string` | Optional | Redirect URL for the user; empty string if not applicable. | getLink(): ?string | setLink(?string link): void |
| `moreinfourl` | `?string` | Optional | URL to additional error documentation; empty string if not available. | getMoreinfourl(): ?string | setMoreinfourl(?string moreinfourl): void |
| `debuginfo` | `?string` | Optional | Additional debug information; empty string when not in debug mode. | getDebuginfo(): ?string | setDebuginfo(?string debuginfo): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |



