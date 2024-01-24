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
from pydantic import BaseModel, Field, StrictStr

class OperationUserDetail(BaseModel):
    """
    OperationUserDetail
    """
    profile_picture_url: Optional[StrictStr] = Field(None, alias="profilePictureUrl")
    country: Optional[StrictStr] = None
    image_url: Optional[StrictStr] = Field(None, alias="imageUrl")
    email: Optional[StrictStr] = None
    phone_number: StrictStr = Field(..., alias="phoneNumber")
    last_name: Optional[StrictStr] = Field(None, alias="lastName")
    first_name: Optional[StrictStr] = Field(None, alias="firstName")
    __properties = ["profilePictureUrl", "country", "imageUrl", "email", "phoneNumber", "lastName", "firstName"]

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
    def from_json(cls, json_str: str) -> OperationUserDetail:
        """Create an instance of OperationUserDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OperationUserDetail:
        """Create an instance of OperationUserDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OperationUserDetail.parse_obj(obj)

        _obj = OperationUserDetail.parse_obj({
            "profile_picture_url": obj.get("profilePictureUrl"),
            "country": obj.get("country"),
            "image_url": obj.get("imageUrl"),
            "email": obj.get("email"),
            "phone_number": obj.get("phoneNumber"),
            "last_name": obj.get("lastName"),
            "first_name": obj.get("firstName")
        })
        return _obj


