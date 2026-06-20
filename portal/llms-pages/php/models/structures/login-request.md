# Login Request

Source: /#/php/x-redirect/JTI0bSUyRkxvZ2luUmVxdWVzdA

NUST LMS credentials used to obtain a gateway bearer token.

*This model accepts additional fields of type array.*


# Class Name

`LoginRequest`


# Fields

| Name | Type | Tags | Description | Getter | Setter |
|  --- | --- | --- | --- | --- | --- |
| `username` | `string` | Required | NUST LMS username. | getUsername(): string | setUsername(string username): void |
| `password` | `string` | Required | NUST LMS password. | getPassword(): string | setPassword(string password): void |
| `additionalProperties` | `array<string, array>` | Optional | - | findAdditionalProperty(string key): array | additionalProperty(string key, array value): void |


# Example

```php
use NustLmsApiLib\Models\Builders\LoginRequestBuilder;
use NustLmsApiLib\ApiHelper;

$loginRequest = LoginRequestBuilder::init(
    'johndoe.bscs23seecs',
    'password2'
)
    ->additionalProperty('exampleAdditionalProperty', ApiHelper::deserialize('{"key1":"val1","key2":"val2"}'))
    ->build();
```



