# swagger_client.CharactersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_character_characters_create_post**](CharactersApi.md#create_character_characters_create_post) | **POST** /characters/create | Create Character
[**delete_character_characters_delete_post**](CharactersApi.md#delete_character_characters_delete_post) | **POST** /characters/delete | Delete Character
[**get_all_characters_characters_get**](CharactersApi.md#get_all_characters_characters_get) | **GET** /characters | Get All Characters
[**get_character_achievements_characters_name_achievements_get**](CharactersApi.md#get_character_achievements_characters_name_achievements_get) | **GET** /characters/{name}/achievements | Get Character Achievements
[**get_character_characters_name_get**](CharactersApi.md#get_character_characters_name_get) | **GET** /characters/{name} | Get Character

# **create_character_characters_create_post**
> CharacterResponseSchema create_character_characters_create_post(body)

Create Character

Create new character on your account. You can create up to 5 characters.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CharactersApi(swagger_client.ApiClient(configuration))
body = swagger_client.AddCharacterSchema() # AddCharacterSchema | 

try:
    # Create Character
    api_response = api_instance.create_character_characters_create_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CharactersApi->create_character_characters_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddCharacterSchema**](AddCharacterSchema.md)|  | 

### Return type

[**CharacterResponseSchema**](CharacterResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_character_characters_delete_post**
> CharacterResponseSchema delete_character_characters_delete_post(body)

Delete Character

Delete character on your account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CharactersApi(swagger_client.ApiClient(configuration))
body = swagger_client.DeleteCharacterSchema() # DeleteCharacterSchema | 

try:
    # Delete Character
    api_response = api_instance.delete_character_characters_delete_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CharactersApi->delete_character_characters_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteCharacterSchema**](DeleteCharacterSchema.md)|  | 

### Return type

[**CharacterResponseSchema**](CharacterResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_characters_characters_get**
> DataPageCharacterSchema_ get_all_characters_characters_get(page=page, size=size)

Get All Characters

Fetch characters details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CharactersApi()
page = 1 # object | Page number (optional) (default to 1)
size = 50 # object | Page size (optional) (default to 50)

try:
    # Get All Characters
    api_response = api_instance.get_all_characters_characters_get(page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CharactersApi->get_all_characters_characters_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | [**object**](.md)| Page number | [optional] [default to 1]
 **size** | [**object**](.md)| Page size | [optional] [default to 50]

### Return type

[**DataPageCharacterSchema_**](DataPageCharacterSchema_.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_character_achievements_characters_name_achievements_get**
> DataPageAchievementSchema_ get_character_achievements_characters_name_achievements_get(name, type=type, completed=completed, page=page, size=size)

Get Character Achievements

Retrieve the details of a character.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CharactersApi()
name = NULL # object | The character name.
type = NULL # object | Type of achievements. (optional)
completed = NULL # object | Filter by completed achievements. (optional)
page = 1 # object | Page number (optional) (default to 1)
size = 50 # object | Page size (optional) (default to 50)

try:
    # Get Character Achievements
    api_response = api_instance.get_character_achievements_characters_name_achievements_get(name, type=type, completed=completed, page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CharactersApi->get_character_achievements_characters_name_achievements_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | [**object**](.md)| The character name. | 
 **type** | [**object**](.md)| Type of achievements. | [optional] 
 **completed** | [**object**](.md)| Filter by completed achievements. | [optional] 
 **page** | [**object**](.md)| Page number | [optional] [default to 1]
 **size** | [**object**](.md)| Page size | [optional] [default to 50]

### Return type

[**DataPageAchievementSchema_**](DataPageAchievementSchema_.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_character_characters_name_get**
> CharacterResponseSchema get_character_characters_name_get(name)

Get Character

Retrieve the details of a character.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CharactersApi()
name = NULL # object | The character name.

try:
    # Get Character
    api_response = api_instance.get_character_characters_name_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CharactersApi->get_character_characters_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | [**object**](.md)| The character name. | 

### Return type

[**CharacterResponseSchema**](CharacterResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

