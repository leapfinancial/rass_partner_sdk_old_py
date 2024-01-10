# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.request_money_partner_params import RequestMoneyPartnerParams  # noqa: E501

class TestRequestMoneyPartnerParams(unittest.TestCase):
    """RequestMoneyPartnerParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RequestMoneyPartnerParams:
        """Test RequestMoneyPartnerParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RequestMoneyPartnerParams`
        """
        model = RequestMoneyPartnerParams()  # noqa: E501
        if include_optional:
            return RequestMoneyPartnerParams(
                request_to = '',
                correlation_id = '',
                destination_payment_method_id = '',
                recipient_amount = 1.337,
                recipient_currency = '',
                reason = ''
            )
        else:
            return RequestMoneyPartnerParams(
                request_to = '',
                correlation_id = '',
                destination_payment_method_id = '',
                recipient_amount = 1.337,
                recipient_currency = '',
        )
        """

    def testRequestMoneyPartnerParams(self):
        """Test RequestMoneyPartnerParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
