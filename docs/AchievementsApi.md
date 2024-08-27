# swagger_client.AchievementsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_achievement_achievements_code_get**](AchievementsApi.md#get_achievement_achievements_code_get) | **GET** /achievements/{code} | Get Achievement
[**get_all_achievements_achievements_get**](AchievementsApi.md#get_all_achievements_achievements_get) | **GET** /achievements | Get All Achievements

# **get_achievement_achievements_code_get**
> BaseachievementResponseSchema get_achievement_achievements_code_get(code)

Get Achievement

Retrieve the details of a achievement.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AchievementsApi()
code = NULL # object | The code of the achievement.

try:
    # Get Achievement
    api_response = api_instance.get_achievement_achievements_code_get(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AchievementsApi->get_achievement_achievements_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | [**object**](.md)| The code of the achievement. | 

### Return type

[**BaseachievementResponseSchema**](BaseachievementResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_achievements_achievements_get**
> DataPageBaseAchievementSchema_ get_all_achievements_achievements_get(type=type, page=page, size=size)

Get All Achievements

List of all achievements.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AchievementsApi()
type = NULL # object | Type of achievements. (optional)
page = 1 # object | Page number (optional) (default to 1)
size = 50 # object | Page size (optional) (default to 50)

try:
    # Get All Achievements
    api_response = api_instance.get_all_achievements_achievements_get(type=type, page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AchievementsApi->get_all_achievements_achievements_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**object**](.md)| Type of achievements. | [optional] 
 **page** | [**object**](.md)| Page number | [optional] [default to 1]
 **size** | [**object**](.md)| Page size | [optional] [default to 50]

### Return type

[**DataPageBaseAchievementSchema_**](DataPageBaseAchievementSchema_.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

