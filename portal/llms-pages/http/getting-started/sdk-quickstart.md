# SDK Quickstart

Source: /#/http/x-redirect/JTI0aCUyRl9fZ2V0dGluZ19zdGFydGVk


# Introduction

NUST Learning Management System API for developer integrations (Moodle AJAX wrapper). Each path is virtual for clean SDK generation; NustDevKit resolves them to the underlying Moodle AJAX service endpoint transparently.

## Base URI

The API uses the following base URI:

```bash
https://lms.nust.edu.pk/portal
```



# Authorization

This API uses the following authentication schemes.

* [`SessKey (Custom Query Parameter)`](/llms-pages/http/getting-started/sdk-quickstart/authorization.md)

## SessKey (Custom Query Parameter)



This API uses the following query parameters for authentication.

| Query | Default | Description |
|  --- | --- | --- |
| sesskey | *None* | Session key obtained after authenticating with the LMS portal. |

The request looks like this:

```bash
curl https://lms.nust.edu.pk/portal?sesskey={SESSKEY}
```

```http
GET /?sesskey={SESSKEY} HTTP/1.1
Host: {HOST}
```




