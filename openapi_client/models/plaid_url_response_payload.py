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


from typing import Any, Optional
from pydantic import BaseModel, Field, StrictStr

class PlaidURLResponsePayload(BaseModel):
    """
    PlaidURLResponsePayload
    """
    url: StrictStr = Field(...)
    status: StrictStr = Field(...)
    status_message: Optional[Any] = Field(None, alias="statusMessage")
    redirect_uri: StrictStr = Field(..., alias="redirectUri")
    __properties = ["url", "status", "statusMessage", "redirectUri"]

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
    def from_json(cls, json_str: str) -> PlaidURLResponsePayload:
        """Create an instance of PlaidURLResponsePayload from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if status_message (nullable) is None
        # and __fields_set__ contains the field
        if self.status_message is None and "status_message" in self.__fields_set__:
            _dict['statusMessage'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PlaidURLResponsePayload:
        """Create an instance of PlaidURLResponsePayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PlaidURLResponsePayload.parse_obj(obj)

        _obj = PlaidURLResponsePayload.parse_obj({
            "url": obj.get("url"),
            "status": obj.get("status"),
            "status_message": obj.get("statusMessage"),
            "redirect_uri": obj.get("redirectUri")
        })
        return _obj


