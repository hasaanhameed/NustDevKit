# Auth Login 401 Error

Source: /#/typescript/x-redirect/JTI0bSUyRkF1dGglMjUyMExvZ2luJTI1MjA0MDElMjUyMEVycm9y

*This model accepts additional fields of type unknown.*


# Class Name

`AuthLogin401Error`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `detail` | `string \| undefined` | Optional | - |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
try {
  // make the API call
} catch (error) {
  if (error instanceof AuthLogin401Error) {
    console.log(error.result);
  }
}
```



