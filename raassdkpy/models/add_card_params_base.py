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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, validator

class AddCardParamsBase(BaseModel):
    """
    AddCardParamsBase
    """
    name: StrictStr = Field(..., description="payment method name: p.e. VISA-1111")
    type: Optional[StrictStr] = Field(None, description="Payment method type DebitCard\" | \"CreditCard\"")
    is_primary: Optional[StrictBool] = Field(None, alias="isPrimary", description="Main payment method?")
    latitude: Optional[Union[StrictFloat, StrictInt]] = None
    longitude: Optional[Union[StrictFloat, StrictInt]] = None
    cardtype: StrictStr = Field(..., description="Card type DebitCard\" | \"CreditCard\"")
    number: StrictStr = Field(..., description="Card number")
    name_on_card: StrictStr = Field(..., alias="nameOnCard")
    expiration_date: StrictStr = Field(..., alias="expirationDate")
    expiration_year: Optional[StrictStr] = Field(None, alias="expirationYear")
    expiration_month: Optional[StrictStr] = Field(None, alias="expirationMonth")
    security_code: Optional[StrictStr] = Field(None, alias="securityCode")
    token_data: Optional[StrictStr] = Field(None, alias="tokenData", description="Card full token json string")
    application: Optional[StrictStr] = None
    currency: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    card_network: StrictStr = Field(..., alias="cardNetwork")
    __properties = ["name", "type", "isPrimary", "latitude", "longitude", "cardtype", "number", "nameOnCard", "expirationDate", "expirationYear", "expirationMonth", "securityCode", "tokenData", "application", "currency", "country", "cardNetwork"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('DebitCard', 'CreditCard'):
            raise ValueError("must be one of enum values ('DebitCard', 'CreditCard')")
        return value

    @validator('cardtype')
    def cardtype_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('DebitCard', 'CreditCard'):
            raise ValueError("must be one of enum values ('DebitCard', 'CreditCard')")
        return value

    @validator('card_network')
    def card_network_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('NotApplicable', 'UATP', 'Visa', 'ChinaUnionPay', 'InterPayment', 'DiscoverCard', 'Dankort', 'Cardguard', 'MIR', 'MasterCard', 'Verve', 'InstaPayment', 'Maestro', 'DinersClubInternational', 'AmericanExpress', 'JCB', 'TROY'):
            raise ValueError("must be one of enum values ('NotApplicable', 'UATP', 'Visa', 'ChinaUnionPay', 'InterPayment', 'DiscoverCard', 'Dankort', 'Cardguard', 'MIR', 'MasterCard', 'Verve', 'InstaPayment', 'Maestro', 'DinersClubInternational', 'AmericanExpress', 'JCB', 'TROY')")
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
    def from_json(cls, json_str: str) -> AddCardParamsBase:
        """Create an instance of AddCardParamsBase from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AddCardParamsBase:
        """Create an instance of AddCardParamsBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AddCardParamsBase.parse_obj(obj)

        _obj = AddCardParamsBase.parse_obj({
            "name": obj.get("name"),
            "type": obj.get("type"),
            "is_primary": obj.get("isPrimary"),
            "latitude": obj.get("latitude"),
            "longitude": obj.get("longitude"),
            "cardtype": obj.get("cardtype"),
            "number": obj.get("number"),
            "name_on_card": obj.get("nameOnCard"),
            "expiration_date": obj.get("expirationDate"),
            "expiration_year": obj.get("expirationYear"),
            "expiration_month": obj.get("expirationMonth"),
            "security_code": obj.get("securityCode"),
            "token_data": obj.get("tokenData"),
            "application": obj.get("application"),
            "currency": obj.get("currency"),
            "country": obj.get("country"),
            "card_network": obj.get("cardNetwork")
        })
        return _obj

