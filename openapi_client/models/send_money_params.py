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
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, validator
from openapi_client.models.raa_s_payment_method import RaaSPaymentMethod

class SendMoneyParams(BaseModel):
    """
    SendMoneyParams
    """
    correlation_id: StrictStr = Field(..., alias="correlationId")
    source_payment_method: RaaSPaymentMethod = Field(..., alias="sourcePaymentMethod")
    destination_payment_method: Optional[RaaSPaymentMethod] = Field(None, alias="destinationPaymentMethod")
    amount: Union[StrictFloat, StrictInt] = Field(...)
    currency: StrictStr = Field(...)
    code: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    sender_amount: Union[StrictFloat, StrictInt] = Field(..., alias="senderAmount")
    sender_currency: StrictStr = Field(..., alias="senderCurrency")
    recipient_amount: Union[StrictFloat, StrictInt] = Field(..., alias="recipientAmount")
    recipient_currency: StrictStr = Field(..., alias="recipientCurrency")
    fee_type: StrictStr = Field(..., alias="feeType")
    source_fee: Union[StrictFloat, StrictInt] = Field(..., alias="sourceFee")
    transaction_fee: Union[StrictFloat, StrictInt] = Field(..., alias="transactionFee")
    destination_fee: Union[StrictFloat, StrictInt] = Field(..., alias="destinationFee")
    exchange_rate: Union[StrictFloat, StrictInt] = Field(..., alias="exchangeRate")
    call_location_longitude: Union[StrictFloat, StrictInt] = Field(..., alias="callLocationLongitude")
    call_location_latitude: Union[StrictFloat, StrictInt] = Field(..., alias="callLocationLatitude")
    reason: Optional[StrictStr] = None
    tenant_id: Optional[StrictStr] = Field(None, alias="tenantId")
    user_tenant_id: Optional[StrictStr] = Field(None, alias="userTenantId")
    tenant_fee: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="tenantFee")
    send_to: StrictStr = Field(..., alias="sendTo")
    __properties = ["correlationId", "sourcePaymentMethod", "destinationPaymentMethod", "amount", "currency", "code", "status", "senderAmount", "senderCurrency", "recipientAmount", "recipientCurrency", "feeType", "sourceFee", "transactionFee", "destinationFee", "exchangeRate", "callLocationLongitude", "callLocationLatitude", "reason", "tenantId", "userTenantId", "tenantFee", "sendTo"]

    @validator('fee_type')
    def fee_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('UserPays', 'ThirdPartyPays', 'SplitPay'):
            raise ValueError("must be one of enum values ('UserPays', 'ThirdPartyPays', 'SplitPay')")
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
    def from_json(cls, json_str: str) -> SendMoneyParams:
        """Create an instance of SendMoneyParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of source_payment_method
        if self.source_payment_method:
            _dict['sourcePaymentMethod'] = self.source_payment_method.to_dict()
        # override the default output from pydantic by calling `to_dict()` of destination_payment_method
        if self.destination_payment_method:
            _dict['destinationPaymentMethod'] = self.destination_payment_method.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SendMoneyParams:
        """Create an instance of SendMoneyParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SendMoneyParams.parse_obj(obj)

        _obj = SendMoneyParams.parse_obj({
            "correlation_id": obj.get("correlationId"),
            "source_payment_method": RaaSPaymentMethod.from_dict(obj.get("sourcePaymentMethod")) if obj.get("sourcePaymentMethod") is not None else None,
            "destination_payment_method": RaaSPaymentMethod.from_dict(obj.get("destinationPaymentMethod")) if obj.get("destinationPaymentMethod") is not None else None,
            "amount": obj.get("amount"),
            "currency": obj.get("currency"),
            "code": obj.get("code"),
            "status": obj.get("status"),
            "sender_amount": obj.get("senderAmount"),
            "sender_currency": obj.get("senderCurrency"),
            "recipient_amount": obj.get("recipientAmount"),
            "recipient_currency": obj.get("recipientCurrency"),
            "fee_type": obj.get("feeType"),
            "source_fee": obj.get("sourceFee"),
            "transaction_fee": obj.get("transactionFee"),
            "destination_fee": obj.get("destinationFee"),
            "exchange_rate": obj.get("exchangeRate"),
            "call_location_longitude": obj.get("callLocationLongitude"),
            "call_location_latitude": obj.get("callLocationLatitude"),
            "reason": obj.get("reason"),
            "tenant_id": obj.get("tenantId"),
            "user_tenant_id": obj.get("userTenantId"),
            "tenant_fee": obj.get("tenantFee"),
            "send_to": obj.get("sendTo")
        })
        return _obj


