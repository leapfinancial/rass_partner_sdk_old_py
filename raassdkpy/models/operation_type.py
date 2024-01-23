# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class OperationType(str, Enum):
    """
    OperationType
    """

    """
    allowed enum values
    """
    REQUEST = 'request'
    SEND = 'send'

    @classmethod
    def from_json(cls, json_str: str) -> OperationType:
        """Create an instance of OperationType from a JSON string"""
        return OperationType(json.loads(json_str))


