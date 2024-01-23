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



from pydantic import BaseModel, Field, StrictBool, StrictStr

class RaasCloseAccountResponse(BaseModel):
    """
    RaasCloseAccountResponse
    """
    success: StrictBool = Field(...)
    error_description: StrictStr = Field(..., alias="errorDescription")
    error_code: StrictStr = Field(..., alias="errorCode")
    __properties = ["success", "errorDescription", "errorCode"]

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
    def from_json(cls, json_str: str) -> RaasCloseAccountResponse:
        """Create an instance of RaasCloseAccountResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RaasCloseAccountResponse:
        """Create an instance of RaasCloseAccountResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RaasCloseAccountResponse.parse_obj(obj)

        _obj = RaasCloseAccountResponse.parse_obj({
            "success": obj.get("success"),
            "error_description": obj.get("errorDescription"),
            "error_code": obj.get("errorCode")
        })
        return _obj


