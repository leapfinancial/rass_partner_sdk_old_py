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
from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.payment_method_type import PaymentMethodType

class PaymentToken(BaseModel):
    """
    PaymentToken
    """
    payment_type: Optional[PaymentMethodType] = Field(None, alias="paymentType")
    display_name: Optional[StrictStr] = Field(None, alias="displayName")
    transaction_identifier: Optional[StrictStr] = Field(None, alias="transactionIdentifier")
    payment_network: Optional[StrictStr] = Field(None, alias="paymentNetwork")
    data: StrictStr = Field(...)
    __properties = ["paymentType", "displayName", "transactionIdentifier", "paymentNetwork", "data"]

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
    def from_json(cls, json_str: str) -> PaymentToken:
        """Create an instance of PaymentToken from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PaymentToken:
        """Create an instance of PaymentToken from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PaymentToken.parse_obj(obj)

        _obj = PaymentToken.parse_obj({
            "payment_type": obj.get("paymentType"),
            "display_name": obj.get("displayName"),
            "transaction_identifier": obj.get("transactionIdentifier"),
            "payment_network": obj.get("paymentNetwork"),
            "data": obj.get("data")
        })
        return _obj


