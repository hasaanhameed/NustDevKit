# Event Subscription

Source: /#/typescript/x-redirect/JTI0bSUyRkV2ZW50U3Vic2NyaXB0aW9u

Subscription display settings for a calendar event.

*This model accepts additional fields of type unknown.*


# Interface Name

`EventSubscription`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `displayeventsource` | `boolean` | Required | Whether to display the event source label on the calendar. |
| `additionalProperties` | `Record<string, unknown>` | Optional | - |


# Example

```ts
import { EventSubscription } from 'nust-lms-apilib';

const eventSubscription: EventSubscription = {
  displayeventsource: false,
  additionalProperties: {
    'exampleAdditionalProperty': { 'key1': 'val1', 'key2': 'val2' }
  },
};
```



