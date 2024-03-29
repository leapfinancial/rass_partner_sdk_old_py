# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.default_api import DefaultApi  # noqa: E501


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_add_bank_account(self) -> None:
        """Test case for add_bank_account

        """
        pass

    def test_add_card(self) -> None:
        """Test case for add_card

        """
        pass

    def test_create_contact(self) -> None:
        """Test case for create_contact

        """
        pass

    def test_create_pin(self) -> None:
        """Test case for create_pin

        """
        pass

    def test_delete_payment_method(self) -> None:
        """Test case for delete_payment_method

        """
        pass

    def test_get_available_operation_type(self) -> None:
        """Test case for get_available_operation_type

        """
        pass

    def test_get_available_payment_methods(self) -> None:
        """Test case for get_available_payment_methods

        """
        pass

    def test_get_cash_operators(self) -> None:
        """Test case for get_cash_operators

        """
        pass

    def test_get_cip_info(self) -> None:
        """Test case for get_cip_info

        """
        pass

    def test_get_corridors(self) -> None:
        """Test case for get_corridors

        """
        pass

    def test_get_destination_sof_for_requet_money_operation(self) -> None:
        """Test case for get_destination_sof_for_requet_money_operation

        """
        pass

    def test_get_exchange_rates(self) -> None:
        """Test case for get_exchange_rates

        """
        pass

    def test_get_in_and_out_operations(self) -> None:
        """Test case for get_in_and_out_operations

        """
        pass

    def test_get_operation(self) -> None:
        """Test case for get_operation

        """
        pass

    def test_get_operation_quote(self) -> None:
        """Test case for get_operation_quote

        """
        pass

    def test_get_payment_method(self) -> None:
        """Test case for get_payment_method

        """
        pass

    def test_get_payment_method_v2(self) -> None:
        """Test case for get_payment_method_v2

        """
        pass

    def test_get_profile(self) -> None:
        """Test case for get_profile

        """
        pass

    def test_get_redis_status(self) -> None:
        """Test case for get_redis_status

        """
        pass

    def test_get_session_link(self) -> None:
        """Test case for get_session_link

        """
        pass

    def test_get_sof_for_send_money_operation(self) -> None:
        """Test case for get_sof_for_send_money_operation

        """
        pass

    def test_get_user_token(self) -> None:
        """Test case for get_user_token

        """
        pass

    def test_get_while_label_link(self) -> None:
        """Test case for get_while_label_link

        """
        pass

    def test_is_phone_available(self) -> None:
        """Test case for is_phone_available

        """
        pass

    def test_list_contacts(self) -> None:
        """Test case for list_contacts

        """
        pass

    def test_perform_level_one(self) -> None:
        """Test case for perform_level_one

        """
        pass

    def test_perform_resubmit_upgrade_level(self) -> None:
        """Test case for perform_resubmit_upgrade_level

        """
        pass

    def test_pre_quote(self) -> None:
        """Test case for pre_quote

        """
        pass

    def test_receive(self) -> None:
        """Test case for receive

        """
        pass

    def test_register_user(self) -> None:
        """Test case for register_user

        """
        pass

    def test_register_user_v2(self) -> None:
        """Test case for register_user_v2

        """
        pass

    def test_request_otp(self) -> None:
        """Test case for request_otp

        """
        pass

    def test_request_v2(self) -> None:
        """Test case for request_v2

        """
        pass

    def test_send(self) -> None:
        """Test case for send

        """
        pass

    def test_set_alternate_cip(self) -> None:
        """Test case for set_alternate_cip

        """
        pass

    def test_set_level_two(self) -> None:
        """Test case for set_level_two

        """
        pass

    def test_set_reference_code(self) -> None:
        """Test case for set_reference_code

        """
        pass

    def test_set_trusted_level_two(self) -> None:
        """Test case for set_trusted_level_two

        """
        pass

    def test_status(self) -> None:
        """Test case for status

        """
        pass

    def test_update_profile(self) -> None:
        """Test case for update_profile

        """
        pass

    def test_updated_contact(self) -> None:
        """Test case for updated_contact

        """
        pass

    def test_validate_otp(self) -> None:
        """Test case for validate_otp

        """
        pass

    def test_validate_phone_number(self) -> None:
        """Test case for validate_phone_number

        """
        pass

    def test_validate_pin_code(self) -> None:
        """Test case for validate_pin_code

        """
        pass


if __name__ == '__main__':
    unittest.main()
