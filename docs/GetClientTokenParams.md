# GetClientTokenParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op_configuration_endpoint** | **str** | The openid configuration endpoint URL. If missing, then &#x60;op_host&#x60; must be defined. | 
**op_host** | **str** | Deprecated in favor of &#x60;op_configuration_endpoint&#x60;. It will be removed in future version(s). Provide the URL of OpenID Provider (OP) in this field. If missing, then &#x60;op_configuration_endpoint&#x60; must be defined. | [optional] 
**op_discovery_path** | **str** | Deprecated in favor of &#x60;op_configuration_endpoint&#x60;. It will be removed in future version(s). Provide path to the OpenID Connect Provider&#x27;s discovery document in this field. For example, if it is &#x27;https://example.com/.well-known/openid-configuration&#x27; then the path is blank. But if it is &#x27;https://example.com/oxauth/.well-known/openid-configuration&#x27; then the path is &#x27;/oxauth&#x27; | [optional] 
**scope** | **list[str]** |  | [optional] 
**client_id** | **str** |  | 
**client_secret** | **str** |  | 
**authentication_method** | **str** | if value is missed then basic authentication is used. Otherwise it&#x27;s possible to set &#x60;private_key_jwt&#x60; value for Private Key authentication. | [optional] 
**algorithm** | **str** | optional but is required if authentication_method&#x3D;private_key_jwt. Valid values are none, HS256, HS384, HS512, RS256, RS384, RS512, ES256, ES384, ES512 | [optional] 
**key_id** | **str** | optional but is required if authentication_method&#x3D;private_key_jwt. It has to be valid key id from key store. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

