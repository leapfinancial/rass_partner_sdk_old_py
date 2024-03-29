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


from typing import Any, Dict, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr

class RaasQuoteTransactionResponse(BaseModel):
    """
    RaasQuoteTransactionResponse
    """
    id: Optional[StrictStr] = None
    source_currency: StrictStr = Field(..., alias="sourceCurrency")
    destination_currency: StrictStr = Field(..., alias="destinationCurrency")
    reason: StrictStr = Field(...)
    reason_detail: StrictStr = Field(..., alias="reasonDetail")
    source_amount: Union[StrictFloat, StrictInt] = Field(..., alias="sourceAmount")
    amount: Union[StrictFloat, StrictInt] = Field(...)
    destination_amount: Union[StrictFloat, StrictInt] = Field(..., alias="destinationAmount")
    exchange_rate: Union[StrictFloat, StrictInt] = Field(..., alias="exchangeRate")
    tax: Union[StrictFloat, StrictInt] = Field(...)
    source_fee: Union[StrictFloat, StrictInt] = Field(..., alias="sourceFee")
    destination_fee: Union[StrictFloat, StrictInt] = Field(..., alias="destinationFee")
    transaction_fee: Union[StrictFloat, StrictInt] = Field(..., alias="transactionFee")
    sender_charge_back: Union[StrictFloat, StrictInt] = Field(..., alias="senderChargeBack")
    recipient_charge_back: Union[StrictFloat, StrictInt] = Field(..., alias="recipientChargeBack")
    is_executable: StrictBool = Field(..., alias="isExecutable")
    valid_time_in_minutes: Union[StrictFloat, StrictInt] = Field(..., alias="validTimeInMinutes")
    tenant_fee: Union[StrictFloat, StrictInt] = Field(..., alias="tenantFee")
    __properties = ["id", "sourceCurrency", "destinationCurrency", "reason", "reasonDetail", "sourceAmount", "amount", "destinationAmount", "exchangeRate", "tax", "sourceFee", "destinationFee", "transactionFee", "senderChargeBack", "recipientChargeBack", "isExecutable", "validTimeInMinutes", "tenantFee"]

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
    def from_json(cls, json_str: str) -> RaasQuoteTransactionResponse:
        """Create an instance of RaasQuoteTransactionResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RaasQuoteTransactionResponse:
        """Create an instance of RaasQuoteTransactionResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RaasQuoteTransactionResponse.parse_obj(obj)

        _obj = RaasQuoteTransactionResponse.parse_obj({
            "id": obj.get("id"),
            "source_currency": obj.get("sourceCurrency"),
            "sourceCurrency": obj.get("sourceCurrency"),
            "destination_currency": obj.get("destinationCurrency"),
            "destinationCurrency": obj.get("destinationCurrency"),
            "reason": obj.get("reason"),
            "reason_detail": obj.get("reasonDetail"),
            "reasonDetail": obj.get("reasonDetail"),
            "source_amount": obj.get("sourceAmount"),
            "sourceAmount": obj.get("sourceAmount"),
            "amount": obj.get("amount"),
            "destination_amount": obj.get("destinationAmount"),
            "destinationAmount": obj.get("destinationAmount"),
            "exchange_rate": obj.get("exchangeRate"),
            "exchangeRate": obj.get("exchangeRate"),
            "tax": obj.get("tax"),
            "source_fee": obj.get("sourceFee"),
            "sourceFee": obj.get("sourceFee"),
            "destination_fee": obj.get("destinationFee"),
            "destinationFee": obj.get("destinationFee"),
            "transaction_fee": obj.get("transactionFee"),
            "transactionFee": obj.get("transactionFee"),
            "sender_charge_back": obj.get("senderChargeBack"),
            "senderChargeBack": obj.get("senderChargeBack"),
            "recipient_charge_back": obj.get("recipientChargeBack"),
            "recipientChargeBack": obj.get("recipientChargeBack"),
            "is_executable": obj.get("isExecutable"),
            "isExecutable": obj.get("isExecutable"),
            "valid_time_in_minutes": obj.get("validTimeInMinutes"),
            "validTimeInMinutes": obj.get("validTimeInMinutes"),
            "tenant_fee": obj.get("tenantFee"),
            "tenantFee": obj.get("tenantFee")
        })
        return _obj


