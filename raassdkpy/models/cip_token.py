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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist
from raassdkpy.models.lola_cip_theme_request import LolaCIPThemeRequest

class CipToken(BaseModel):
    """
    CipToken
    """
    user_id: StrictStr = Field(..., alias="userId")
    first_name: StrictStr = Field(..., alias="firstName")
    last_name: StrictStr = Field(..., alias="lastName")
    proof_of_life: Optional[StrictBool] = Field(None, alias="proofOfLife")
    validate_id_name: StrictBool = Field(..., alias="validateIdName")
    request_id: StrictBool = Field(..., alias="requestId")
    target_country: StrictStr = Field(..., alias="targetCountry")
    ttl_in_seconds: Union[StrictFloat, StrictInt] = Field(..., alias="ttlInSeconds")
    allowed_platforms: conlist(StrictStr) = Field(..., alias="allowedPlatforms")
    brand_name: StrictStr = Field(..., alias="brandName")
    webhook_url: StrictStr = Field(..., alias="webhookUrl")
    callback_url: StrictStr = Field(..., alias="callbackUrl")
    theme: LolaCIPThemeRequest = Field(...)
    id: StrictStr = Field(...)
    allowed_countries_ids: conlist(StrictStr) = Field(..., alias="allowedCountriesIds")
    language: StrictStr = Field(...)
    validate_exp_date: StrictBool = Field(..., alias="validateExpDate")
    request_selfie: Optional[StrictBool] = Field(None, alias="requestSelfie")
    claimed: StrictBool = Field(...)
    claimed_at: StrictStr = Field(..., alias="claimedAt")
    claimed_by: StrictStr = Field(..., alias="claimedBy")
    claimed_platform_id: StrictStr = Field(..., alias="claimedPlatformId")
    __properties = ["userId", "firstName", "lastName", "proofOfLife", "validateIdName", "requestId", "targetCountry", "ttlInSeconds", "allowedPlatforms", "brandName", "webhookUrl", "callbackUrl", "theme", "id", "allowedCountriesIds", "language", "validateExpDate", "requestSelfie", "claimed", "claimedAt", "claimedBy", "claimedPlatformId"]

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
    def from_json(cls, json_str: str) -> CipToken:
        """Create an instance of CipToken from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of theme
        if self.theme:
            _dict['theme'] = self.theme.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CipToken:
        """Create an instance of CipToken from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CipToken.parse_obj(obj)

        _obj = CipToken.parse_obj({
            "user_id": obj.get("userId"),
            "first_name": obj.get("firstName"),
            "last_name": obj.get("lastName"),
            "proof_of_life": obj.get("proofOfLife"),
            "validate_id_name": obj.get("validateIdName"),
            "request_id": obj.get("requestId"),
            "target_country": obj.get("targetCountry"),
            "ttl_in_seconds": obj.get("ttlInSeconds"),
            "allowed_platforms": obj.get("allowedPlatforms"),
            "brand_name": obj.get("brandName"),
            "webhook_url": obj.get("webhookUrl"),
            "callback_url": obj.get("callbackUrl"),
            "theme": LolaCIPThemeRequest.from_dict(obj.get("theme")) if obj.get("theme") is not None else None,
            "id": obj.get("id"),
            "allowed_countries_ids": obj.get("allowedCountriesIds"),
            "language": obj.get("language"),
            "validate_exp_date": obj.get("validateExpDate"),
            "request_selfie": obj.get("requestSelfie"),
            "claimed": obj.get("claimed"),
            "claimed_at": obj.get("claimedAt"),
            "claimed_by": obj.get("claimedBy"),
            "claimed_platform_id": obj.get("claimedPlatformId")
        })
        return _obj

