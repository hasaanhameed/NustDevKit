# Event Action

Source: /#/typescript/x-redirect/JTI0bSUyRkV2ZW50QWN0aW9u

Primary action button metadata for a calendar event.

*This model accepts additional fields of type unknown.*


# Interface Name

`EventAction`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Required | Display label for the primary action button. |
| `url` | `string` | Required | URL the user should navigate to in order to perform the action. |
| `itemcount` | `number` | Required | Number of items associated with this action. |
| `actionable` | `boolean` | Required | Whether the action can currently be taken by the user. |
| `showitemcount` | `boolean` | Required | Whether to display the item count alongside the action label. |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
import { EventAction } from 'nust-lms-apilib';

const eventAction: EventAction = {
  name: 'Add submission',
  url: 'https://lms.nust.edu.pk/portal/mod/assign/view.php?id=999404&action=editsubmission',
  itemcount: 1,
  actionable: true,
  showitemcount: false,
  additionalProperties: {
    'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
  },
};
```



