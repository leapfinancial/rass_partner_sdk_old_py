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
from pydantic import BaseModel

class INufiJobResponseData(BaseModel):
    """
    INufiJobResponseData
    """
    ocr: Optional[Any] = None
    figuras: Optional[Any] = None
    __properties = ["ocr", "figuras"]

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
    def from_json(cls, json_str: str) -> INufiJobResponseData:
        """Create an instance of INufiJobResponseData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if ocr (nullable) is None
        # and __fields_set__ contains the field
        if self.ocr is None and "ocr" in self.__fields_set__:
            _dict['ocr'] = None

        # set to None if figuras (nullable) is None
        # and __fields_set__ contains the field
        if self.figuras is None and "figuras" in self.__fields_set__:
            _dict['figuras'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> INufiJobResponseData:
        """Create an instance of INufiJobResponseData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return INufiJobResponseData.parse_obj(obj)

        _obj = INufiJobResponseData.parse_obj({
            "ocr": obj.get("ocr"),
            "figuras": obj.get("figuras")
        })
        return _obj


