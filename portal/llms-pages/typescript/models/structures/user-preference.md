# User Preference

Source: /#/typescript/x-redirect/JTI0bSUyRlVzZXJQcmVmZXJlbmNl

A single user preference setting.

*This model accepts additional fields of type unknown.*


# Interface Name

`UserPreference`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Required | Unique key identifying the preference. |
| `value` | `string` | Required | Preference value as a string. Note that the internal _lastloaded preference is returned as an integer by the LMS. |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
import { UserPreference } from 'nust-lms-apilib';

const userPreference: UserPreference = {
  name: 'block_myoverview_user_sort_preference',
  value: 'title',
  additionalProperties: {
    'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
  },
};
```



