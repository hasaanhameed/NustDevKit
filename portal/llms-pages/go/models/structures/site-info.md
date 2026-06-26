# Site Info

Source: /#/go/x-redirect/JTI0bSUyRlNpdGVJbmZv

Your identity plus basic site information, from Moodle's site-info call. The `userid` here is what other endpoints need (e.g. it is the `useridto` for popup notifications).

*This model accepts additional fields of type interface{}.*


# Class Name

`SiteInfo`


# Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `Userid` | `int` | Required | Your numeric Moodle user ID. |
| `Username` | `string` | Required | Your login username. |
| `Firstname` | `*string` | Optional | Your first name. |
| `Lastname` | `*string` | Optional | Your last name. |
| `Fullname` | `string` | Required | Your full display name. |
| `Userpictureurl` | `*string` | Optional | URL of your profile picture. |
| `Lang` | `*string` | Optional | Your preferred interface language code. |
| `Sitename` | `string` | Required | Name of the LMS site. |
| `Siteurl` | `*string` | Optional | Base URL of the LMS site. |
| `Release` | `*string` | Optional | Moodle release/version string of the site. |
| `AdditionalProperties` | `map[string]interface{}` | Optional | - |


# Example

```go
package main

import (
    "nustLmsApi/models"
)

func main() {
    siteInfo := models.SiteInfo{
        Userid:                234567,
        Username:              "johndoe.bscs23seecs",
        Firstname:             models.ToPointer("John"),
        Lastname:              models.ToPointer("Doe"),
        Fullname:              "John Doe",
        Userpictureurl:        models.ToPointer("https://lms.nust.edu.pk/portal/pluginfile.php/1583361/user/icon/moove/f1"),
        Lang:                  models.ToPointer("en"),
        Sitename:              "NUST LMS",
        Siteurl:               models.ToPointer("https://lms.nust.edu.pk/portal"),
        Release:               models.ToPointer("4.1.2"),
        AdditionalProperties:  map[string]interface{}{
            "exampleAdditionalProperty": interface{}("[key1, val1][key2, val2]"),
        },
    }

}
```



