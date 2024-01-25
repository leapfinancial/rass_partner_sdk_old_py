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
from pydantic import BaseModel, Field, StrictStr, validator
from raassdkpy.models.country_alpha2_code import CountryAlpha2Code

class RegisterUserParams(BaseModel):
    """
    RegisterUserParams
    """
    phone_number: StrictStr = Field(..., alias="phoneNumber")
    last_name: StrictStr = Field(..., alias="lastName")
    last_name2: Optional[StrictStr] = Field(None, alias="lastName2")
    gender: Optional[StrictStr] = None
    dob: Optional[datetime] = None
    email: Optional[StrictStr] = None
    first_name: StrictStr = Field(..., alias="firstName")
    middle_name: Optional[StrictStr] = Field(None, alias="middleName")
    address1: StrictStr = Field(...)
    address2: Optional[StrictStr] = None
    country_code: CountryAlpha2Code = Field(..., alias="countryCode")
    city: StrictStr = Field(...)
    zip_code: Optional[StrictStr] = Field(None, alias="zipCode")
    state: StrictStr = Field(...)
    birth_state: Optional[StrictStr] = Field(None, alias="birthState")
    __properties = ["phoneNumber", "lastName", "lastName2", "gender", "dob", "email", "firstName", "middleName", "address1", "address2", "countryCode", "city", "zipCode", "state", "birthState"]

    @validator('gender')
    def gender_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Male', 'Female'):
            raise ValueError("must be one of enum values ('Male', 'Female')")
        return value

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
    def from_json(cls, json_str: str) -> RegisterUserParams:
        """Create an instance of RegisterUserParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RegisterUserParams:
        """Create an instance of RegisterUserParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RegisterUserParams.parse_obj(obj)

        _obj = RegisterUserParams.parse_obj({
            "phone_number": obj.get("phoneNumber"),
            "last_name": obj.get("lastName"),
            "last_name2": obj.get("lastName2"),
            "gender": obj.get("gender"),
            "dob": obj.get("dob"),
            "email": obj.get("email"),
            "first_name": obj.get("firstName"),
            "middle_name": obj.get("middleName"),
            "address1": obj.get("address1"),
            "address2": obj.get("address2"),
            "country_code": obj.get("countryCode"),
            "city": obj.get("city"),
            "zip_code": obj.get("zipCode"),
            "state": obj.get("state"),
            "birth_state": obj.get("birthState")
        })
        return _obj


