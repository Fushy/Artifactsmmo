# swagger_client.MyAccountApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_password_my_change_password_post**](MyAccountApi.md#change_password_my_change_password_post) | **POST** /my/change_password | Change Password
[**get_bank_details_my_bank_get**](MyAccountApi.md#get_bank_details_my_bank_get) | **GET** /my/bank | Get Bank Details
[**get_bank_items_my_bank_items_get**](MyAccountApi.md#get_bank_items_my_bank_items_get) | **GET** /my/bank/items | Get Bank Items

# **change_password_my_change_password_post**
> ResponseSchema change_password_my_change_password_post(body)

Change Password

Change your account password. Changing the password reset the account token.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MyAccountApi(swagger_client.ApiClient(configuration))
body = swagger_client.ChangePassword() # ChangePassword | 

try:
    # Change Password
    api_response = api_instance.change_password_my_change_password_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyAccountApi->change_password_my_change_password_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChangePassword**](ChangePassword.md)|  | 

### Return type

[**ResponseSchema**](ResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_details_my_bank_get**
> BankResponseSchema get_bank_details_my_bank_get()

Get Bank Details

Fetch bank details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MyAccountApi(swagger_client.ApiClient(configuration))

try:
    # Get Bank Details
    api_response = api_instance.get_bank_details_my_bank_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyAccountApi->get_bank_details_my_bank_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BankResponseSchema**](BankResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_items_my_bank_items_get**
> DataPageSimpleItemSchema_ get_bank_items_my_bank_items_get(item_code=item_code, page=page, size=size)

Get Bank Items

Fetch all items in your bank.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.MyAccountApi(swagger_client.ApiClient(configuration))
item_code = NULL # object | Item to search in your bank. (optional)
page = 1 # object | Page number (optional) (default to 1)
size = 50 # object | Page size (optional) (default to 50)

try:
    # Get Bank Items
    api_response = api_instance.get_bank_items_my_bank_items_get(item_code=item_code, page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MyAccountApi->get_bank_items_my_bank_items_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_code** | [**object**](.md)| Item to search in your bank. | [optional] 
 **page** | [**object**](.md)| Page number | [optional] [default to 1]
 **size** | [**object**](.md)| Page size | [optional] [default to 50]

### Return type

[**DataPageSimpleItemSchema_**](DataPageSimpleItemSchema_.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

