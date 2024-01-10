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


from typing import Dict, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from openapi_client.models.field_errors_value import FieldErrorsValue

class ValidateError(BaseModel):
    """
    ValidateError
    """
    name: StrictStr = Field(...)
    message: StrictStr = Field(...)
    stack: Optional[StrictStr] = None
    status: Union[StrictFloat, StrictInt] = Field(...)
    fields: Dict[str, FieldErrorsValue] = Field(...)
    __properties = ["name", "message", "stack", "status", "fields"]

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
    def from_json(cls, json_str: str) -> ValidateError:
        """Create an instance of ValidateError from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in fields (dict)
        _field_dict = {}
        if self.fields:
            for _key in self.fields:
                if self.fields[_key]:
                    _field_dict[_key] = self.fields[_key].to_dict()
            _dict['fields'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ValidateError:
        """Create an instance of ValidateError from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ValidateError.parse_obj(obj)

        _obj = ValidateError.parse_obj({
            "name": obj.get("name"),
            "message": obj.get("message"),
            "stack": obj.get("stack"),
            "status": obj.get("status"),
            "fields": dict(
                (_k, FieldErrorsValue.from_dict(_v))
                for _k, _v in obj.get("fields").items()
            )
            if obj.get("fields") is not None
            else None
        })
        return _obj


