# swagger_client.TokenApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_token_token_post**](TokenApi.md#generate_token_token_post) | **POST** /token | Generate Token

# **generate_token_token_post**
> TokenResponseSchema generate_token_token_post()

Generate Token

Use your account as HTTPBasic Auth to generate your token to use the API. You can also generate your token directly on the website.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: HTTPBasic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.TokenApi(swagger_client.ApiClient(configuration))

try:
    # Generate Token
    api_response = api_instance.generate_token_token_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenApi->generate_token_token_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TokenResponseSchema**](TokenResponseSchema.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

