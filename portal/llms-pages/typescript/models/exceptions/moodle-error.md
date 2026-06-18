# Moodle Error

Source: /#/typescript/x-redirect/JTI0bSUyRk1vb2RsZUVycm9y

Error returned by the LMS on a failed operation.

*This model accepts additional fields of type unknown.*


# Class Name

`MoodleError`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errorcode` | `string \| undefined` | Optional | Machine-readable error code identifier. |
| `message` | `string \| undefined` | Optional | Human-readable error description. |
| `link` | `string \| undefined` | Optional | Redirect URL for the user; empty string if not applicable. |
| `moreinfourl` | `string \| undefined` | Optional | URL to additional error documentation; empty string if not available. |
| `debuginfo` | `string \| undefined` | Optional | Additional debug information; empty string when not in debug mode. |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
try {
  // make the API call
} catch (error) {
  if (error instanceof MoodleError) {
    console.log(error.result);
  }
}
```



