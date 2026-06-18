# ApiResponse

Source: /#/python/x-redirect/JTI0aCUyRl9fYWRkaXRpb25hbF9kb2N1bWVudGF0aW9uJTJGVXRpbGl0aWVzJTJGQXBpUmVzcG9uc2U


An object with the response value as well as other useful information such as status codes and headers.

# Properties

| Name | Type | Description |
|  --- | --- | --- |
| status_code | `int` | The HTTP status code of the response. |
| reason_phrase | `str` | The reason phrase returned with the status code. |
| headers | `dict[str, str]` | The HTTP response headers. |
| text | `str` | The raw response body as a string. |
| request | [`HttpRequest`](/llms-pages/python/sdk-infrastructure/http/httprequest.md) | The original HTTP request sent. |
| body | `Any` | The parsed response data, if applicable. |

# Usage Example

```python
try:
    # Perform API request
    result: ApiResponse = client.example_controller.example_endpoint(input)

    # Inspect response attributes
    print("Status Code:", result.status_code)
    print("Headers:", result.headers)
    print("Body:", result.body)
except APIException as e:
    print("API Exception:", e)
except Exception as e:
    print("General Exception:", e)
```



