# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.scan_identity_response import ScanIdentityResponse  # noqa: E501

class TestScanIdentityResponse(unittest.TestCase):
    """ScanIdentityResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScanIdentityResponse:
        """Test ScanIdentityResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScanIdentityResponse`
        """
        model = ScanIdentityResponse()  # noqa: E501
        if include_optional:
            return ScanIdentityResponse(
                id = '',
                type = 'sync',
                estimated_time = 1.337,
                method = '',
                pull_url = '',
                data = openapi_client.models.base_identity.BaseIdentity(
                    surname = '', 
                    names = '', 
                    dob = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    dob_raw = '', 
                    address = '', 
                    country = '', 
                    id_country = '', 
                    state = '', 
                    city = '', 
                    county = '', 
                    district = '', 
                    id = '', 
                    exp_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    exp_date_raw = '', 
                    gender = '', 
                    doc_type = '', 
                    nationality = '', 
                    id_validated = '', 
                    id_name = '', 
                    zipcode = '', 
                    state_code = '', 
                    county_code = '', 
                    section_code = '', 
                    locality_code = '', 
                    first_name = '', 
                    last_name = '', 
                    second_lastname = '', 
                    second_name = null, 
                    marital_status = '', 
                    maiden_name = '', 
                    third_name = '', 
                    subtype = '', ),
                attachment_responses = openapi_client.models.attachment_responses.AttachmentResponses(
                    user_document = null, 
                    selfies = null, 
                    photo_id_file_name = null, )
            )
        else:
            return ScanIdentityResponse(
                id = '',
                type = 'sync',
        )
        """

    def testScanIdentityResponse(self):
        """Test ScanIdentityResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
