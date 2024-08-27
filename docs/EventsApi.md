# swagger_client.EventsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_events_events_get**](EventsApi.md#get_all_events_events_get) | **GET** /events | Get All Events

# **get_all_events_events_get**
> DataPageActiveEventSchema_ get_all_events_events_get(page=page, size=size)

Get All Events

Fetch events details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventsApi()
page = 1 # object | Page number (optional) (default to 1)
size = 50 # object | Page size (optional) (default to 50)

try:
    # Get All Events
    api_response = api_instance.get_all_events_events_get(page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_all_events_events_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | [**object**](.md)| Page number | [optional] [default to 1]
 **size** | [**object**](.md)| Page size | [optional] [default to 50]

### Return type

[**DataPageActiveEventSchema_**](DataPageActiveEventSchema_.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

