# Token Response

Source: /#/typescript/x-redirect/JTI0bSUyRlRva2VuUmVzcG9uc2U

Bearer token issued by the gateway after a successful login.

*This model accepts additional fields of type unknown.*


# Interface Name

`TokenResponse`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accessToken` | `string` | Required | JWT to send as `Authorization: Bearer <token>` on subsequent requests. |
| `tokenType` | `string` | Required | **Default**: `'bearer'` |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
import { TokenResponse } from 'nust-lms-apilib';

const tokenResponse: TokenResponse = {
  accessToken: 'access_token2',
  tokenType: 'bearer',
  additionalProperties: {
    'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
  },
};
```



