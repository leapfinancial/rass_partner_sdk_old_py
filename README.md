# openapi-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import openapi_client
from pprint import pprint
from openapi_client.api import file_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.scan_identity_response import ScanIdentityResponse
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = file_api.FileApi(api_client)
    phone_number = "phoneNumber_example" # str | 

    try:
        api_response = api_instance.upload_documents(phone_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling FileApi->upload_documents: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FileApi* | [**upload_documents**](docs/FileApi.md#upload_documents) | **POST** /cip/documents/{phoneNumber} | 
*FileApi* | [**upload_proof_of_life**](docs/FileApi.md#upload_proof_of_life) | **POST** /cip/proof-of-life/{phoneNumber} | 
*DefaultApi* | [**add_bank_account**](docs/DefaultApi.md#add_bank_account) | **POST** /user/funding/source/bank/add/{userToken} | 
*DefaultApi* | [**add_card**](docs/DefaultApi.md#add_card) | **POST** /user/funding/source/card/add/{userToken} | 
*DefaultApi* | [**create_contact**](docs/DefaultApi.md#create_contact) | **POST** /user/contacts/{userToken} | 
*DefaultApi* | [**create_pin**](docs/DefaultApi.md#create_pin) | **POST** /user/pin | 
*DefaultApi* | [**delete_payment_method**](docs/DefaultApi.md#delete_payment_method) | **POST** /user/funding/source/delete/{userToken} | 
*DefaultApi* | [**get_available_operation_type**](docs/DefaultApi.md#get_available_operation_type) | **GET** /user/corridors/available-operations/{userToken} | 
*DefaultApi* | [**get_available_payment_methods**](docs/DefaultApi.md#get_available_payment_methods) | **GET** /user/corridors/available-methods/{userToken} | 
*DefaultApi* | [**get_cash_operators**](docs/DefaultApi.md#get_cash_operators) | **POST** /user/funding/cash/operators/{userToken} | 
*DefaultApi* | [**get_cip_info**](docs/DefaultApi.md#get_cip_info) | **GET** /cip/process/{phoneNumber} | 
*DefaultApi* | [**get_corridors**](docs/DefaultApi.md#get_corridors) | **GET** /user/corridors | 
*DefaultApi* | [**get_destination_sof_for_requet_money_operation**](docs/DefaultApi.md#get_destination_sof_for_requet_money_operation) | **GET** /user/funding/source/request-money/{userToken} | 
*DefaultApi* | [**get_exchange_rates**](docs/DefaultApi.md#get_exchange_rates) | **GET** /user/exchange-rates/exchange-rates | 
*DefaultApi* | [**get_in_and_out_operations**](docs/DefaultApi.md#get_in_and_out_operations) | **GET** /user/operations/in-out/{userToken} | 
*DefaultApi* | [**get_operation**](docs/DefaultApi.md#get_operation) | **GET** /user/operations/detail/{id} | 
*DefaultApi* | [**get_operation_quote**](docs/DefaultApi.md#get_operation_quote) | **POST** /user/operations/quotation/{userToken} | 
*DefaultApi* | [**get_payment_method**](docs/DefaultApi.md#get_payment_method) | **GET** /user/funding/source/get-payment-method/{userToken} | 
*DefaultApi* | [**get_payment_method_v2**](docs/DefaultApi.md#get_payment_method_v2) | **GET** /user/funding/source/get-payment-method-v2/{userToken} | 
*DefaultApi* | [**get_profile**](docs/DefaultApi.md#get_profile) | **GET** /user/profile/{phone} | 
*DefaultApi* | [**get_redis_status**](docs/DefaultApi.md#get_redis_status) | **GET** /system/status/redis | 
*DefaultApi* | [**get_session_link**](docs/DefaultApi.md#get_session_link) | **POST** /auth/sessionlink | 
*DefaultApi* | [**get_sof_for_send_money_operation**](docs/DefaultApi.md#get_sof_for_send_money_operation) | **GET** /user/funding/source/send-money/{userToken} | 
*DefaultApi* | [**get_user_token**](docs/DefaultApi.md#get_user_token) | **POST** /auth/get-user-token | 
*DefaultApi* | [**get_while_label_link**](docs/DefaultApi.md#get_while_label_link) | **POST** /auth/white-label-link | 
*DefaultApi* | [**is_phone_available**](docs/DefaultApi.md#is_phone_available) | **POST** /auth/is-phone-available | 
*DefaultApi* | [**list_contacts**](docs/DefaultApi.md#list_contacts) | **GET** /user/contacts/{userToken} | 
*DefaultApi* | [**perform_level_one**](docs/DefaultApi.md#perform_level_one) | **POST** /cip/level/one/{phoneNumber} | 
*DefaultApi* | [**perform_resubmit_upgrade_level**](docs/DefaultApi.md#perform_resubmit_upgrade_level) | **POST** /cip/level/resubmit-upgrade | 
*DefaultApi* | [**pre_quote**](docs/DefaultApi.md#pre_quote) | **POST** /user/operations/pre-quote/{userToken} | 
*DefaultApi* | [**receive**](docs/DefaultApi.md#receive) | **POST** /user/operations/receive-money/{userToken} | 
*DefaultApi* | [**register_user**](docs/DefaultApi.md#register_user) | **POST** /auth/register-user | 
*DefaultApi* | [**register_user_v2**](docs/DefaultApi.md#register_user_v2) | **POST** /auth/register-user-v2 | 
*DefaultApi* | [**request_otp**](docs/DefaultApi.md#request_otp) | **POST** /auth/request-otp | 
*DefaultApi* | [**request_v2**](docs/DefaultApi.md#request_v2) | **POST** /user/operations/request-money-v2/{userToken} | 
*DefaultApi* | [**send**](docs/DefaultApi.md#send) | **POST** /user/operations/send-money/{userToken} | 
*DefaultApi* | [**set_alternate_cip**](docs/DefaultApi.md#set_alternate_cip) | **POST** /cip/alternate | 
*DefaultApi* | [**set_level_two**](docs/DefaultApi.md#set_level_two) | **POST** /cip/level/two/{phoneNumber} | 
*DefaultApi* | [**set_reference_code**](docs/DefaultApi.md#set_reference_code) | **POST** /user/funding/cash/reference-code/{userToken} | 
*DefaultApi* | [**set_trusted_level_two**](docs/DefaultApi.md#set_trusted_level_two) | **POST** /cip/level/two/{phoneNumber}/trusted | 
*DefaultApi* | [**status**](docs/DefaultApi.md#status) | **GET** /user/operations/status/{userToken}/{operationId} | 
*DefaultApi* | [**update_profile**](docs/DefaultApi.md#update_profile) | **PUT** /user/profile/{phone} | 
*DefaultApi* | [**updated_contact**](docs/DefaultApi.md#updated_contact) | **PUT** /user/contacts/{userToken} | 
*DefaultApi* | [**validate_otp**](docs/DefaultApi.md#validate_otp) | **POST** /auth/validate-otp | 
*DefaultApi* | [**validate_phone_number**](docs/DefaultApi.md#validate_phone_number) | **POST** /auth/validate-phone | 
*DefaultApi* | [**validate_pin_code**](docs/DefaultApi.md#validate_pin_code) | **POST** /user/validate-pincode | 


## Documentation For Models

 - [AddBankAccountParamsBase](docs/AddBankAccountParamsBase.md)
 - [AddCardPartnerParams](docs/AddCardPartnerParams.md)
 - [AddCardSessionParams](docs/AddCardSessionParams.md)
 - [AddPaymentMethodResponse](docs/AddPaymentMethodResponse.md)
 - [AlternateFlow](docs/AlternateFlow.md)
 - [AttachmentResponses](docs/AttachmentResponses.md)
 - [AvailablePaymentMethods](docs/AvailablePaymentMethods.md)
 - [BaseIdentity](docs/BaseIdentity.md)
 - [CIP](docs/CIP.md)
 - [CIPData](docs/CIPData.md)
 - [CIPDocument](docs/CIPDocument.md)
 - [CIPInfo](docs/CIPInfo.md)
 - [CashLocation](docs/CashLocation.md)
 - [CashNetwork](docs/CashNetwork.md)
 - [CashOperators](docs/CashOperators.md)
 - [CashOperatorsParamsBase](docs/CashOperatorsParamsBase.md)
 - [ContactInfo](docs/ContactInfo.md)
 - [CorridorDTO](docs/CorridorDTO.md)
 - [CountryAlpha2Code](docs/CountryAlpha2Code.md)
 - [CreateContactRequestParamsPartner](docs/CreateContactRequestParamsPartner.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [ErrorsCIPProcess](docs/ErrorsCIPProcess.md)
 - [EventSystem](docs/EventSystem.md)
 - [ExchangeRateDTO](docs/ExchangeRateDTO.md)
 - [FieldErrors](docs/FieldErrors.md)
 - [FieldErrorsValue](docs/FieldErrorsValue.md)
 - [GetRedisStatus200Response](docs/GetRedisStatus200Response.md)
 - [GetReferenceCodeResponse](docs/GetReferenceCodeResponse.md)
 - [GetUserToken400Response](docs/GetUserToken400Response.md)
 - [GetUserTokenParams](docs/GetUserTokenParams.md)
 - [IPhoneInfo](docs/IPhoneInfo.md)
 - [IPhoneInfoCarrier](docs/IPhoneInfoCarrier.md)
 - [IgnoredOperationData](docs/IgnoredOperationData.md)
 - [IgnoredOperationReason](docs/IgnoredOperationReason.md)
 - [IsPhoneAvailableRequest](docs/IsPhoneAvailableRequest.md)
 - [IsPhoneAvailableResponse](docs/IsPhoneAvailableResponse.md)
 - [Language](docs/Language.md)
 - [LevelOneParamsRequst](docs/LevelOneParamsRequst.md)
 - [LevelStatus](docs/LevelStatus.md)
 - [LevelStatusDetail](docs/LevelStatusDetail.md)
 - [LevelTwoParams](docs/LevelTwoParams.md)
 - [OmitCIPIdOrAttempsOrIsValidOFAC](docs/OmitCIPIdOrAttempsOrIsValidOFAC.md)
 - [OmitOperationDetailResponseIdOrTypeOrShowWarningScreen](docs/OmitOperationDetailResponseIdOrTypeOrShowWarningScreen.md)
 - [OmitValidateOTPParamsDeviceId](docs/OmitValidateOTPParamsDeviceId.md)
 - [OmitValidatePINCodeParamsDeviceId](docs/OmitValidatePINCodeParamsDeviceId.md)
 - [OperationContactData](docs/OperationContactData.md)
 - [OperationData](docs/OperationData.md)
 - [OperationDetail](docs/OperationDetail.md)
 - [OperationDetailResponse](docs/OperationDetailResponse.md)
 - [OperationResponsePartner](docs/OperationResponsePartner.md)
 - [OperationUserDetail](docs/OperationUserDetail.md)
 - [PaymentMethodResponse](docs/PaymentMethodResponse.md)
 - [PaymentMethodType](docs/PaymentMethodType.md)
 - [PaymentToken](docs/PaymentToken.md)
 - [PerformLevelOneParams](docs/PerformLevelOneParams.md)
 - [PerformResubmitUpgradeLevelParams](docs/PerformResubmitUpgradeLevelParams.md)
 - [PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFAC](docs/PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFAC.md)
 - [PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFACLolaCIP](docs/PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFACLolaCIP.md)
 - [PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen](docs/PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen.md)
 - [PickValidateOTPParamsExcludeKeyofValidateOTPParamsDeviceId](docs/PickValidateOTPParamsExcludeKeyofValidateOTPParamsDeviceId.md)
 - [PickValidatePINCodeParamsExcludeKeyofValidatePINCodeParamsDeviceId](docs/PickValidatePINCodeParamsExcludeKeyofValidatePINCodeParamsDeviceId.md)
 - [PlaidBankValidationResponse](docs/PlaidBankValidationResponse.md)
 - [PlaidURLResponsePayload](docs/PlaidURLResponsePayload.md)
 - [QuickAmount](docs/QuickAmount.md)
 - [QuoteTransactionBase](docs/QuoteTransactionBase.md)
 - [RaaSPartnerPaymentMethod](docs/RaaSPartnerPaymentMethod.md)
 - [RaaSPaymentMethod](docs/RaaSPaymentMethod.md)
 - [RaasPreQuoteRequest](docs/RaasPreQuoteRequest.md)
 - [RaasPreQuoteResponse](docs/RaasPreQuoteResponse.md)
 - [RaasPreQuoteValues](docs/RaasPreQuoteValues.md)
 - [RaasQuoteTransactionResponse](docs/RaasQuoteTransactionResponse.md)
 - [ReceiveMoneyParams](docs/ReceiveMoneyParams.md)
 - [RegisterUserParams](docs/RegisterUserParams.md)
 - [RequestMoneyBase](docs/RequestMoneyBase.md)
 - [RequestMoneyParams](docs/RequestMoneyParams.md)
 - [RequestMoneyParamsAllOf](docs/RequestMoneyParamsAllOf.md)
 - [RequestMoneyPartnerParams](docs/RequestMoneyPartnerParams.md)
 - [RequestMoneyResponse](docs/RequestMoneyResponse.md)
 - [RequestOTPParams](docs/RequestOTPParams.md)
 - [RequestOtp404Response](docs/RequestOtp404Response.md)
 - [ScanIdentityResponse](docs/ScanIdentityResponse.md)
 - [SendMoneyBase](docs/SendMoneyBase.md)
 - [SendMoneyParams](docs/SendMoneyParams.md)
 - [SendMoneyParamsAllOf](docs/SendMoneyParamsAllOf.md)
 - [SendMoneyResponse](docs/SendMoneyResponse.md)
 - [SessionLinkParams](docs/SessionLinkParams.md)
 - [SessionLinkResponse](docs/SessionLinkResponse.md)
 - [SetPincodeParams](docs/SetPincodeParams.md)
 - [SetPincodeParamsPartner](docs/SetPincodeParamsPartner.md)
 - [SetReferenceCodeParamsBase](docs/SetReferenceCodeParamsBase.md)
 - [SourceOfFunding](docs/SourceOfFunding.md)
 - [TenantOpStatusHook](docs/TenantOpStatusHook.md)
 - [UpdateContactRequestParams](docs/UpdateContactRequestParams.md)
 - [User](docs/User.md)
 - [UserDocument](docs/UserDocument.md)
 - [UserTokenResponse](docs/UserTokenResponse.md)
 - [UserUpdateParams](docs/UserUpdateParams.md)
 - [ValidateError](docs/ValidateError.md)
 - [ValidateOTP403Response](docs/ValidateOTP403Response.md)
 - [ValidateOTP500Response](docs/ValidateOTP500Response.md)
 - [ValidateOTPParamsPartner](docs/ValidateOTPParamsPartner.md)
 - [ValidatePINCodeParamsPartner](docs/ValidatePINCodeParamsPartner.md)
 - [ValidatePhoneNumberRequest](docs/ValidatePhoneNumberRequest.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: HTTP header


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in openapi_client.apis and openapi_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from openapi_client.api.default_api import DefaultApi`
- `from openapi_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import openapi_client
from openapi_client.apis import *
from openapi_client.models import *
```

