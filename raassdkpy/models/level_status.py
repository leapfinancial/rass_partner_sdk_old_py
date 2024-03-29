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





class LevelStatus(str, Enum):
    """
    LevelStatus
    """

    """
    allowed enum values
    """
    PENDING = 'Pending'
    ONPROCESS = 'OnProcess'
    SUCCESS = 'Success'
    FAILED = 'Failed'
    UPGRADEFAILED = 'UpgradeFailed'
    COMPLETED = 'Completed'
    UPGRADEPENDING = 'UpgradePending'
    UPGRADEINPROGRESS = 'UpgradeInProgress'
    UPGRADESOFTFAILED = 'UpgradeSoftFailed'

    @classmethod
    def from_json(cls, json_str: str) -> LevelStatus:
        """Create an instance of LevelStatus from a JSON string"""
        return LevelStatus(json.loads(json_str))


