# User Preferences Response

Source: /#/typescript/x-redirect/JTI0bSUyRlVzZXJQcmVmZXJlbmNlc1Jlc3BvbnNl

Response envelope for the user-preferences endpoint.

*This model accepts additional fields of type unknown.*


# Interface Name

`UserPreferencesResponse`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `preferences` | [`UserPreference[]`](/llms-pages/typescript/models/structures/user-preference.md) | Required | List of user preference key/value pairs. |
| `warnings` | [`MoodleWarning[]`](/llms-pages/typescript/models/structures/moodle-warning.md) | Required | Array of warning objects. Empty when no warnings are present. |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
import { UserPreferencesResponse } from 'nust-lms-apilib';

const userPreferencesResponse: UserPreferencesResponse = {
  preferences: [
    {
      name: 'block_myoverview_user_sort_preference',
      value: 'title',
      additionalProperties: {
        'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
      },
    }
  ],
  warnings: [
    {
      item: 'item6',
      itemid: 0,
      warningcode: 'warningcode4',
      message: 'message4',
      additionalProperties: {
        'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
      },
    }
  ],
  additionalProperties: {
    'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
  },
};
```



