# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.create_contact_request_params_partner import CreateContactRequestParamsPartner  # noqa: E501

class TestCreateContactRequestParamsPartner(unittest.TestCase):
    """CreateContactRequestParamsPartner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateContactRequestParamsPartner:
        """Test CreateContactRequestParamsPartner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateContactRequestParamsPartner`
        """
        model = CreateContactRequestParamsPartner()  # noqa: E501
        if include_optional:
            return CreateContactRequestParamsPartner(
                alias = '',
                country_code = 'AF',
                phone = '',
                last_name = '',
                first_name = '',
                email = ''
            )
        else:
            return CreateContactRequestParamsPartner(
                country_code = 'AF',
                phone = '',
                last_name = '',
                first_name = '',
        )
        """

    def testCreateContactRequestParamsPartner(self):
        """Test CreateContactRequestParamsPartner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
