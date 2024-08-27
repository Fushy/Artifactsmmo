# swagger_client.MyCharactersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**action_accept_new_task_my_name_action_task_new_post**](MyCharactersApi.md#action_accept_new_task_my_name_action_task_new_post) | **POST** /my/{name}/action/task/new | Action Accept New Task
[**action_buy_bank_expansion_my_name_action_bank_buy_expansion_post**](MyCharactersApi.md#action_buy_bank_expansion_my_name_action_bank_buy_expansion_post) | **POST** /my/{name}/action/bank/buy_expansion | Action Buy Bank Expansion
[**action_complete_task_my_name_action_task_complete_post**](MyCharactersApi.md#action_complete_task_my_name_action_task_complete_post) | **POST** /my/{name}/action/task/complete | Action Complete Task
[**action_crafting_my_name_action_crafting_post**](MyCharactersApi.md#action_crafting_my_name_action_crafting_post) | **POST** /my/{name}/action/crafting | Action Crafting
[**action_delete_item_my_name_action_delete_post**](MyCharactersApi.md#action_delete_item_my_name_action_delete_post) | **POST** /my/{name}/action/delete | Action Delete Item
[**action_deposit_bank_gold_my_name_action_bank_deposit_gold_post**](MyCharactersApi.md#action_deposit_bank_gold_my_name_action_bank_deposit_gold_post) | **POST** /my/{name}/action/bank/deposit/gold | Action Deposit Bank Gold
[**action_deposit_bank_my_name_action_bank_deposit_post**](MyCharactersApi.md#action_deposit_bank_my_name_action_bank_deposit_post) | **POST** /my/{name}/action/bank/deposit | Action Deposit Bank
[**action_equip_item_my_name_action_equip_post**](MyCharactersApi.md#action_equip_item_my_name_action_equip_post) | **POST** /my/{name}/action/equip | Action Equip Item
[**action_fight_my_name_action_fight_post**](MyCharactersApi.md#action_fight_my_name_action_fight_post) | **POST** /my/{name}/action/fight | Action Fight
[**action_gathering_my_name_action_gathering_post**](MyCharactersApi.md#action_gathering_my_name_action_gathering_post) | **POST** /my/{name}/action/gathering | Action Gathering
[**action_ge_buy_item_my_name_action_ge_buy_post**](MyCharactersApi.md#action_ge_buy_item_my_name_action_ge_buy_post) | **POST** /my/{name}/action/ge/buy | Action Ge Buy Item
[**action_ge_sell_item_my_name_action_ge_sell_post**](MyCharactersApi.md#action_ge_sell_item_my_name_action_ge_sell_post) | **POST** /my/{name}/action/ge/sell | Action Ge Sell Item
[**action_move_my_name_action_move_post**](MyCharactersApi.md#action_move_my_name_action_move_post) | **POST** /my/{name}/action/move | Action Move
[**action_recycling_my_name_action_recycling_post**](MyCharactersApi.md#action_recycling_my_name_action_recycling_post) | **POST** /my/{name}/action/recycling | Action Recycling
[**action_task_cancel_my_name_action_task_cancel_post**](MyCharactersApi.md#action_task_cancel_my_name_action_task_cancel_post) | **POST** /my/{name}/action/task/cancel | Action Task Cancel
[**action_task_exchange_my_name_action_task_exchange_post**](MyCharactersApi.md#action_task_exchange_my_name_action_task_exchange_post) | **POST** /my/{name}/action/task/exchange | Action Task Exchange
[**action_unequip_item_my_name_action_unequip_post**](MyCharactersApi.md#action_unequip_item_my_name_action_unequip_post) | **POST** /my/{name}/action/unequip | Action Unequip Item
[**action_withdraw_bank_gold_my_name_action_bank_withdraw_gold_post**](MyCharactersApi.md#action_withdraw_bank_gold_my_name_action_bank_withdraw_gold_post) | **POST** /my/{name}/action/bank/withdraw/gold | Action Withdraw Bank Gold
[**action_withdraw_bank_my_name_action_bank_withdraw_post**](MyCharactersApi.md#action_withdraw_bank_my_name_action_bank_withdraw_post) | **POST** /my/{name}/action/bank/withdraw | Action Withdraw Bank
[**get_all_characters_logs_my_logs_get**](MyCharactersApi.md#get_all_characters_logs_my_logs_get) | **GET** /my/logs | Get All Characters Logs
[**get_my_characters_my_characters_get**](MyCharactersApi.md#get_my_characters_my_characters_get) | **GET** /my/characters | Get My Characters

# **action_accept_new_task_my_name_action_task_new_post**
> TaskResponseSchema action_accept_new_task_my_name_action_task_new_post(name)

Action Accept New Task

Accepting a new task.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MyCharactersApi(swagger_client.ApiClient(configuration))
name = NULL # object | Name of your character.

try:
    # Action Accept New Task
    api_response = api_instance.action_accept_new_task_my_name_action_task_new_post(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyCharactersApi->action_accept_new_task_my_name_action_task_new_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | [**object**](.md)| Name of your character. | 

### Return type

[**TaskResponseSchema**](TaskResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_buy_bank_expansion_my_name_action_bank_buy_expansion_post**
> BankExtensionTransactionResponseSchema action_buy_bank_expansion_my_name_action_bank_buy_expansion_post(name)

Action Buy Bank Expansion

Buy a 20 slots bank expansion.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MyCharactersApi(swagger_client.ApiClient(configuration))
name = NULL # object | Name of your character.

try:
    # Action Buy Bank Expansion
    api_response = api_instance.action_buy_bank_expansion_my_name_action_bank_buy_expansion_post(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyCharactersApi->action_buy_bank_expansion_my_name_action_bank_buy_expansion_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | [**object**](.md)| Name of your character. | 

### Return type

[**BankExtensionTransactionResponseSchema**](BankExtensionTransactionResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_complete_task_my_name_action_task_complete_post**
> TaskRewardResponseSchema action_complete_task_my_name_action_task_complete_post(name)

Action Complete Task

Complete a task.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MyCharactersApi(swagger_client.ApiClient(configuration))
name = NULL # object | Name of your character.

try:
    # Action Complete Task
    api_response = api_instance.action_complete_task_my_name_action_task_complete_post(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyCharactersApi->action_complete_task_my_name_action_task_complete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | [**object**](.md)| Name of your character. | 

### Return type

[**TaskRewardResponseSchema**](TaskRewardResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_crafting_my_name_action_crafting_post**
> SkillResponseSchema action_crafting_my_name_action_crafting_post(body, name)

Action Crafting

Crafting an item. The character must be on a map with a workshop.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MyCharactersApi(swagger_client.ApiClient(configuration))
body = swagger_client.CraftingSchema() # CraftingSchema | 
name = NULL # object | Name of your character.

try:
    # Action Crafting
    api_response = api_instance.action_crafting_my_name_action_crafting_post(body, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyCharactersApi->action_crafting_my_name_action_crafting_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CraftingSchema**](CraftingSchema.md)|  | 
 **name** | [**object**](.md)| Name of your character. | 

### Return type

[**SkillResponseSchema**](SkillResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_delete_item_my_name_action_delete_post**
> DeleteItemResponseSchema action_delete_item_my_name_action_delete_post(body, name)

Action Delete Item

Delete an item from your character's inventory.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MyCharactersApi(swagger_client.ApiClient(configuration))
body = swagger_client.SimpleItemSchema() # SimpleItemSchema | 
name = NULL # object | Name of your character.

try:
    # Action Delete Item
    api_response = api_instance.action_delete_item_my_name_action_delete_post(body, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyCharactersApi->action_delete_item_my_name_action_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SimpleItemSchema**](SimpleItemSchema.md)|  | 
 **name** | [**object**](.md)| Name of your character. | 

### Return type

[**DeleteItemResponseSchema**](DeleteItemResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_deposit_bank_gold_my_name_action_bank_deposit_gold_post**
> BankGoldTransactionResponseSchema action_deposit_bank_gold_my_name_action_bank_deposit_gold_post(body, name)

Action Deposit Bank Gold

Deposit golds in a bank on the character's map.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MyCharactersApi(swagger_client.ApiClient(configuration))
body = swagger_client.DepositWithdrawGoldSchema() # DepositWithdrawGoldSchema | 
name = NULL # object | Name of your character.

try:
    # Action Deposit Bank Gold
    api_response = api_instance.action_deposit_bank_gold_my_name_action_bank_deposit_gold_post(body, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyCharactersApi->action_deposit_bank_gold_my_name_action_bank_deposit_gold_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DepositWithdrawGoldSchema**](DepositWithdrawGoldSchema.md)|  | 
 **name** | [**object**](.md)| Name of your character. | 

### Return type

[**BankGoldTransactionResponseSchema**](BankGoldTransactionResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_deposit_bank_my_name_action_bank_deposit_post**
> BankItemTransactionResponseSchema action_deposit_bank_my_name_action_bank_deposit_post(body, name)

Action Deposit Bank

Deposit an item in a bank on the character's map.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MyCharactersApi(swagger_client.ApiClient(configuration))
body = swagger_client.SimpleItemSchema() # SimpleItemSchema | 
name = NULL # object | Name of your character.

try:
    # Action Deposit Bank
    api_response = api_instance.action_deposit_bank_my_name_action_bank_deposit_post(body, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyCharactersApi->action_deposit_bank_my_name_action_bank_deposit_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SimpleItemSchema**](SimpleItemSchema.md)|  | 
 **name** | [**object**](.md)| Name of your character. | 

### Return type

[**BankItemTransactionResponseSchema**](BankItemTransactionResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_equip_item_my_name_action_equip_post**
> EquipmentResponseSchema action_equip_item_my_name_action_equip_post(body, name)

Action Equip Item

Equip an item on your character.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MyCharactersApi(swagger_client.ApiClient(configuration))
body = swagger_client.EquipSchema() # EquipSchema | 
name = NULL # object | Name of your character.

try:
    # Action Equip Item
    api_response = api_instance.action_equip_item_my_name_action_equip_post(body, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyCharactersApi->action_equip_item_my_name_action_equip_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EquipSchema**](EquipSchema.md)|  | 
 **name** | [**object**](.md)| Name of your character. | 

### Return type

[**EquipmentResponseSchema**](EquipmentResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_fight_my_name_action_fight_post**
> CharacterFightResponseSchema action_fight_my_name_action_fight_post(name)

Action Fight

Start a fight against a monster on the character's map.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MyCharactersApi(swagger_client.ApiClient(configuration))
name = NULL # object | Name of your character.

try:
    # Action Fight
    api_response = api_instance.action_fight_my_name_action_fight_post(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyCharactersApi->action_fight_my_name_action_fight_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | [**object**](.md)| Name of your character. | 

### Return type

[**CharacterFightResponseSchema**](CharacterFightResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_gathering_my_name_action_gathering_post**
> SkillResponseSchema action_gathering_my_name_action_gathering_post(name)

Action Gathering

Harvest a resource on the character's map.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MyCharactersApi(swagger_client.ApiClient(configuration))
name = NULL # object | Name of your character.

try:
    # Action Gathering
    api_response = api_instance.action_gathering_my_name_action_gathering_post(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyCharactersApi->action_gathering_my_name_action_gathering_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | [**object**](.md)| Name of your character. | 

### Return type

[**SkillResponseSchema**](SkillResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_ge_buy_item_my_name_action_ge_buy_post**
> GETransactionResponseSchema action_ge_buy_item_my_name_action_ge_buy_post(body, name)

Action Ge Buy Item

Buy an item at the Grand Exchange on the character's map.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MyCharactersApi(swagger_client.ApiClient(configuration))
body = swagger_client.GETransactionItemSchema() # GETransactionItemSchema | 
name = NULL # object | Name of your character.

try:
    # Action Ge Buy Item
    api_response = api_instance.action_ge_buy_item_my_name_action_ge_buy_post(body, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyCharactersApi->action_ge_buy_item_my_name_action_ge_buy_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GETransactionItemSchema**](GETransactionItemSchema.md)|  | 
 **name** | [**object**](.md)| Name of your character. | 

### Return type

[**GETransactionResponseSchema**](GETransactionResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_ge_sell_item_my_name_action_ge_sell_post**
> GETransactionResponseSchema action_ge_sell_item_my_name_action_ge_sell_post(body, name)

Action Ge Sell Item

Sell an item at the Grand Exchange on the character's map.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MyCharactersApi(swagger_client.ApiClient(configuration))
body = swagger_client.GETransactionItemSchema() # GETransactionItemSchema | 
name = NULL # object | Name of your character.

try:
    # Action Ge Sell Item
    api_response = api_instance.action_ge_sell_item_my_name_action_ge_sell_post(body, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyCharactersApi->action_ge_sell_item_my_name_action_ge_sell_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GETransactionItemSchema**](GETransactionItemSchema.md)|  | 
 **name** | [**object**](.md)| Name of your character. | 

### Return type

[**GETransactionResponseSchema**](GETransactionResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_move_my_name_action_move_post**
> CharacterMovementResponseSchema action_move_my_name_action_move_post(body, name)

Action Move

Moves a character on the map using the map's X and Y position.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MyCharactersApi(swagger_client.ApiClient(configuration))
body = swagger_client.DestinationSchema() # DestinationSchema | 
name = NULL # object | Name of your character.

try:
    # Action Move
    api_response = api_instance.action_move_my_name_action_move_post(body, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyCharactersApi->action_move_my_name_action_move_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DestinationSchema**](DestinationSchema.md)|  | 
 **name** | [**object**](.md)| Name of your character. | 

### Return type

[**CharacterMovementResponseSchema**](CharacterMovementResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_recycling_my_name_action_recycling_post**
> RecyclingResponseSchema action_recycling_my_name_action_recycling_post(body, name)

Action Recycling

Recyling an item. The character must be on a map with a workshop (only for equipments and weapons).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MyCharactersApi(swagger_client.ApiClient(configuration))
body = swagger_client.RecyclingSchema() # RecyclingSchema | 
name = NULL # object | Name of your character.

try:
    # Action Recycling
    api_response = api_instance.action_recycling_my_name_action_recycling_post(body, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyCharactersApi->action_recycling_my_name_action_recycling_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecyclingSchema**](RecyclingSchema.md)|  | 
 **name** | [**object**](.md)| Name of your character. | 

### Return type

[**RecyclingResponseSchema**](RecyclingResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_task_cancel_my_name_action_task_cancel_post**
> TaskCancelledResponseSchema action_task_cancel_my_name_action_task_cancel_post(name)

Action Task Cancel

Cancel a task for 1 tasks coin.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MyCharactersApi(swagger_client.ApiClient(configuration))
name = NULL # object | Name of your character.

try:
    # Action Task Cancel
    api_response = api_instance.action_task_cancel_my_name_action_task_cancel_post(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyCharactersApi->action_task_cancel_my_name_action_task_cancel_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | [**object**](.md)| Name of your character. | 

### Return type

[**TaskCancelledResponseSchema**](TaskCancelledResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_task_exchange_my_name_action_task_exchange_post**
> TaskRewardResponseSchema action_task_exchange_my_name_action_task_exchange_post(name)

Action Task Exchange

Exchange 3 tasks coins for a random reward. Rewards are exclusive resources for crafting  items.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MyCharactersApi(swagger_client.ApiClient(configuration))
name = NULL # object | Name of your character.

try:
    # Action Task Exchange
    api_response = api_instance.action_task_exchange_my_name_action_task_exchange_post(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyCharactersApi->action_task_exchange_my_name_action_task_exchange_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | [**object**](.md)| Name of your character. | 

### Return type

[**TaskRewardResponseSchema**](TaskRewardResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_unequip_item_my_name_action_unequip_post**
> EquipmentResponseSchema action_unequip_item_my_name_action_unequip_post(body, name)

Action Unequip Item

Unequip an item on your character.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MyCharactersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UnequipSchema() # UnequipSchema | 
name = NULL # object | Name of your character.

try:
    # Action Unequip Item
    api_response = api_instance.action_unequip_item_my_name_action_unequip_post(body, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyCharactersApi->action_unequip_item_my_name_action_unequip_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnequipSchema**](UnequipSchema.md)|  | 
 **name** | [**object**](.md)| Name of your character. | 

### Return type

[**EquipmentResponseSchema**](EquipmentResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_withdraw_bank_gold_my_name_action_bank_withdraw_gold_post**
> BankGoldTransactionResponseSchema action_withdraw_bank_gold_my_name_action_bank_withdraw_gold_post(body, name)

Action Withdraw Bank Gold

Withdraw gold from your bank.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MyCharactersApi(swagger_client.ApiClient(configuration))
body = swagger_client.DepositWithdrawGoldSchema() # DepositWithdrawGoldSchema | 
name = NULL # object | Name of your character.

try:
    # Action Withdraw Bank Gold
    api_response = api_instance.action_withdraw_bank_gold_my_name_action_bank_withdraw_gold_post(body, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyCharactersApi->action_withdraw_bank_gold_my_name_action_bank_withdraw_gold_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DepositWithdrawGoldSchema**](DepositWithdrawGoldSchema.md)|  | 
 **name** | [**object**](.md)| Name of your character. | 

### Return type

[**BankGoldTransactionResponseSchema**](BankGoldTransactionResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **action_withdraw_bank_my_name_action_bank_withdraw_post**
> BankItemTransactionResponseSchema action_withdraw_bank_my_name_action_bank_withdraw_post(body, name)

Action Withdraw Bank

Take an item from your bank and put it in the character's inventory.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MyCharactersApi(swagger_client.ApiClient(configuration))
body = swagger_client.SimpleItemSchema() # SimpleItemSchema | 
name = NULL # object | Name of your character.

try:
    # Action Withdraw Bank
    api_response = api_instance.action_withdraw_bank_my_name_action_bank_withdraw_post(body, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyCharactersApi->action_withdraw_bank_my_name_action_bank_withdraw_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SimpleItemSchema**](SimpleItemSchema.md)|  | 
 **name** | [**object**](.md)| Name of your character. | 

### Return type

[**BankItemTransactionResponseSchema**](BankItemTransactionResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_characters_logs_my_logs_get**
> DataPageLogSchema_ get_all_characters_logs_my_logs_get(page=page, size=size)

Get All Characters Logs

History of the last 100 actions of all your characters.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MyCharactersApi(swagger_client.ApiClient(configuration))
page = 1 # object | Page number (optional) (default to 1)
size = 50 # object | Page size (optional) (default to 50)

try:
    # Get All Characters Logs
    api_response = api_instance.get_all_characters_logs_my_logs_get(page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyCharactersApi->get_all_characters_logs_my_logs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | [**object**](.md)| Page number | [optional] [default to 1]
 **size** | [**object**](.md)| Page size | [optional] [default to 50]

### Return type

[**DataPageLogSchema_**](DataPageLogSchema_.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_characters_my_characters_get**
> MyCharactersListSchema get_my_characters_my_characters_get()

Get My Characters

List of your characters.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MyCharactersApi(swagger_client.ApiClient(configuration))

try:
    # Get My Characters
    api_response = api_instance.get_my_characters_my_characters_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyCharactersApi->get_my_characters_my_characters_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MyCharactersListSchema**](MyCharactersListSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

