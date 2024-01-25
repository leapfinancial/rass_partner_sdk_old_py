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
from raassdkpy.models.i_phone_info_carrier import IPhoneInfoCarrier

class IPhoneInfo(BaseModel):
    """
    IPhoneInfo
    """
    is_valid: Optional[StrictBool] = Field(None, alias="isValid")
    caller_name: Optional[StrictStr] = Field(None, alias="callerName")
    country_code: Optional[StrictStr] = Field(None, alias="countryCode")
    phone_number: StrictStr = Field(..., alias="phoneNumber")
    carrier: Optional[IPhoneInfoCarrier] = None
    __properties = ["isValid", "callerName", "countryCode", "phoneNumber", "carrier"]

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
    def from_json(cls, json_str: str) -> IPhoneInfo:
        """Create an instance of IPhoneInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of carrier
        if self.carrier:
            _dict['carrier'] = self.carrier.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IPhoneInfo:
        """Create an instance of IPhoneInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IPhoneInfo.parse_obj(obj)

        _obj = IPhoneInfo.parse_obj({
            "is_valid": obj.get("isValid"),
            "isValid": obj.get("isValid"),
            "caller_name": obj.get("callerName"),
            "callerName": obj.get("callerName"),
            "country_code": obj.get("countryCode"),
            "countryCode": obj.get("countryCode"),
            "phone_number": obj.get("phoneNumber"),
            "phoneNumber": obj.get("phoneNumber"),
            "carrier": IPhoneInfoCarrier.from_dict(obj.get("carrier")) if obj.get("carrier") is not None else None
        })
        return _obj


