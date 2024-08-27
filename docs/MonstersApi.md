# swagger_client.MonstersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_monsters_monsters_get**](MonstersApi.md#get_all_monsters_monsters_get) | **GET** /monsters | Get All Monsters
[**get_monster_monsters_code_get**](MonstersApi.md#get_monster_monsters_code_get) | **GET** /monsters/{code} | Get Monster

# **get_all_monsters_monsters_get**
> DataPageMonsterSchema_ get_all_monsters_monsters_get(min_level=min_level, max_level=max_level, drop=drop, page=page, size=size)

Get All Monsters

Fetch monsters details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MonstersApi()
min_level = NULL # object | Monster minimum level. (optional)
max_level = NULL # object | Monster maximum level. (optional)
drop = NULL # object | Item code of the drop. (optional)
page = 1 # object | Page number (optional) (default to 1)
size = 50 # object | Page size (optional) (default to 50)

try:
    # Get All Monsters
    api_response = api_instance.get_all_monsters_monsters_get(min_level=min_level, max_level=max_level, drop=drop, page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonstersApi->get_all_monsters_monsters_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_level** | [**object**](.md)| Monster minimum level. | [optional] 
 **max_level** | [**object**](.md)| Monster maximum level. | [optional] 
 **drop** | [**object**](.md)| Item code of the drop. | [optional] 
 **page** | [**object**](.md)| Page number | [optional] [default to 1]
 **size** | [**object**](.md)| Page size | [optional] [default to 50]

### Return type

[**DataPageMonsterSchema_**](DataPageMonsterSchema_.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monster_monsters_code_get**
> MonsterResponseSchema get_monster_monsters_code_get(code)

Get Monster

Retrieve the details of a monster.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MonstersApi()
code = NULL # object | The code of the monster.

try:
    # Get Monster
    api_response = api_instance.get_monster_monsters_code_get(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonstersApi->get_monster_monsters_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | [**object**](.md)| The code of the monster. | 

### Return type

[**MonsterResponseSchema**](MonsterResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

