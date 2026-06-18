# Event Action

Source: /#/ruby/x-redirect/JTI0bSUyRkV2ZW50QWN0aW9u

Primary action button metadata for a calendar event.

*This model accepts additional fields of type Object.*


# Class Name

`EventAction`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `String` | Required | Display label for the primary action button. |
| `url` | `String` | Required | URL the user should navigate to in order to perform the action. |
| `itemcount` | `Integer` | Required | Number of items associated with this action. |
| `actionable` | `TrueClass \| FalseClass` | Required | Whether the action can currently be taken by the user. |
| `showitemcount` | `TrueClass \| FalseClass` | Required | Whether to display the item count alongside the action label. |
| `additional_properties` | `Hash[String, Object]` | Optional | - |


# Example

```ruby
event_action = EventAction.new(
  name: 'Add submission',
  url: 'https://lms.nust.edu.pk/portal/mod/assign/view.php?id=999404&action=editsubmission',
  itemcount: 1,
  actionable: true,
  showitemcount: false,
  additional_properties: {
    'exampleAdditionalProperty' => JSON.parse('{"key1":"val1","key2":"val2"}')
  }
)
```



