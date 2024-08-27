# swagger_client.LeaderboardApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_leaderboard_leaderboard_get**](LeaderboardApi.md#get_leaderboard_leaderboard_get) | **GET** /leaderboard | Get Leaderboard

# **get_leaderboard_leaderboard_get**
> DataPageCharacterLeaderboardSchema_ get_leaderboard_leaderboard_get(sort=sort, page=page, size=size)

Get Leaderboard

Fetch leaderboard details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LeaderboardApi()
sort = NULL # object | Default sort by combat total XP. (optional)
page = 1 # object | Page number (optional) (default to 1)
size = 50 # object | Page size (optional) (default to 50)

try:
    # Get Leaderboard
    api_response = api_instance.get_leaderboard_leaderboard_get(sort=sort, page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaderboardApi->get_leaderboard_leaderboard_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | [**object**](.md)| Default sort by combat total XP. | [optional] 
 **page** | [**object**](.md)| Page number | [optional] [default to 1]
 **size** | [**object**](.md)| Page size | [optional] [default to 50]

### Return type

[**DataPageCharacterLeaderboardSchema_**](DataPageCharacterLeaderboardSchema_.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

