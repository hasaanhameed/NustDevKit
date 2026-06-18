# Popup Notifications Response

Source: /#/go/x-redirect/JTI0bSUyRlBvcHVwTm90aWZpY2F0aW9uc1Jlc3BvbnNl

Response envelope for the popup-notifications endpoint.

*This model accepts additional fields of type interface{}.*


# Class Name

`PopupNotificationsResponse`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Notifications` | [`[]models.Notification`](/llms-pages/go/models/structures/notification.md) | Required | List of popup notifications for the user. |
| `Unreadcount` | `int` | Required | Total number of unread notifications for the user. |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
package main

import (
    "nustLmsApi/models"
)

func main() {
    popupNotificationsResponse := models.PopupNotificationsResponse{
        Notifications:         []models.Notification{
            models.Notification{
                Id:                    4857819,
                Useridfrom:            198956,
                Useridto:              162154,
                Subject:               "CS-419-Deep Learning: Lab Sessional Finalization",
                Shortenedsubject:      "CS-419-Deep Learning: Lab Sessional Finalization",
                Text:                  "<p>Areeba Rameen posted in CS-419-Deep Learning...</p>",
                Fullmessage:           "fullmessage8",
                Fullmessageformat:     2,
                Fullmessagehtml:       "fullmessagehtml4",
                Smallmessage:          "Areeba Rameen posted in CS-419-Deep Learning...",
                Contexturl:            "https://lms.nust.edu.pk/portal/mod/forum/discuss.php?d=41767#p52342",
                Contexturlname:        "Lab Sessional Finalization - (DL - Section D & E)",
                Timecreated:           1780045085,
                Timecreatedpretty:     "19 days ago",
                Timeread:              models.NewOptional(models.ToPointer(152)),
                Read:                  false,
                Deleted:               false,
                Iconurl:               "https://lms.nust.edu.pk/portal/theme/image.php/moove/mod_forum/1778048051/icon",
                Component:             "mod_forum",
                Eventtype:             "posts",
                Customdata:            "{\"cmid\":\"1272420\",\"instance\":\"62569\",\"discussionid\":\"41767\"}",
                AdditionalProperties:  map[string]interface{}{
                    "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
                },
            },
        },
        Unreadcount:           1,
        AdditionalProperties:  map[string]interface{}{
            "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
        },
    }

}
```



