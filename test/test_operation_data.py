# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.operation_data import OperationData  # noqa: E501

class TestOperationData(unittest.TestCase):
    """OperationData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OperationData:
        """Test OperationData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OperationData`
        """
        model = OperationData()  # noqa: E501
        if include_optional:
            return OperationData(
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
                source_payment_method = None,
                destination_payment_method = None,
                amount = 1.337,
                currency = '',
                sender_amount = 1.337,
                sender_currency = '',
                recipient_amount = 1.337,
                recipient_currency = '',
                exchange_rate = 1.337,
                fee_payer = ''
            )
        else:
            return OperationData(
                id = '',
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
                source_payment_method = None,
                destination_payment_method = None,
                amount = 1.337,
                currency = '',
                sender_amount = 1.337,
                sender_currency = '',
                recipient_amount = 1.337,
                recipient_currency = '',
                exchange_rate = 1.337,
                fee_payer = '',
        )
        """

    def testOperationData(self):
        """Test OperationData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
