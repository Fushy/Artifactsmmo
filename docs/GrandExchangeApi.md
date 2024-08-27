# swagger_client.GrandExchangeApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_ge_items_ge_get**](GrandExchangeApi.md#get_all_ge_items_ge_get) | **GET** /ge | Get All Ge Items
[**get_ge_item_ge_code_get**](GrandExchangeApi.md#get_ge_item_ge_code_get) | **GET** /ge/{code} | Get Ge Item

# **get_all_ge_items_ge_get**
> DataPageGEItemSchema_ get_all_ge_items_ge_get(page=page, size=size)

Get All Ge Items

Fetch Grand Exchange items details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GrandExchangeApi()
page = 1 # object | Page number (optional) (default to 1)
size = 50 # object | Page size (optional) (default to 50)

try:
    # Get All Ge Items
    api_response = api_instance.get_all_ge_items_ge_get(page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrandExchangeApi->get_all_ge_items_ge_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | [**object**](.md)| Page number | [optional] [default to 1]
 **size** | [**object**](.md)| Page size | [optional] [default to 50]

### Return type

[**DataPageGEItemSchema_**](DataPageGEItemSchema_.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ge_item_ge_code_get**
> GEItemResponseSchema get_ge_item_ge_code_get(code)

Get Ge Item

Retrieve the details of a Grand Exchange item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GrandExchangeApi()
code = NULL # object | The code of the item.

try:
    # Get Ge Item
    api_response = api_instance.get_ge_item_ge_code_get(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GrandExchangeApi->get_ge_item_ge_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | [**object**](.md)| The code of the item. | 

### Return type

[**GEItemResponseSchema**](GEItemResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

