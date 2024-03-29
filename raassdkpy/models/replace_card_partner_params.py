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

class ReplaceCardPartnerParams(BaseModel):
    """
    ReplaceCardPartnerParams
    """
    number: StrictStr = Field(...)
    name: StrictStr = Field(...)
    cardtype: StrictStr = Field(...)
    is_primary: StrictBool = Field(..., alias="isPrimary")
    name_on_card: StrictStr = Field(..., alias="nameOnCard")
    expiration_date: StrictStr = Field(..., alias="expirationDate")
    security_code: Optional[StrictStr] = Field(None, alias="securityCode")
    currency: Optional[StrictStr] = None
    country: StrictStr = Field(...)
    card_network: StrictStr = Field(..., alias="cardNetwork")
    operation_id: StrictStr = Field(..., alias="operationId")
    __properties = ["number", "name", "cardtype", "isPrimary", "nameOnCard", "expirationDate", "securityCode", "currency", "country", "cardNetwork", "operationId"]

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
    def from_json(cls, json_str: str) -> ReplaceCardPartnerParams:
        """Create an instance of ReplaceCardPartnerParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReplaceCardPartnerParams:
        """Create an instance of ReplaceCardPartnerParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReplaceCardPartnerParams.parse_obj(obj)

        _obj = ReplaceCardPartnerParams.parse_obj({
            "number": obj.get("number"),
            "name": obj.get("name"),
            "cardtype": obj.get("cardtype"),
            "is_primary": obj.get("isPrimary"),
            "name_on_card": obj.get("nameOnCard"),
            "expiration_date": obj.get("expirationDate"),
            "security_code": obj.get("securityCode"),
            "currency": obj.get("currency"),
            "country": obj.get("country"),
            "card_network": obj.get("cardNetwork"),
            "operation_id": obj.get("operationId")
        })
        return _obj


