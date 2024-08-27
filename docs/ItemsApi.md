# swagger_client.ItemsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_items_items_get**](ItemsApi.md#get_all_items_items_get) | **GET** /items | Get All Items
[**get_item_items_code_get**](ItemsApi.md#get_item_items_code_get) | **GET** /items/{code} | Get Item

# **get_all_items_items_get**
> DataPageItemSchema_ get_all_items_items_get(min_level=min_level, max_level=max_level, name=name, type=type, craft_skill=craft_skill, craft_material=craft_material, page=page, size=size)

Get All Items

Fetch items details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemsApi()
min_level = NULL # object | Minimum level items. (optional)
max_level = NULL # object | Maximum level items. (optional)
name = NULL # object | Name of the item. (optional)
type = NULL # object | Type of items. (optional)
craft_skill = NULL # object | Skill to craft items. (optional)
craft_material = NULL # object | Item code of items used as material for crafting. (optional)
page = 1 # object | Page number (optional) (default to 1)
size = 50 # object | Page size (optional) (default to 50)

try:
    # Get All Items
    api_response = api_instance.get_all_items_items_get(min_level=min_level, max_level=max_level, name=name, type=type, craft_skill=craft_skill, craft_material=craft_material, page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->get_all_items_items_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_level** | [**object**](.md)| Minimum level items. | [optional] 
 **max_level** | [**object**](.md)| Maximum level items. | [optional] 
 **name** | [**object**](.md)| Name of the item. | [optional] 
 **type** | [**object**](.md)| Type of items. | [optional] 
 **craft_skill** | [**object**](.md)| Skill to craft items. | [optional] 
 **craft_material** | [**object**](.md)| Item code of items used as material for crafting. | [optional] 
 **page** | [**object**](.md)| Page number | [optional] [default to 1]
 **size** | [**object**](.md)| Page size | [optional] [default to 50]

### Return type

[**DataPageItemSchema_**](DataPageItemSchema_.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_items_code_get**
> ItemResponseSchema get_item_items_code_get(code)

Get Item

Retrieve the details of a item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemsApi()
code = NULL # object | The code of the item.

try:
    # Get Item
    api_response = api_instance.get_item_items_code_get(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsApi->get_item_items_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | [**object**](.md)| The code of the item. | 

### Return type

[**ItemResponseSchema**](ItemResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

