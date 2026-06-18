# Custom Field

Source: /#/typescript/x-redirect/JTI0bSUyRkN1c3RvbUZpZWxk

A custom profile field value attached to a user.

*This model accepts additional fields of type unknown.*


# Interface Name

`CustomField`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `type` | `string` | Required | Data type of the custom field (e.g., 'text', 'select'). |
| `value` | `string` | Required | Value stored in the custom field. |
| `name` | `string` | Required | Display label of the custom field. |
| `shortname` | `string` | Required | Machine-readable shortname identifier for the custom field. |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
import { CustomField } from 'nust-lms-apilib';

const customField: CustomField = {
  type: 'text',
  value: 'SEECS',
  name: 'Institute',
  shortname: 'institution',
  additionalProperties: {
    'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
  },
};
```



