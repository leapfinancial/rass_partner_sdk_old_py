# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, validator
from openapi_client.models.available_payment_methods import AvailablePaymentMethods
from openapi_client.models.payment_token import PaymentToken

class RaaSPaymentMethod(BaseModel):
    """
    RaaSPaymentMethod
    """
    payment_token: Optional[PaymentToken] = Field(None, alias="paymentToken")
    application: Optional[StrictStr] = None
    account_id: Optional[StrictStr] = Field(None, alias="accountId")
    longitude: Optional[Union[StrictFloat, StrictInt]] = None
    latitude: Optional[Union[StrictFloat, StrictInt]] = None
    phone_number: Optional[StrictStr] = Field(None, alias="phoneNumber")
    country: StrictStr = Field(...)
    zip_code: Optional[StrictStr] = Field(None, alias="zipCode")
    state: Optional[StrictStr] = None
    city: Optional[StrictStr] = None
    address2: Optional[StrictStr] = None
    address1: Optional[StrictStr] = None
    currency: Optional[StrictStr] = None
    external_id: Optional[StrictStr] = Field(None, alias="externalId")
    card_network: Optional[StrictStr] = Field(None, alias="cardNetwork")
    cardtype: Optional[StrictStr] = None
    security_code: Optional[StrictStr] = Field(None, alias="securityCode")
    expiration_month: Optional[StrictStr] = Field(None, alias="expirationMonth")
    expiration_year: Optional[StrictStr] = Field(None, alias="expirationYear")
    expiration_date: Optional[StrictStr] = Field(None, alias="expirationDate")
    name_on_card: Optional[StrictStr] = Field(None, alias="nameOnCard")
    number: Optional[StrictStr] = None
    beneficiary_account_id: Optional[StrictStr] = Field(None, alias="beneficiaryAccountId")
    token_data: Optional[StrictStr] = Field(None, alias="tokenData")
    card_type: Optional[StrictStr] = Field(None, alias="cardType")
    account_number: Optional[StrictStr] = Field(None, alias="accountNumber")
    bank_entity_number: Optional[StrictStr] = Field(None, alias="bankEntityNumber")
    bank_name: Optional[StrictStr] = Field(None, alias="bankName")
    bank_account_type: Optional[StrictStr] = Field(None, alias="bankAccountType")
    updated_at: Optional[datetime] = Field(None, alias="updatedAt")
    created_at: Optional[datetime] = Field(None, alias="createdAt")
    is_primary: Optional[StrictBool] = Field(None, alias="isPrimary")
    type: AvailablePaymentMethods = Field(...)
    name: Optional[StrictStr] = None
    id: Optional[StrictStr] = Field(None, alias="Id")
    __properties = ["paymentToken", "application", "accountId", "longitude", "latitude", "phoneNumber", "country", "zipCode", "state", "city", "address2", "address1", "currency", "externalId", "cardNetwork", "cardtype", "securityCode", "expirationMonth", "expirationYear", "expirationDate", "nameOnCard", "number", "beneficiaryAccountId", "tokenData", "cardType", "accountNumber", "bankEntityNumber", "bankName", "bankAccountType", "updatedAt", "createdAt", "isPrimary", "type", "name", "Id"]

    @validator('cardtype')
    def cardtype_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('DebitCard', 'CreditCard'):
            raise ValueError("must be one of enum values ('DebitCard', 'CreditCard')")
        return value

    @validator('card_type')
    def card_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('DebitCard', 'CreditCard'):
            raise ValueError("must be one of enum values ('DebitCard', 'CreditCard')")
        return value

    @validator('bank_account_type')
    def bank_account_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('CheckingAccount', 'SavingsAccount', 'OtherAccount'):
            raise ValueError("must be one of enum values ('CheckingAccount', 'SavingsAccount', 'OtherAccount')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> RaaSPaymentMethod:
        """Create an instance of RaaSPaymentMethod from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of payment_token
        if self.payment_token:
            _dict['paymentToken'] = self.payment_token.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RaaSPaymentMethod:
        """Create an instance of RaaSPaymentMethod from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RaaSPaymentMethod.parse_obj(obj)

        _obj = RaaSPaymentMethod.parse_obj({
            "payment_token": PaymentToken.from_dict(obj.get("paymentToken")) if obj.get("paymentToken") is not None else None,
            "application": obj.get("application"),
            "account_id": obj.get("accountId"),
            "longitude": obj.get("longitude"),
            "latitude": obj.get("latitude"),
            "phone_number": obj.get("phoneNumber"),
            "country": obj.get("country"),
            "zip_code": obj.get("zipCode"),
            "state": obj.get("state"),
            "city": obj.get("city"),
            "address2": obj.get("address2"),
            "address1": obj.get("address1"),
            "currency": obj.get("currency"),
            "external_id": obj.get("externalId"),
            "card_network": obj.get("cardNetwork"),
            "cardtype": obj.get("cardtype"),
            "security_code": obj.get("securityCode"),
            "expiration_month": obj.get("expirationMonth"),
            "expiration_year": obj.get("expirationYear"),
            "expiration_date": obj.get("expirationDate"),
            "name_on_card": obj.get("nameOnCard"),
            "number": obj.get("number"),
            "beneficiary_account_id": obj.get("beneficiaryAccountId"),
            "token_data": obj.get("tokenData"),
            "card_type": obj.get("cardType"),
            "account_number": obj.get("accountNumber"),
            "bank_entity_number": obj.get("bankEntityNumber"),
            "bank_name": obj.get("bankName"),
            "bank_account_type": obj.get("bankAccountType"),
            "updated_at": obj.get("updatedAt"),
            "created_at": obj.get("createdAt"),
            "is_primary": obj.get("isPrimary"),
            "type": obj.get("type"),
            "name": obj.get("name"),
            "id": obj.get("Id")
        })
        return _obj


