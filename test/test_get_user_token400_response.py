# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.get_user_token400_response import GetUserToken400Response  # noqa: E501

class TestGetUserToken400Response(unittest.TestCase):
    """GetUserToken400Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetUserToken400Response:
        """Test GetUserToken400Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetUserToken400Response`
        """
        model = GetUserToken400Response()  # noqa: E501
        if include_optional:
            return GetUserToken400Response(
                reason = ''
            )
        else:
            return GetUserToken400Response(
                reason = '',
        )
        """

    def testGetUserToken400Response(self):
        """Test GetUserToken400Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
