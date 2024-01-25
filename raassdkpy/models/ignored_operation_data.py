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
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr
from raassdkpy.models.ignored_operation_reason import IgnoredOperationReason

class IgnoredOperationData(BaseModel):
    """
    IgnoredOperationData
    """
    description: Optional[StrictStr] = None
    var_date: datetime = Field(..., alias="date")
    notify_support: StrictBool = Field(..., alias="notifySupport")
    reason: IgnoredOperationReason = Field(...)
    responsible_user_id: StrictStr = Field(..., alias="responsibleUserId")
    __properties = ["description", "date", "notifySupport", "reason", "responsibleUserId"]

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
    def from_json(cls, json_str: str) -> IgnoredOperationData:
        """Create an instance of IgnoredOperationData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IgnoredOperationData:
        """Create an instance of IgnoredOperationData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IgnoredOperationData.parse_obj(obj)

        _obj = IgnoredOperationData.parse_obj({
            "description": obj.get("description"),
            "var_date": obj.get("date"),
            "notify_support": obj.get("notifySupport"),
            "reason": obj.get("reason"),
            "responsible_user_id": obj.get("responsibleUserId")
        })
        return _obj


