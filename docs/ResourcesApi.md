# swagger_client.ResourcesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_resources_resources_get**](ResourcesApi.md#get_all_resources_resources_get) | **GET** /resources | Get All Resources
[**get_resource_resources_code_get**](ResourcesApi.md#get_resource_resources_code_get) | **GET** /resources/{code} | Get Resource

# **get_all_resources_resources_get**
> DataPageResourceSchema_ get_all_resources_resources_get(min_level=min_level, max_level=max_level, skill=skill, drop=drop, page=page, size=size)

Get All Resources

Fetch resources details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesApi()
min_level = NULL # object | Skill minimum level. (optional)
max_level = NULL # object | Skill maximum level. (optional)
skill = NULL # object | The code of the skill. (optional)
drop = NULL # object | Item code of the drop. (optional)
page = 1 # object | Page number (optional) (default to 1)
size = 50 # object | Page size (optional) (default to 50)

try:
    # Get All Resources
    api_response = api_instance.get_all_resources_resources_get(min_level=min_level, max_level=max_level, skill=skill, drop=drop, page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->get_all_resources_resources_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_level** | [**object**](.md)| Skill minimum level. | [optional] 
 **max_level** | [**object**](.md)| Skill maximum level. | [optional] 
 **skill** | [**object**](.md)| The code of the skill. | [optional] 
 **drop** | [**object**](.md)| Item code of the drop. | [optional] 
 **page** | [**object**](.md)| Page number | [optional] [default to 1]
 **size** | [**object**](.md)| Page size | [optional] [default to 50]

### Return type

[**DataPageResourceSchema_**](DataPageResourceSchema_.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_resources_code_get**
> ResourceResponseSchema get_resource_resources_code_get(code)

Get Resource

Retrieve the details of a resource.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesApi()
code = NULL # object | The code of the resource.

try:
    # Get Resource
    api_response = api_instance.get_resource_resources_code_get(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesApi->get_resource_resources_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | [**object**](.md)| The code of the resource. | 

### Return type

[**ResourceResponseSchema**](ResourceResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

