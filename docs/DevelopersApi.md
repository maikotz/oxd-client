# swagger_client.DevelopersApi

All URIs are relative to *https://gluu.org/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_access_token_by_refresh_token**](DevelopersApi.md#get_access_token_by_refresh_token) | **POST** /get-access-token-by-refresh-token | Get Access Token By Refresh Token
[**get_authorization_url**](DevelopersApi.md#get_authorization_url) | **POST** /get-authorization-url | Get Authorization Url
[**get_client_token**](DevelopersApi.md#get_client_token) | **POST** /get-client-token | Get Client Token
[**get_discovery**](DevelopersApi.md#get_discovery) | **POST** /get-discovery | Get OP Discovery Configuration
[**get_issuer**](DevelopersApi.md#get_issuer) | **POST** /get-issuer | Get Issuer
[**get_json_web_key_set**](DevelopersApi.md#get_json_web_key_set) | **POST** /get-jwks | Get JSON Web Key Set
[**get_logout_uri**](DevelopersApi.md#get_logout_uri) | **POST** /get-logout-uri | Get Logout URL
[**get_tokens_by_code**](DevelopersApi.md#get_tokens_by_code) | **POST** /get-tokens-by-code | Get Tokens By Code
[**get_user_info**](DevelopersApi.md#get_user_info) | **POST** /get-user-info | Get User Info
[**health_check**](DevelopersApi.md#health_check) | **GET** /health-check | Health Check
[**introspect_access_token**](DevelopersApi.md#introspect_access_token) | **POST** /introspect-access-token | Introspect Access Token
[**introspect_rpt**](DevelopersApi.md#introspect_rpt) | **POST** /introspect-rpt | Introspect RPT
[**register_site**](DevelopersApi.md#register_site) | **POST** /register-site | Register Site
[**remove_site**](DevelopersApi.md#remove_site) | **POST** /remove-site | Remove Site
[**uma_rp_get_claims_gathering_url**](DevelopersApi.md#uma_rp_get_claims_gathering_url) | **POST** /uma-rp-get-claims-gathering-url | UMA RP Get Claims Gathering URL
[**uma_rp_get_rpt**](DevelopersApi.md#uma_rp_get_rpt) | **POST** /uma-rp-get-rpt | UMA RP Get RPT
[**uma_rs_check_access**](DevelopersApi.md#uma_rs_check_access) | **POST** /uma-rs-check-access | UMA RS Check Access
[**uma_rs_modify**](DevelopersApi.md#uma_rs_modify) | **POST** /uma-rs-modify | UMA RS Modify Resources
[**uma_rs_protect**](DevelopersApi.md#uma_rs_protect) | **POST** /uma-rs-protect | UMA RS Protect Resources
[**update_site**](DevelopersApi.md#update_site) | **POST** /update-site | Update Site

# **get_access_token_by_refresh_token**
> GetAccessTokenByRefreshTokenResponse get_access_token_by_refresh_token(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)

Get Access Token By Refresh Token

Get Access Token By Refresh Token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
body = swagger_client.GetAccessTokenByRefreshTokenParams() # GetAccessTokenByRefreshTokenParams |  (optional)
authorization = 'authorization_example' # str |  (optional)
authorization_oxd_id = 'authorization_oxd_id_example' # str |  (optional)

try:
    # Get Access Token By Refresh Token
    api_response = api_instance.get_access_token_by_refresh_token(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_access_token_by_refresh_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetAccessTokenByRefreshTokenParams**](GetAccessTokenByRefreshTokenParams.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **authorization_oxd_id** | **str**|  | [optional] 

### Return type

[**GetAccessTokenByRefreshTokenResponse**](GetAccessTokenByRefreshTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authorization_url**
> GetAuthorizationUrlResponse get_authorization_url(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)

Get Authorization Url

Gets authorization url

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
body = swagger_client.GetAuthorizationUrlParams() # GetAuthorizationUrlParams |  (optional)
authorization = 'authorization_example' # str |  (optional)
authorization_oxd_id = 'authorization_oxd_id_example' # str |  (optional)

try:
    # Get Authorization Url
    api_response = api_instance.get_authorization_url(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_authorization_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetAuthorizationUrlParams**](GetAuthorizationUrlParams.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **authorization_oxd_id** | **str**|  | [optional] 

### Return type

[**GetAuthorizationUrlResponse**](GetAuthorizationUrlResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_token**
> GetClientTokenResponse get_client_token(body=body)

Get Client Token

Gets Client Token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
body = swagger_client.GetClientTokenParams() # GetClientTokenParams |  (optional)

try:
    # Get Client Token
    api_response = api_instance.get_client_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_client_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetClientTokenParams**](GetClientTokenParams.md)|  | [optional] 

### Return type

[**GetClientTokenResponse**](GetClientTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discovery**
> GetDiscoveryResponse get_discovery(body=body)

Get OP Discovery Configuration

Get OP Discovery Configuration

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
body = swagger_client.GetDiscoveryParams() # GetDiscoveryParams |  (optional)

try:
    # Get OP Discovery Configuration
    api_response = api_instance.get_discovery(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_discovery: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetDiscoveryParams**](GetDiscoveryParams.md)|  | [optional] 

### Return type

[**GetDiscoveryResponse**](GetDiscoveryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_issuer**
> GetIssuerResponse get_issuer(body=body)

Get Issuer

Get Issuer

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
body = swagger_client.GetIssuerParams() # GetIssuerParams |  (optional)

try:
    # Get Issuer
    api_response = api_instance.get_issuer(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_issuer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetIssuerParams**](GetIssuerParams.md)|  | [optional] 

### Return type

[**GetIssuerResponse**](GetIssuerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_json_web_key_set**
> GetJwksResponse get_json_web_key_set(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)

Get JSON Web Key Set

Get JSON Web Key Set

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
body = swagger_client.GetJwksParams() # GetJwksParams |  (optional)
authorization = 'authorization_example' # str |  (optional)
authorization_oxd_id = 'authorization_oxd_id_example' # str |  (optional)

try:
    # Get JSON Web Key Set
    api_response = api_instance.get_json_web_key_set(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_json_web_key_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetJwksParams**](GetJwksParams.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **authorization_oxd_id** | **str**|  | [optional] 

### Return type

[**GetJwksResponse**](GetJwksResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logout_uri**
> GetLogoutUriResponse get_logout_uri(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)

Get Logout URL

Get Logout URL

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
body = swagger_client.GetLogoutUriParams() # GetLogoutUriParams |  (optional)
authorization = 'authorization_example' # str |  (optional)
authorization_oxd_id = 'authorization_oxd_id_example' # str |  (optional)

try:
    # Get Logout URL
    api_response = api_instance.get_logout_uri(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_logout_uri: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetLogoutUriParams**](GetLogoutUriParams.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **authorization_oxd_id** | **str**|  | [optional] 

### Return type

[**GetLogoutUriResponse**](GetLogoutUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tokens_by_code**
> GetTokensByCodeResponse get_tokens_by_code(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)

Get Tokens By Code

Get tokens by code

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
body = swagger_client.GetTokensByCodeParams() # GetTokensByCodeParams |  (optional)
authorization = 'authorization_example' # str |  (optional)
authorization_oxd_id = 'authorization_oxd_id_example' # str |  (optional)

try:
    # Get Tokens By Code
    api_response = api_instance.get_tokens_by_code(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_tokens_by_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetTokensByCodeParams**](GetTokensByCodeParams.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **authorization_oxd_id** | **str**|  | [optional] 

### Return type

[**GetTokensByCodeResponse**](GetTokensByCodeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_info**
> dict(str, object) get_user_info(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)

Get User Info

Get User Info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
body = swagger_client.GetUserInfoParams() # GetUserInfoParams |  (optional)
authorization = 'authorization_example' # str |  (optional)
authorization_oxd_id = 'authorization_oxd_id_example' # str |  (optional)

try:
    # Get User Info
    api_response = api_instance.get_user_info(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->get_user_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetUserInfoParams**](GetUserInfoParams.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **authorization_oxd_id** | **str**|  | [optional] 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_check**
> health_check()

Health Check

Health Check endpoint is for quick check whether oxd-server is alive.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()

try:
    # Health Check
    api_instance.health_check()
except ApiException as e:
    print("Exception when calling DevelopersApi->health_check: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **introspect_access_token**
> IntrospectAccessTokenResponse introspect_access_token(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)

Introspect Access Token

Introspect Access Token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
body = swagger_client.IntrospectAccessTokenParams() # IntrospectAccessTokenParams |  (optional)
authorization = 'authorization_example' # str |  (optional)
authorization_oxd_id = 'authorization_oxd_id_example' # str |  (optional)

try:
    # Introspect Access Token
    api_response = api_instance.introspect_access_token(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->introspect_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IntrospectAccessTokenParams**](IntrospectAccessTokenParams.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **authorization_oxd_id** | **str**|  | [optional] 

### Return type

[**IntrospectAccessTokenResponse**](IntrospectAccessTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **introspect_rpt**
> IntrospectRptResponse introspect_rpt(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)

Introspect RPT

Introspect RPT

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
body = swagger_client.IntrospectRptParams() # IntrospectRptParams |  (optional)
authorization = 'authorization_example' # str |  (optional)
authorization_oxd_id = 'authorization_oxd_id_example' # str |  (optional)

try:
    # Introspect RPT
    api_response = api_instance.introspect_rpt(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->introspect_rpt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IntrospectRptParams**](IntrospectRptParams.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **authorization_oxd_id** | **str**|  | [optional] 

### Return type

[**IntrospectRptResponse**](IntrospectRptResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_site**
> RegisterSiteResponse register_site(body=body)

Register Site

Registers site at oxd-server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
body = swagger_client.RegisterSiteParams() # RegisterSiteParams |  (optional)

try:
    # Register Site
    api_response = api_instance.register_site(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->register_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegisterSiteParams**](RegisterSiteParams.md)|  | [optional] 

### Return type

[**RegisterSiteResponse**](RegisterSiteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_site**
> RemoveSiteResponse remove_site(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)

Remove Site

Removes site from oxd-server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
body = swagger_client.RemoveSiteParams() # RemoveSiteParams |  (optional)
authorization = 'authorization_example' # str |  (optional)
authorization_oxd_id = 'authorization_oxd_id_example' # str |  (optional)

try:
    # Remove Site
    api_response = api_instance.remove_site(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->remove_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RemoveSiteParams**](RemoveSiteParams.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **authorization_oxd_id** | **str**|  | [optional] 

### Return type

[**RemoveSiteResponse**](RemoveSiteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uma_rp_get_claims_gathering_url**
> UmaRpGetClaimsGatheringUrlResponse uma_rp_get_claims_gathering_url(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)

UMA RP Get Claims Gathering URL

UMA RP Get Claims Gathering URL

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
body = swagger_client.UmaRpGetClaimsGatheringUrlParams() # UmaRpGetClaimsGatheringUrlParams |  (optional)
authorization = 'authorization_example' # str |  (optional)
authorization_oxd_id = 'authorization_oxd_id_example' # str |  (optional)

try:
    # UMA RP Get Claims Gathering URL
    api_response = api_instance.uma_rp_get_claims_gathering_url(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->uma_rp_get_claims_gathering_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UmaRpGetClaimsGatheringUrlParams**](UmaRpGetClaimsGatheringUrlParams.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **authorization_oxd_id** | **str**|  | [optional] 

### Return type

[**UmaRpGetClaimsGatheringUrlResponse**](UmaRpGetClaimsGatheringUrlResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uma_rp_get_rpt**
> UmaRpGetRptResponse uma_rp_get_rpt(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)

UMA RP Get RPT

UMA RP Get RPT

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
body = swagger_client.UmaRpGetRptParams() # UmaRpGetRptParams |  (optional)
authorization = 'authorization_example' # str |  (optional)
authorization_oxd_id = 'authorization_oxd_id_example' # str |  (optional)

try:
    # UMA RP Get RPT
    api_response = api_instance.uma_rp_get_rpt(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->uma_rp_get_rpt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UmaRpGetRptParams**](UmaRpGetRptParams.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **authorization_oxd_id** | **str**|  | [optional] 

### Return type

[**UmaRpGetRptResponse**](UmaRpGetRptResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uma_rs_check_access**
> UmaRsCheckAccessResponse uma_rs_check_access(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)

UMA RS Check Access

UMA RS Check Access

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
body = swagger_client.UmaRsCheckAccessParams() # UmaRsCheckAccessParams |  (optional)
authorization = 'authorization_example' # str |  (optional)
authorization_oxd_id = 'authorization_oxd_id_example' # str |  (optional)

try:
    # UMA RS Check Access
    api_response = api_instance.uma_rs_check_access(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->uma_rs_check_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UmaRsCheckAccessParams**](UmaRsCheckAccessParams.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **authorization_oxd_id** | **str**|  | [optional] 

### Return type

[**UmaRsCheckAccessResponse**](UmaRsCheckAccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uma_rs_modify**
> UmaRsModifyResponse uma_rs_modify(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)

UMA RS Modify Resources

UMA RS Modify Resource. This end-point can be used to modify one resource at a time from whole set of UMA resources of cient.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
body = swagger_client.UmaRsModifyParams() # UmaRsModifyParams |  (optional)
authorization = 'authorization_example' # str |  (optional)
authorization_oxd_id = 'authorization_oxd_id_example' # str |  (optional)

try:
    # UMA RS Modify Resources
    api_response = api_instance.uma_rs_modify(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->uma_rs_modify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UmaRsModifyParams**](UmaRsModifyParams.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **authorization_oxd_id** | **str**|  | [optional] 

### Return type

[**UmaRsModifyResponse**](UmaRsModifyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uma_rs_protect**
> UmaRsProtectResponse uma_rs_protect(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)

UMA RS Protect Resources

UMA RS Protect Resources. It's important to have a single HTTP method, mentioned only once within a given path in JSON, otherwise, the operation will fail.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
body = swagger_client.UmaRsProtectParams() # UmaRsProtectParams |  (optional)
authorization = 'authorization_example' # str |  (optional)
authorization_oxd_id = 'authorization_oxd_id_example' # str |  (optional)

try:
    # UMA RS Protect Resources
    api_response = api_instance.uma_rs_protect(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopersApi->uma_rs_protect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UmaRsProtectParams**](UmaRsProtectParams.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **authorization_oxd_id** | **str**|  | [optional] 

### Return type

[**UmaRsProtectResponse**](UmaRsProtectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_site**
> UpdateSiteResponse update_site(body=body, authorization=authorization, authorization_oxd_id=authorization_oxd_id)

Update Site

Updates site at oxd-server. If something changes in a pre-registered client, you can use this API to update your client in the OP.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevelopersApi()
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateSiteParams**](UpdateSiteParams.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **authorization_oxd_id** | **str**|  | [optional] 

### Return type

[**UpdateSiteResponse**](UpdateSiteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

