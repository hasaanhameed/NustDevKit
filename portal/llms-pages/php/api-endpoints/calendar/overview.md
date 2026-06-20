# Overview

Source: /#/php/x-redirect/JTI0aCUyRl9fYXBpX3JlZmVyZW5jZSUyRkNhbGVuZGFyJTJGT3ZlcnZpZXc

Calendar operations. On NUST LMS, these "action events" are how deadlines are surfaced — assignment, lab, quiz, and other submission due dates each appear as a calendar event on the day the work must be submitted.


# Get singleton instance

The singleton instance of the `CalendarApi` class can be accessed from the API Client.

```
$calendarApi = $client->getCalendarApi();
```



