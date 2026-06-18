# Get Users by Field Request

Source: /#/typescript/x-redirect/JTI0bSUyRkdldFVzZXJzQnlGaWVsZFJlcXVlc3Q

Request parameters for retrieving user profiles by a profile field value.

*This model accepts additional fields of type unknown.*


# Interface Name

`GetUsersByFieldRequest`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `field` | [`UserProfileField`](/llms-pages/typescript/models/enumerations/user-profile-field.md) | Required | User profile field to match against when searching for users. |
| `values` | `string[]` | Required | List of field values to look up. All values must be provided as strings even when the field is numeric (e.g., "162154" for an integer ID). |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
import { GetUsersByFieldRequest, UserProfileField } from 'nust-lms-apilib';

const getUsersByFieldRequest: GetUsersByFieldRequest = {
  field: UserProfileField.Id,
  values: [
    '162154'
  ],
  additionalProperties: {
    'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
  },
};
```



