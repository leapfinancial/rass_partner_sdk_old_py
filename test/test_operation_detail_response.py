# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.operation_detail_response import OperationDetailResponse  # noqa: E501

class TestOperationDetailResponse(unittest.TestCase):
    """OperationDetailResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OperationDetailResponse:
        """Test OperationDetailResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OperationDetailResponse`
        """
        model = OperationDetailResponse()  # noqa: E501
        if include_optional:
            return OperationDetailResponse(
                tenantfee = 1.337,
                ignored_data = openapi_client.models.ignored_operation_data.IgnoredOperationData(
                    description = '', 
                    date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    notify_support = True, 
                    reason = 'I_DONT_RECOGNIZE_CONTACT', 
                    responsible_user_id = '', ),
                is_ignored = True,
                attribution_link = '',
                to_user = openapi_client.models.operation_user_detail.OperationUserDetail(
                    profile_picture_url = '', 
                    country = '', 
                    image_url = '', 
                    email = '', 
                    phone_number = '', 
                    last_name = '', 
                    first_name = '', ),
                from_user = openapi_client.models.operation_user_detail.OperationUserDetail(
                    profile_picture_url = '', 
                    country = '', 
                    image_url = '', 
                    email = '', 
                    phone_number = '', 
                    last_name = '', 
                    first_name = '', ),
                has_reference_code = True,
                exchange_rate = 1.337,
                destination_fee = 1.337,
                transaction_fee = 1.337,
                source_fee = 1.337,
                destination_payment_method = openapi_client.models.payment_method_response.PaymentMethodResponse(
                    name = '', 
                    type = '', 
                    is_primary = True, 
                    account_number = '', 
                    currency = '', 
                    country = '', 
                    number = '', 
                    id = '', ),
                source_payment_method = openapi_client.models.payment_method_response.PaymentMethodResponse(
                    name = '', 
                    type = '', 
                    is_primary = True, 
                    account_number = '', 
                    currency = '', 
                    country = '', 
                    number = '', 
                    id = '', ),
                recipient_currency = '',
                sender_currency = '',
                currency = '',
                show_warning_screen = True,
                sender_amount = 1.337,
                recipient_amout = 1.337,
                code = '',
                reason = '',
                mobile_status = '',
                status_details = '',
                status = '',
                amount = 1.337,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                type = '',
                correlation_id = '',
                plat_id = '',
                id = ''
            )
        else:
            return OperationDetailResponse(
                to_user = openapi_client.models.operation_user_detail.OperationUserDetail(
                    profile_picture_url = '', 
                    country = '', 
                    image_url = '', 
                    email = '', 
                    phone_number = '', 
                    last_name = '', 
                    first_name = '', ),
                from_user = openapi_client.models.operation_user_detail.OperationUserDetail(
                    profile_picture_url = '', 
                    country = '', 
                    image_url = '', 
                    email = '', 
                    phone_number = '', 
                    last_name = '', 
                    first_name = '', ),
                show_warning_screen = True,
                recipient_amout = 1.337,
                code = '',
                status = '',
                amount = 1.337,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                type = '',
                correlation_id = '',
                id = '',
        )
        """

    def testOperationDetailResponse(self):
        """Test OperationDetailResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
