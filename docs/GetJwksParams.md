# GetJwksParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op_configuration_endpoint** | **str** | The openid configuration endpoint URL. If missing, then &#x60;op_host&#x60; must be defined. | 
**op_host** | **str** | Deprecated in favor of &#x60;op_configuration_endpoint&#x60;. It will be removed in future version(s). Provide the URL of OpenID Provider (OP) in this field. If missing, then &#x60;op_configuration_endpoint&#x60; must be defined. | [optional] 
**op_discovery_path** | **str** | Deprecated in favor of &#x60;op_configuration_endpoint&#x60;. It will be removed in future version(s). Provide path to the OpenID Connect Provider&#x27;s discovery document in this field. For example, if it is &#x27;https://example.com/.well-known/openid-configuration&#x27; then the path is blank. But if it is &#x27;https://example.com/oxauth/.well-known/openid-configuration&#x27; then the path is &#x27;/oxauth&#x27; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

