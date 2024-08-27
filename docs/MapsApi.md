# swagger_client.MapsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_maps_maps_get**](MapsApi.md#get_all_maps_maps_get) | **GET** /maps | Get All Maps
[**get_map_maps_xy_get**](MapsApi.md#get_map_maps_xy_get) | **GET** /maps/{x}/{y} | Get Map

# **get_all_maps_maps_get**
> DataPageMapSchema_ get_all_maps_maps_get(content_type=content_type, content_code=content_code, page=page, size=size)

Get All Maps

Fetch maps details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MapsApi()
content_type = NULL # object | Type of content on the map. (optional)
content_code = NULL # object | Content code on the map. (optional)
page = 1 # object | Page number (optional) (default to 1)
size = 50 # object | Page size (optional) (default to 50)

try:
    # Get All Maps
    api_response = api_instance.get_all_maps_maps_get(content_type=content_type, content_code=content_code, page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapsApi->get_all_maps_maps_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | [**object**](.md)| Type of content on the map. | [optional] 
 **content_code** | [**object**](.md)| Content code on the map. | [optional] 
 **page** | [**object**](.md)| Page number | [optional] [default to 1]
 **size** | [**object**](.md)| Page size | [optional] [default to 50]

### Return type

[**DataPageMapSchema_**](DataPageMapSchema_.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_map_maps_xy_get**
> MapResponseSchema get_map_maps_xy_get(x, y)

Get Map

Retrieve the details of a map.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MapsApi()
x = NULL # object | The position x of the map.
y = NULL # object | The position X of the map.

try:
    # Get Map
    api_response = api_instance.get_map_maps_xy_get(x, y)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MapsApi->get_map_maps_xy_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x** | [**object**](.md)| The position x of the map. | 
 **y** | [**object**](.md)| The position X of the map. | 

### Return type

[**MapResponseSchema**](MapResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

