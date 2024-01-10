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
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from openapi_client.models.cip_document import CIPDocument

class CIP(BaseModel):
    """
    CIP
    """
    sent: Optional[StrictBool] = None
    touched: Optional[StrictBool] = None
    rejected: Optional[StrictBool] = None
    manual_required: Optional[StrictBool] = None
    message: Optional[StrictStr] = None
    documents: Optional[conlist(CIPDocument)] = None
    updated_at: Optional[datetime] = Field(None, alias="updatedAt")
    facematch_sent: Optional[StrictBool] = None
    facematch_ok: Optional[StrictBool] = None
    facematch_msg: Optional[StrictStr] = None
    __properties = ["sent", "touched", "rejected", "manual_required", "message", "documents", "updatedAt", "facematch_sent", "facematch_ok", "facematch_msg"]

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
    def from_json(cls, json_str: str) -> CIP:
        """Create an instance of CIP from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in documents (list)
        _items = []
        if self.documents:
            for _item in self.documents:
                if _item:
                    _items.append(_item.to_dict())
            _dict['documents'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CIP:
        """Create an instance of CIP from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CIP.parse_obj(obj)

        _obj = CIP.parse_obj({
            "sent": obj.get("sent"),
            "touched": obj.get("touched"),
            "rejected": obj.get("rejected"),
            "manual_required": obj.get("manual_required"),
            "message": obj.get("message"),
            "documents": [CIPDocument.from_dict(_item) for _item in obj.get("documents")] if obj.get("documents") is not None else None,
            "updated_at": obj.get("updatedAt"),
            "facematch_sent": obj.get("facematch_sent"),
            "facematch_ok": obj.get("facematch_ok"),
            "facematch_msg": obj.get("facematch_msg")
        })
        return _obj


