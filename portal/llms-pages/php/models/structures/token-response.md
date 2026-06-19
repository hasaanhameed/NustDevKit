# Token Response

Source: /#/php/x-redirect/JTI0bSUyRlRva2VuUmVzcG9uc2U

Bearer token issued by the gateway after a successful login.

*This model accepts additional fields of type array.*


# Class Name

`TokenResponse`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `accessToken` | `string` | Required | JWT to send as `Authorization: Bearer <token>` on subsequent requests. | getAccessToken(): string | setAccessToken(string accessToken): void |
| `tokenType` | `string` | Required | **Default**: `'bearer'` | getTokenType(): string | setTokenType(string tokenType): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |


# Example

```php
use NustLmsApiLib\Models\Builders\TokenResponseBuilder;
use NustLmsApiLib\ApiHelper;

$tokenResponse = TokenResponseBuilder::init(
    'access_token2',
    'bearer'
)
    ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
    ->build();
```



