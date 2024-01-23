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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from raassdkpy.models.landmark import Landmark

class TemplateField(BaseModel):
    """
    TemplateField
    """
    until_landmark: Optional[Landmark] = Field(None, alias="untilLandmark")
    data_type: Optional[StrictStr] = Field(None, alias="dataType")
    field_name: Optional[StrictStr] = Field(None, alias="fieldName")
    filter_blank_spaces: Optional[StrictBool] = Field(None, alias="filterBlankSpaces")
    filter_non_az_chars: Optional[StrictBool] = Field(None, alias="filterNonAZChars")
    filter_non_number_chars: Optional[StrictBool] = Field(None, alias="filterNonNumberChars")
    height: Optional[StrictInt] = None
    join_splitted_words: Optional[StrictBool] = Field(None, alias="joinSplittedWords")
    layout: Optional[StrictStr] = None
    left: Optional[StrictInt] = None
    position: Optional[StrictStr] = None
    skip_line: Optional[StrictInt] = None
    skip_word: Optional[StrictInt] = None
    take_lines: Optional[StrictInt] = None
    text: Optional[StrictStr] = None
    top: Optional[StrictInt] = None
    type: Optional[StrictStr] = None
    width: Optional[StrictInt] = None
    skip_chars: Optional[StrictInt] = None
    take_chars: Optional[StrictInt] = None
    is_regex: Optional[StrictBool] = Field(None, alias="isRegex")
    regex: Optional[StrictStr] = None
    filter: Optional[StrictStr] = None
    __properties = ["untilLandmark", "dataType", "fieldName", "filterBlankSpaces", "filterNonAZChars", "filterNonNumberChars", "height", "joinSplittedWords", "layout", "left", "position", "skip_line", "skip_word", "take_lines", "text", "top", "type", "width", "skip_chars", "take_chars", "isRegex", "regex", "filter"]

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
    def from_json(cls, json_str: str) -> TemplateField:
        """Create an instance of TemplateField from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of until_landmark
        if self.until_landmark:
            _dict['untilLandmark'] = self.until_landmark.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TemplateField:
        """Create an instance of TemplateField from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TemplateField.parse_obj(obj)

        _obj = TemplateField.parse_obj({
            "until_landmark": Landmark.from_dict(obj.get("untilLandmark")) if obj.get("untilLandmark") is not None else None,
            "data_type": obj.get("dataType"),
            "field_name": obj.get("fieldName"),
            "filter_blank_spaces": obj.get("filterBlankSpaces"),
            "filter_non_az_chars": obj.get("filterNonAZChars"),
            "filter_non_number_chars": obj.get("filterNonNumberChars"),
            "height": obj.get("height"),
            "join_splitted_words": obj.get("joinSplittedWords"),
            "layout": obj.get("layout"),
            "left": obj.get("left"),
            "position": obj.get("position"),
            "skip_line": obj.get("skip_line"),
            "skip_word": obj.get("skip_word"),
            "take_lines": obj.get("take_lines"),
            "text": obj.get("text"),
            "top": obj.get("top"),
            "type": obj.get("type"),
            "width": obj.get("width"),
            "skip_chars": obj.get("skip_chars"),
            "take_chars": obj.get("take_chars"),
            "is_regex": obj.get("isRegex"),
            "regex": obj.get("regex"),
            "filter": obj.get("filter")
        })
        return _obj


