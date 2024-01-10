# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.plaid_bank_validation_response import PlaidBankValidationResponse  # noqa: E501

class TestPlaidBankValidationResponse(unittest.TestCase):
    """PlaidBankValidationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlaidBankValidationResponse:
        """Test PlaidBankValidationResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlaidBankValidationResponse`
        """
        model = PlaidBankValidationResponse()  # noqa: E501
        if include_optional:
            return PlaidBankValidationResponse(
                success = True,
                access_token = '',
                item_id = '',
                account_type = '',
                account_sub_type = '',
                account_name = '',
                account_number = '',
                account_routing = '',
                bank_name = ''
            )
        else:
            return PlaidBankValidationResponse(
                success = True,
                access_token = '',
                item_id = '',
                account_type = '',
                account_sub_type = '',
                account_name = '',
                account_number = '',
                account_routing = '',
                bank_name = '',
        )
        """

    def testPlaidBankValidationResponse(self):
        """Test PlaidBankValidationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
