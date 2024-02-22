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
from pydantic import BaseModel, Field, StrictBool, StrictStr

class SourceOfFunding(BaseModel):
    """
    simplifies delivered response for sources of funding  # noqa: E501
    """
    id: Optional[StrictStr] = None
    is_primary: Optional[StrictBool] = Field(None, alias="isPrimary", description="Subscriber's main source of funding")
    account_number: StrictStr = Field(..., alias="accountNumber", description="Bank account number")
    bank_entity_number: StrictStr = Field(..., alias="bankEntityNumber")
    type: StrictStr = Field(..., description="Source of funding type: MobileWallet|BankAccount|DebitCard|CreditCard|CashLoadLocaion|CashPayoutLocation|MTOLoad|None|StorePay\"")
    expiration_date: StrictStr = Field(..., alias="expirationDate", description="Credit/Debit card expiration date")
    expiration_month: StrictStr = Field(..., alias="expirationMonth", description="Credit/Debit card expiration month")
    expiration_year: StrictStr = Field(..., alias="expirationYear", description="Credit/Debit card expiration year")
    card_type: StrictStr = Field(..., alias="cardType", description="Card type: Credit|Debit")
    number: StrictStr = Field(..., description="Credit/Debit card number")
    name: Optional[StrictStr] = Field(None, description="Credit/Debit card holder name. Account name.")
    token_data: StrictStr = Field(..., alias="tokenData", description="Tokenized card data.")
    card_network: Optional[StrictStr] = Field(None, alias="cardNetwork")
    currency: Optional[StrictStr] = None
    __properties = ["id", "isPrimary", "accountNumber", "bankEntityNumber", "type", "expirationDate", "expirationMonth", "expirationYear", "cardType", "number", "name", "tokenData", "cardNetwork", "currency"]

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
    def from_json(cls, json_str: str) -> SourceOfFunding:
        """Create an instance of SourceOfFunding from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SourceOfFunding:
        """Create an instance of SourceOfFunding from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SourceOfFunding.parse_obj(obj)

        _obj = SourceOfFunding.parse_obj({
            "id": obj.get("id"),
            "is_primary": obj.get("isPrimary"),
            "account_number": obj.get("accountNumber"),
            "bank_entity_number": obj.get("bankEntityNumber"),
            "type": obj.get("type"),
            "expiration_date": obj.get("expirationDate"),
            "expiration_month": obj.get("expirationMonth"),
            "expiration_year": obj.get("expirationYear"),
            "card_type": obj.get("cardType"),
            "number": obj.get("number"),
            "name": obj.get("name"),
            "token_data": obj.get("tokenData"),
            "card_network": obj.get("cardNetwork"),
            "currency": obj.get("currency"),
            "isPrimary": obj.get("isPrimary"),
            "accountNumber": obj.get("accountNumber"),
            "bankEntityNumber": obj.get("bankEntityNumber"),
            "expirationDate": obj.get("expirationDate"),
            "expirationMonth": obj.get("expirationMonth"),
            "expirationYear": obj.get("expirationYear"),
            "cardType": obj.get("cardType"),
            "tokenData": obj.get("tokenData"),
            "cardNetwork": obj.get("cardNetwork")
        })
        return _obj


