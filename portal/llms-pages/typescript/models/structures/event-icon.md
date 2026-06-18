# Event Icon

Source: /#/typescript/x-redirect/JTI0bSUyRkV2ZW50SWNvbg

Icon metadata for a calendar event.

*This model accepts additional fields of type unknown.*


# Interface Name

`EventIcon`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `string` | Required | Icon key name used to locate the icon asset. |
| `component` | `string` | Required | Moodle component that owns the icon (e.g., 'assign'). |
| `alttext` | `string` | Required | Accessible alt text for the icon image. |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
import { EventIcon } from 'nust-lms-apilib';

const eventIcon: EventIcon = {
  key: 'icon',
  component: 'assign',
  alttext: 'Activity event',
  additionalProperties: {
    'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
  },
};
```



