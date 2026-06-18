# Event Action

Source: /#/http/x-redirect/JTI0bSUyRkV2ZW50QWN0aW9u

Primary action button metadata for a calendar event.

*This model accepts additional fields of type Object.*


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `String` | Required | Display label for the primary action button. |
| `url` | `String` | Required | URL the user should navigate to in order to perform the action. |
| `itemcount` | `Number` | Required | Number of items associated with this action. |
| `actionable` | `Boolean` | Required | Whether the action can currently be taken by the user. |
| `showitemcount` | `Boolean` | Required | Whether to display the item count alongside the action label. |
| `additionalProperties` | `Object` | Optional | - |


# Example (as JSON)

```json
{
  "name": "Add submission",
  "url": "https://lms.nust.edu.pk/portal/mod/assign/view.php?id=999404&action=editsubmission",
  "itemcount": 1,
  "actionable": true,
  "showitemcount": false,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```



