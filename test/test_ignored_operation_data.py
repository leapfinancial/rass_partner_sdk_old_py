# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.ignored_operation_data import IgnoredOperationData  # noqa: E501

class TestIgnoredOperationData(unittest.TestCase):
    """IgnoredOperationData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IgnoredOperationData:
        """Test IgnoredOperationData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IgnoredOperationData`
        """
        model = IgnoredOperationData()  # noqa: E501
        if include_optional:
            return IgnoredOperationData(
                description = '',
                var_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                notify_support = True,
                reason = 'I_DONT_RECOGNIZE_CONTACT',
                responsible_user_id = ''
            )
        else:
            return IgnoredOperationData(
                var_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                notify_support = True,
                reason = 'I_DONT_RECOGNIZE_CONTACT',
                responsible_user_id = '',
        )
        """

    def testIgnoredOperationData(self):
        """Test IgnoredOperationData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
