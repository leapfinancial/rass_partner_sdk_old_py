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
from typing import Any, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from openapi_client.models.operation_contact_data import OperationContactData

class OperationData(BaseModel):
    """
    OperationData
    """
    id: StrictStr = Field(...)
    created_at: Optional[datetime] = Field(None, alias="createdAt")
    status: StrictStr = Field(...)
    code: StrictStr = Field(...)
    created_by: StrictStr = Field(..., alias="createdBy")
    correlation_id: StrictStr = Field(..., alias="correlationId")
    sender: OperationContactData = Field(...)
    recipient: OperationContactData = Field(...)
    source_payment_method: Optional[Any] = Field(..., alias="sourcePaymentMethod")
    destination_payment_method: Optional[Any] = Field(..., alias="destinationPaymentMethod")
    amount: Union[StrictFloat, StrictInt] = Field(...)
    currency: StrictStr = Field(...)
    sender_amount: Union[StrictFloat, StrictInt] = Field(..., alias="senderAmount")
    sender_currency: StrictStr = Field(..., alias="senderCurrency")
    recipient_amount: Union[StrictFloat, StrictInt] = Field(..., alias="recipientAmount")
    recipient_currency: StrictStr = Field(..., alias="recipientCurrency")
    exchange_rate: Union[StrictFloat, StrictInt] = Field(..., alias="exchangeRate")
    fee_payer: StrictStr = Field(..., alias="feePayer")
    __properties = ["id", "createdAt", "status", "code", "createdBy", "correlationId", "sender", "recipient", "sourcePaymentMethod", "destinationPaymentMethod", "amount", "currency", "senderAmount", "senderCurrency", "recipientAmount", "recipientCurrency", "exchangeRate", "feePayer"]

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
    def from_json(cls, json_str: str) -> OperationData:
        """Create an instance of OperationData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of sender
        if self.sender:
            _dict['sender'] = self.sender.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recipient
        if self.recipient:
            _dict['recipient'] = self.recipient.to_dict()
        # set to None if source_payment_method (nullable) is None
        # and __fields_set__ contains the field
        if self.source_payment_method is None and "source_payment_method" in self.__fields_set__:
            _dict['sourcePaymentMethod'] = None

        # set to None if destination_payment_method (nullable) is None
        # and __fields_set__ contains the field
        if self.destination_payment_method is None and "destination_payment_method" in self.__fields_set__:
            _dict['destinationPaymentMethod'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OperationData:
        """Create an instance of OperationData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OperationData.parse_obj(obj)

        _obj = OperationData.parse_obj({
            "id": obj.get("id"),
            "created_at": obj.get("createdAt"),
            "status": obj.get("status"),
            "code": obj.get("code"),
            "created_by": obj.get("createdBy"),
            "correlation_id": obj.get("correlationId"),
            "sender": OperationContactData.from_dict(obj.get("sender")) if obj.get("sender") is not None else None,
            "recipient": OperationContactData.from_dict(obj.get("recipient")) if obj.get("recipient") is not None else None,
            "source_payment_method": obj.get("sourcePaymentMethod"),
            "destination_payment_method": obj.get("destinationPaymentMethod"),
            "amount": obj.get("amount"),
            "currency": obj.get("currency"),
            "sender_amount": obj.get("senderAmount"),
            "sender_currency": obj.get("senderCurrency"),
            "recipient_amount": obj.get("recipientAmount"),
            "recipient_currency": obj.get("recipientCurrency"),
            "exchange_rate": obj.get("exchangeRate"),
            "fee_payer": obj.get("feePayer")
        })
        return _obj


