# Login Request

Source: /#/typescript/x-redirect/JTI0bSUyRkxvZ2luUmVxdWVzdA

NUST LMS credentials used to obtain a gateway bearer token.

*This model accepts additional fields of type unknown.*


# Interface Name

`LoginRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `username` | `string` | Required | NUST LMS username. |
| `password` | `string` | Required | NUST LMS password. |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
import { LoginRequest } from 'nust-lms-apilib';

const loginRequest: LoginRequest = {
  username: 'johndoe.bscs23seecs',
  password: 'password2',
  additionalProperties: {
    'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
  },
};
```



