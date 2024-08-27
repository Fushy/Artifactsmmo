# swagger_client.AccountsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account_accounts_create_post**](AccountsApi.md#create_account_accounts_create_post) | **POST** /accounts/create | Create Account

# **create_account_accounts_create_post**
> ResponseSchema create_account_accounts_create_post(body)

Create Account

Create an account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
body = swagger_client.AddAccountSchema() # AddAccountSchema | 

try:
    # Create Account
    api_response = api_instance.create_account_accounts_create_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->create_account_accounts_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddAccountSchema**](AddAccountSchema.md)|  | 

### Return type

[**ResponseSchema**](ResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

