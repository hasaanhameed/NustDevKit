# Moodle Warning

Source: /#/typescript/x-redirect/JTI0bSUyRk1vb2RsZVdhcm5pbmc

A non-fatal warning returned alongside a successful response.

*This model accepts additional fields of type unknown.*


# Interface Name

`MoodleWarning`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item` | `string \| undefined` | Optional | Item identifier related to the warning; empty string if not applicable. |
| `itemid` | `number \| undefined` | Optional | Numeric item ID related to the warning; 0 if not applicable. |
| `warningcode` | `string \| undefined` | Optional | Machine-readable warning code; empty string if no code. |
| `message` | `string \| undefined` | Optional | Human-readable warning description. |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
import { MoodleWarning } from 'nust-lms-apilib';

const moodleWarning: MoodleWarning = {
  item: 'item6',
  itemid: 0,
  warningcode: 'warningcode6',
  message: 'message4',
  additionalProperties: {
    'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
  },
};
```



