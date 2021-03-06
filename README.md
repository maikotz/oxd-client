# swagger-client
oxd-server

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 4.2
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi(swagger_client.ApiClient(configuration))
body = swagger_client.GetAccessTokenByRefreshTokenParams() # GetAccessTokenByRefreshTokenParams |  (optional)
authorization = 'authorization_example' # str |  (optional)
authorization_oxd_id = 'authorization_oxd_id_example' # str |  (optional)

try:
    # Get Access Token By Refresh Token
    api_response = api_instance.get_access_token_by_refresh_token(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_access_token_by_refresh_token: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DevelopersApi(swagger_client.ApiClient(configuration))
body = swagger_client.GetAuthorizationUrlParams() # GetAuthorizationUrlParams |  (optional)
authorization = 'authorization_example' # str |  (optional)
authorization_oxd_id = 'authorization_oxd_id_example' # str |  (optional)

try:
    # Get Authorization Url
    api_response = api_instance.get_authorization_url(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_authorization_url: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DevelopersApi(swagger_client.ApiClient(configuration))
body = swagger_client.GetClientTokenParams() # GetClientTokenParams |  (optional)

try:
    # Get Client Token
    api_response = api_instance.get_client_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_client_token: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DevelopersApi(swagger_client.ApiClient(configuration))
body = swagger_client.GetDiscoveryParams() # GetDiscoveryParams |  (optional)

try:
    # Get OP Discovery Configuration
    api_response = api_instance.get_discovery(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_discovery: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DevelopersApi(swagger_client.ApiClient(configuration))
body = swagger_client.GetIssuerParams() # GetIssuerParams |  (optional)

try:
    # Get Issuer
    api_response = api_instance.get_issuer(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_issuer: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DevelopersApi(swagger_client.ApiClient(configuration))
body = swagger_client.GetJwksParams() # GetJwksParams |  (optional)
authorization = 'authorization_example' # str |  (optional)
authorization_oxd_id = 'authorization_oxd_id_example' # str |  (optional)

try:
    # Get JSON Web Key Set
    api_response = api_instance.get_json_web_key_set(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_json_web_key_set: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DevelopersApi(swagger_client.ApiClient(configuration))
body = swagger_client.GetLogoutUriParams() # GetLogoutUriParams |  (optional)
authorization = 'authorization_example' # str |  (optional)
authorization_oxd_id = 'authorization_oxd_id_example' # str |  (optional)

try:
    # Get Logout URL
    api_response = api_instance.get_logout_uri(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_logout_uri: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DevelopersApi(swagger_client.ApiClient(configuration))
body = swagger_client.GetTokensByCodeParams() # GetTokensByCodeParams |  (optional)
authorization = 'authorization_example' # str |  (optional)
authorization_oxd_id = 'authorization_oxd_id_example' # str |  (optional)

try:
    # Get Tokens By Code
    api_response = api_instance.get_tokens_by_code(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_tokens_by_code: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DevelopersApi(swagger_client.ApiClient(configuration))
body = swagger_client.GetUserInfoParams() # GetUserInfoParams |  (optional)
authorization = 'authorization_example' # str |  (optional)
authorization_oxd_id = 'authorization_oxd_id_example' # str |  (optional)

try:
    # Get User Info
    api_response = api_instance.get_user_info(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_user_info: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DevelopersApi(swagger_client.ApiClient(configuration))

try:
    # Health Check
    api_instance.health_check()
except ApiException as e:
    print("Exception when calling DevelopersApi->health_check: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DevelopersApi(swagger_client.ApiClient(configuration))
body = swagger_client.IntrospectAccessTokenParams() # IntrospectAccessTokenParams |  (optional)
authorization = 'authorization_example' # str |  (optional)
authorization_oxd_id = 'authorization_oxd_id_example' # str |  (optional)

try:
    # Introspect Access Token
    api_response = api_instance.introspect_access_token(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->introspect_access_token: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DevelopersApi(swagger_client.ApiClient(configuration))
body = swagger_client.IntrospectRptParams() # IntrospectRptParams |  (optional)
authorization = 'authorization_example' # str |  (optional)
authorization_oxd_id = 'authorization_oxd_id_example' # str |  (optional)

try:
    # Introspect RPT
    api_response = api_instance.introspect_rpt(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->introspect_rpt: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DevelopersApi(swagger_client.ApiClient(configuration))
body = swagger_client.RegisterSiteParams() # RegisterSiteParams |  (optional)

try:
    # Register Site
    api_response = api_instance.register_site(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->register_site: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DevelopersApi(swagger_client.ApiClient(configuration))
body = swagger_client.RemoveSiteParams() # RemoveSiteParams |  (optional)
authorization = 'authorization_example' # str |  (optional)
authorization_oxd_id = 'authorization_oxd_id_example' # str |  (optional)

try:
    # Remove Site
    api_response = api_instance.remove_site(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->remove_site: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DevelopersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UmaRpGetClaimsGatheringUrlParams() # UmaRpGetClaimsGatheringUrlParams |  (optional)
authorization = 'authorization_example' # str |  (optional)
authorization_oxd_id = 'authorization_oxd_id_example' # str |  (optional)

try:
    # UMA RP Get Claims Gathering URL
    api_response = api_instance.uma_rp_get_claims_gathering_url(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->uma_rp_get_claims_gathering_url: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DevelopersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UmaRpGetRptParams() # UmaRpGetRptParams |  (optional)
authorization = 'authorization_example' # str |  (optional)
authorization_oxd_id = 'authorization_oxd_id_example' # str |  (optional)

try:
    # UMA RP Get RPT
    api_response = api_instance.uma_rp_get_rpt(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->uma_rp_get_rpt: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DevelopersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UmaRsCheckAccessParams() # UmaRsCheckAccessParams |  (optional)
authorization = 'authorization_example' # str |  (optional)
authorization_oxd_id = 'authorization_oxd_id_example' # str |  (optional)

try:
    # UMA RS Check Access
    api_response = api_instance.uma_rs_check_access(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->uma_rs_check_access: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DevelopersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UmaRsModifyParams() # UmaRsModifyParams |  (optional)
authorization = 'authorization_example' # str |  (optional)
authorization_oxd_id = 'authorization_oxd_id_example' # str |  (optional)

try:
    # UMA RS Modify Resources
    api_response = api_instance.uma_rs_modify(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->uma_rs_modify: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DevelopersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UmaRsProtectParams() # UmaRsProtectParams |  (optional)
authorization = 'authorization_example' # str |  (optional)
authorization_oxd_id = 'authorization_oxd_id_example' # str |  (optional)

try:
    # UMA RS Protect Resources
    api_response = api_instance.uma_rs_protect(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->uma_rs_protect: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DevelopersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateSiteParams() # UpdateSiteParams |  (optional)
authorization = 'authorization_example' # str |  (optional)
authorization_oxd_id = 'authorization_oxd_id_example' # str |  (optional)

try:
    # Update Site
    api_response = api_instance.update_site(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->update_site: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://gluu.org/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DevelopersApi* | [**get_access_token_by_refresh_token**](docs/DevelopersApi.md#get_access_token_by_refresh_token) | **POST** /get-access-token-by-refresh-token | Get Access Token By Refresh Token
*DevelopersApi* | [**get_authorization_url**](docs/DevelopersApi.md#get_authorization_url) | **POST** /get-authorization-url | Get Authorization Url
*DevelopersApi* | [**get_client_token**](docs/DevelopersApi.md#get_client_token) | **POST** /get-client-token | Get Client Token
*DevelopersApi* | [**get_discovery**](docs/DevelopersApi.md#get_discovery) | **POST** /get-discovery | Get OP Discovery Configuration
*DevelopersApi* | [**get_issuer**](docs/DevelopersApi.md#get_issuer) | **POST** /get-issuer | Get Issuer
*DevelopersApi* | [**get_json_web_key_set**](docs/DevelopersApi.md#get_json_web_key_set) | **POST** /get-jwks | Get JSON Web Key Set
*DevelopersApi* | [**get_logout_uri**](docs/DevelopersApi.md#get_logout_uri) | **POST** /get-logout-uri | Get Logout URL
*DevelopersApi* | [**get_tokens_by_code**](docs/DevelopersApi.md#get_tokens_by_code) | **POST** /get-tokens-by-code | Get Tokens By Code
*DevelopersApi* | [**get_user_info**](docs/DevelopersApi.md#get_user_info) | **POST** /get-user-info | Get User Info
*DevelopersApi* | [**health_check**](docs/DevelopersApi.md#health_check) | **GET** /health-check | Health Check
*DevelopersApi* | [**introspect_access_token**](docs/DevelopersApi.md#introspect_access_token) | **POST** /introspect-access-token | Introspect Access Token
*DevelopersApi* | [**introspect_rpt**](docs/DevelopersApi.md#introspect_rpt) | **POST** /introspect-rpt | Introspect RPT
*DevelopersApi* | [**register_site**](docs/DevelopersApi.md#register_site) | **POST** /register-site | Register Site
*DevelopersApi* | [**remove_site**](docs/DevelopersApi.md#remove_site) | **POST** /remove-site | Remove Site
*DevelopersApi* | [**uma_rp_get_claims_gathering_url**](docs/DevelopersApi.md#uma_rp_get_claims_gathering_url) | **POST** /uma-rp-get-claims-gathering-url | UMA RP Get Claims Gathering URL
*DevelopersApi* | [**uma_rp_get_rpt**](docs/DevelopersApi.md#uma_rp_get_rpt) | **POST** /uma-rp-get-rpt | UMA RP Get RPT
*DevelopersApi* | [**uma_rs_check_access**](docs/DevelopersApi.md#uma_rs_check_access) | **POST** /uma-rs-check-access | UMA RS Check Access
*DevelopersApi* | [**uma_rs_modify**](docs/DevelopersApi.md#uma_rs_modify) | **POST** /uma-rs-modify | UMA RS Modify Resources
*DevelopersApi* | [**uma_rs_protect**](docs/DevelopersApi.md#uma_rs_protect) | **POST** /uma-rs-protect | UMA RS Protect Resources
*DevelopersApi* | [**update_site**](docs/DevelopersApi.md#update_site) | **POST** /update-site | Update Site

## Documentation For Models

 - [Condition](docs/Condition.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [GetAccessTokenByRefreshTokenParams](docs/GetAccessTokenByRefreshTokenParams.md)
 - [GetAccessTokenByRefreshTokenResponse](docs/GetAccessTokenByRefreshTokenResponse.md)
 - [GetAuthorizationUrlParams](docs/GetAuthorizationUrlParams.md)
 - [GetAuthorizationUrlResponse](docs/GetAuthorizationUrlResponse.md)
 - [GetClientTokenParams](docs/GetClientTokenParams.md)
 - [GetClientTokenResponse](docs/GetClientTokenResponse.md)
 - [GetDiscoveryParams](docs/GetDiscoveryParams.md)
 - [GetDiscoveryResponse](docs/GetDiscoveryResponse.md)
 - [GetIssuerParams](docs/GetIssuerParams.md)
 - [GetIssuerResponse](docs/GetIssuerResponse.md)
 - [GetJwksParams](docs/GetJwksParams.md)
 - [GetJwksResponse](docs/GetJwksResponse.md)
 - [GetLogoutUriParams](docs/GetLogoutUriParams.md)
 - [GetLogoutUriResponse](docs/GetLogoutUriResponse.md)
 - [GetTokensByCodeParams](docs/GetTokensByCodeParams.md)
 - [GetTokensByCodeResponse](docs/GetTokensByCodeResponse.md)
 - [GetUserInfoParams](docs/GetUserInfoParams.md)
 - [IntrospectAccessTokenParams](docs/IntrospectAccessTokenParams.md)
 - [IntrospectAccessTokenResponse](docs/IntrospectAccessTokenResponse.md)
 - [IntrospectRptParams](docs/IntrospectRptParams.md)
 - [IntrospectRptResponse](docs/IntrospectRptResponse.md)
 - [JsonWebKey](docs/JsonWebKey.md)
 - [OxdId](docs/OxdId.md)
 - [RegisterSiteParams](docs/RegisterSiteParams.md)
 - [RegisterSiteResponse](docs/RegisterSiteResponse.md)
 - [RemoveSiteParams](docs/RemoveSiteParams.md)
 - [RemoveSiteResponse](docs/RemoveSiteResponse.md)
 - [RsResource](docs/RsResource.md)
 - [UmaRpGetClaimsGatheringUrlParams](docs/UmaRpGetClaimsGatheringUrlParams.md)
 - [UmaRpGetClaimsGatheringUrlResponse](docs/UmaRpGetClaimsGatheringUrlResponse.md)
 - [UmaRpGetRptParams](docs/UmaRpGetRptParams.md)
 - [UmaRpGetRptResponse](docs/UmaRpGetRptResponse.md)
 - [UmaRsCheckAccessParams](docs/UmaRsCheckAccessParams.md)
 - [UmaRsCheckAccessResponse](docs/UmaRsCheckAccessResponse.md)
 - [UmaRsModifyParams](docs/UmaRsModifyParams.md)
 - [UmaRsModifyResponse](docs/UmaRsModifyResponse.md)
 - [UmaRsProtectParams](docs/UmaRsProtectParams.md)
 - [UmaRsProtectResponse](docs/UmaRsProtectResponse.md)
 - [UpdateSiteParams](docs/UpdateSiteParams.md)
 - [UpdateSiteResponse](docs/UpdateSiteResponse.md)
 - [WebFingerLink](docs/WebFingerLink.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

yuriyz@gluu.org
