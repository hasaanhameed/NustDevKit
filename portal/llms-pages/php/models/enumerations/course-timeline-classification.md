# Course Timeline Classification

Source: /#/php/x-redirect/JTI0bSUyRkNvdXJzZVRpbWVsaW5lQ2xhc3NpZmljYXRpb24

Timeline classification filter for enrolled courses.


# Enum Type Name

`CourseTimelineClassification`


# Fields

| Name |
|  --- |
| `ALL` |
| `INPROGRESS` |
| `PAST` |
| `FUTURE` |
| `FAVOURITES` |
| `HIDDEN` |
| `ALLINCLUDINGHIDDEN` |


# Example

```php
use NustLmsApiLib\Models\CourseTimelineClassification;

$courseTimelineClassification = CourseTimelineClassification::FUTURE;
```



