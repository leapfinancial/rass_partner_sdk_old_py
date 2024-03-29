# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.request_money_response import RequestMoneyResponse  # noqa: E501

class TestRequestMoneyResponse(unittest.TestCase):
    """RequestMoneyResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RequestMoneyResponse:
        """Test RequestMoneyResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RequestMoneyResponse`
        """
        model = RequestMoneyResponse()  # noqa: E501
        if include_optional:
            return RequestMoneyResponse(
                operation = openapi_client.models.operation_data.OperationData(
                    id = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    status = '', 
                    code = '', 
                    created_by = '', 
                    correlation_id = '', 
                    sender = openapi_client.models.operation_contact_data.OperationContactData(
                        id = '', 
                        contact_id = '', 
                        country_code = '', 
                        mobile_phone = '', 
                        first_name = '', 
                        middle_name = '', 
                        last_name = '', 
                        last_name2 = '', 
                        email = '', 
                        relationship = '', ), 
                    recipient = openapi_client.models.operation_contact_data.OperationContactData(
                        id = '', 
                        contact_id = '', 
                        country_code = '', 
                        mobile_phone = '', 
                        first_name = '', 
                        middle_name = '', 
                        last_name = '', 
                        last_name2 = '', 
                        email = '', 
                        relationship = '', ), 
                    source_payment_method = null, 
                    destination_payment_method = null, 
                    amount = 1.337, 
                    currency = '', 
                    sender_amount = 1.337, 
                    sender_currency = '', 
                    recipient_amount = 1.337, 
                    recipient_currency = '', 
                    exchange_rate = 1.337, 
                    fee_payer = '', ),
                link = ''
            )
        else:
            return RequestMoneyResponse(
                operation = openapi_client.models.operation_data.OperationData(
                    id = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    status = '', 
                    code = '', 
                    created_by = '', 
                    correlation_id = '', 
                    sender = openapi_client.models.operation_contact_data.OperationContactData(
                        id = '', 
                        contact_id = '', 
                        country_code = '', 
                        mobile_phone = '', 
                        first_name = '', 
                        middle_name = '', 
                        last_name = '', 
                        last_name2 = '', 
                        email = '', 
                        relationship = '', ), 
                    recipient = openapi_client.models.operation_contact_data.OperationContactData(
                        id = '', 
                        contact_id = '', 
                        country_code = '', 
                        mobile_phone = '', 
                        first_name = '', 
                        middle_name = '', 
                        last_name = '', 
                        last_name2 = '', 
                        email = '', 
                        relationship = '', ), 
                    source_payment_method = null, 
                    destination_payment_method = null, 
                    amount = 1.337, 
                    currency = '', 
                    sender_amount = 1.337, 
                    sender_currency = '', 
                    recipient_amount = 1.337, 
                    recipient_currency = '', 
                    exchange_rate = 1.337, 
                    fee_payer = '', ),
                link = '',
        )
        """

    def testRequestMoneyResponse(self):
        """Test RequestMoneyResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
