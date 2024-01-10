# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.plaid_url_response_payload import PlaidURLResponsePayload  # noqa: E501

class TestPlaidURLResponsePayload(unittest.TestCase):
    """PlaidURLResponsePayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlaidURLResponsePayload:
        """Test PlaidURLResponsePayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlaidURLResponsePayload`
        """
        model = PlaidURLResponsePayload()  # noqa: E501
        if include_optional:
            return PlaidURLResponsePayload(
                url = '',
                status = '',
                status_message = None,
                redirect_uri = ''
            )
        else:
            return PlaidURLResponsePayload(
                url = '',
                status = '',
                redirect_uri = '',
        )
        """

    def testPlaidURLResponsePayload(self):
        """Test PlaidURLResponsePayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
