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
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt
from raassdkpy.models.match_name_results import MatchNameResults

class ValidateName(BaseModel):
    """
    ValidateName
    """
    is_matched: StrictBool = Field(..., alias="isMatched")
    score: Union[StrictFloat, StrictInt] = Field(...)
    match_name_results: Optional[MatchNameResults] = Field(None, alias="matchNameResults")
    __properties = ["isMatched", "score", "matchNameResults"]

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
    def from_json(cls, json_str: str) -> ValidateName:
        """Create an instance of ValidateName from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of match_name_results
        if self.match_name_results:
            _dict['matchNameResults'] = self.match_name_results.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ValidateName:
        """Create an instance of ValidateName from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ValidateName.parse_obj(obj)

        _obj = ValidateName.parse_obj({
            "is_matched": obj.get("isMatched"),
            "score": obj.get("score"),
            "match_name_results": MatchNameResults.from_dict(obj.get("matchNameResults")) if obj.get("matchNameResults") is not None else None
        })
        return _obj


