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
from raassdkpy.models.country_alpha2_code import CountryAlpha2Code

class CreateContactRequestParamsPartner(BaseModel):
    """
    CreateContactRequestParamsPartner
    """
    alias: Optional[StrictStr] = None
    country_code: CountryAlpha2Code = Field(..., alias="countryCode")
    phone: StrictStr = Field(...)
    last_name: StrictStr = Field(..., alias="lastName")
    first_name: StrictStr = Field(..., alias="firstName")
    email: Optional[StrictStr] = None
    __properties = ["alias", "countryCode", "phone", "lastName", "firstName", "email"]

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
    def from_json(cls, json_str: str) -> CreateContactRequestParamsPartner:
        """Create an instance of CreateContactRequestParamsPartner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateContactRequestParamsPartner:
        """Create an instance of CreateContactRequestParamsPartner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateContactRequestParamsPartner.parse_obj(obj)

        _obj = CreateContactRequestParamsPartner.parse_obj({
            "alias": obj.get("alias"),
            "country_code": obj.get("countryCode"),
            "phone": obj.get("phone"),
            "last_name": obj.get("lastName"),
            "first_name": obj.get("firstName"),
            "email": obj.get("email")
        })
        return _obj


