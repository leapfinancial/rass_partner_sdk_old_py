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
from pydantic import BaseModel, Field

class AttachmentResponses(BaseModel):
    """
    AttachmentResponses
    """
    user_document: Optional[Any] = Field(None, alias="userDocument")
    selfies: Optional[Any] = None
    photo_id_file_name: Optional[Any] = Field(None, alias="photoIdFileName")
    __properties = ["userDocument", "selfies", "photoIdFileName"]

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
    def from_json(cls, json_str: str) -> AttachmentResponses:
        """Create an instance of AttachmentResponses from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if user_document (nullable) is None
        # and __fields_set__ contains the field
        if self.user_document is None and "user_document" in self.__fields_set__:
            _dict['userDocument'] = None

        # set to None if selfies (nullable) is None
        # and __fields_set__ contains the field
        if self.selfies is None and "selfies" in self.__fields_set__:
            _dict['selfies'] = None

        # set to None if photo_id_file_name (nullable) is None
        # and __fields_set__ contains the field
        if self.photo_id_file_name is None and "photo_id_file_name" in self.__fields_set__:
            _dict['photoIdFileName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AttachmentResponses:
        """Create an instance of AttachmentResponses from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AttachmentResponses.parse_obj(obj)

        _obj = AttachmentResponses.parse_obj({
            "user_document": obj.get("userDocument"),
            "selfies": obj.get("selfies"),
            "photo_id_file_name": obj.get("photoIdFileName")
        })
        return _obj


