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


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, validator

class RaaSPartnerPaymentMethod(BaseModel):
    """
    RaaSPartnerPaymentMethod
    """
    currency: Optional[StrictStr] = None
    bank_account_type: Optional[StrictStr] = Field(None, alias="bankAccountType")
    cardtype: Optional[StrictStr] = None
    number: Optional[StrictStr] = None
    account_number: Optional[StrictStr] = Field(None, alias="accountNumber")
    bank_entity_number: Optional[StrictStr] = Field(None, alias="bankEntityNumber")
    bank_name: Optional[StrictStr] = Field(None, alias="bankName")
    is_primary: Optional[StrictBool] = Field(None, alias="isPrimary")
    name: Optional[StrictStr] = None
    id: Optional[StrictStr] = Field(None, alias="Id")
    __properties = ["currency", "bankAccountType", "cardtype", "number", "accountNumber", "bankEntityNumber", "bankName", "isPrimary", "name", "Id"]

    @validator('bank_account_type')
    def bank_account_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('CheckingAccount', 'SavingsAccount', 'OtherAccount'):
            raise ValueError("must be one of enum values ('CheckingAccount', 'SavingsAccount', 'OtherAccount')")
        return value

    @validator('cardtype')
    def cardtype_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('DebitCard', 'CreditCard'):
            raise ValueError("must be one of enum values ('DebitCard', 'CreditCard')")
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
    def from_json(cls, json_str: str) -> RaaSPartnerPaymentMethod:
        """Create an instance of RaaSPartnerPaymentMethod from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RaaSPartnerPaymentMethod:
        """Create an instance of RaaSPartnerPaymentMethod from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RaaSPartnerPaymentMethod.parse_obj(obj)

        _obj = RaaSPartnerPaymentMethod.parse_obj({
            "currency": obj.get("currency"),
            "bank_account_type": obj.get("bankAccountType"),
            "cardtype": obj.get("cardtype"),
            "number": obj.get("number"),
            "account_number": obj.get("accountNumber"),
            "bank_entity_number": obj.get("bankEntityNumber"),
            "bank_name": obj.get("bankName"),
            "is_primary": obj.get("isPrimary"),
            "name": obj.get("name"),
            "id": obj.get("Id")
        })
        return _obj


