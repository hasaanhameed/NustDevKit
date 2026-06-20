# Get User Preferences Request

Source: /#/typescript/x-redirect/JTI0bSUyRkdldFVzZXJQcmVmZXJlbmNlc1JlcXVlc3Q

Request parameters for retrieving user preferences.

*This model accepts additional fields of type unknown.*


# Interface Name

`GetUserPreferencesRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `userid` | `number` | Required | ID of the user whose preferences to retrieve. |
| `name` | `string \| undefined` | Optional | Specific preference name to retrieve. Omit to retrieve all preferences. |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
import { GetUserPreferencesRequest } from 'nust-lms-apilib';

const getUserPreferencesRequest: GetUserPreferencesRequest = {
  userid: 123456,
  name: 'name6',
  additionalProperties: {
    'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
  },
};
```



