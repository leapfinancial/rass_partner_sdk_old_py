# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.set_pincode_params import SetPincodeParams  # noqa: E501

class TestSetPincodeParams(unittest.TestCase):
    """SetPincodeParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SetPincodeParams:
        """Test SetPincodeParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SetPincodeParams`
        """
        model = SetPincodeParams()  # noqa: E501
        if include_optional:
            return SetPincodeParams(
                pincode = ''
            )
        else:
            return SetPincodeParams(
                pincode = '',
        )
        """

    def testSetPincodeParams(self):
        """Test SetPincodeParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
