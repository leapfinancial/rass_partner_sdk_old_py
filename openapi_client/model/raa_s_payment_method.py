"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from openapi_client.exceptions import ApiAttributeError


def lazy_import():
    from openapi_client.model.available_payment_methods import AvailablePaymentMethods
    from openapi_client.model.payment_token import PaymentToken
    globals()['AvailablePaymentMethods'] = AvailablePaymentMethods
    globals()['PaymentToken'] = PaymentToken


class RaaSPaymentMethod(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('cardtype',): {
            'DEBITCARD': "DebitCard",
            'CREDITCARD': "CreditCard",
        },
        ('card_type',): {
            'DEBITCARD': "DebitCard",
            'CREDITCARD': "CreditCard",
        },
        ('bank_account_type',): {
            'CHECKINGACCOUNT': "CheckingAccount",
            'SAVINGSACCOUNT': "SavingsAccount",
            'OTHERACCOUNT': "OtherAccount",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'country': (str,),  # noqa: E501
            'type': (AvailablePaymentMethods,),  # noqa: E501
            'payment_token': (PaymentToken,),  # noqa: E501
            'application': (str,),  # noqa: E501
            'account_id': (str,),  # noqa: E501
            'longitude': (float,),  # noqa: E501
            'latitude': (float,),  # noqa: E501
            'phone_number': (str,),  # noqa: E501
            'zip_code': (str,),  # noqa: E501
            'state': (str,),  # noqa: E501
            'city': (str,),  # noqa: E501
            'address2': (str,),  # noqa: E501
            'address1': (str,),  # noqa: E501
            'currency': (str,),  # noqa: E501
            'external_id': (str,),  # noqa: E501
            'card_network': (str,),  # noqa: E501
            'cardtype': (str,),  # noqa: E501
            'security_code': (str,),  # noqa: E501
            'expiration_month': (str,),  # noqa: E501
            'expiration_year': (str,),  # noqa: E501
            'expiration_date': (str,),  # noqa: E501
            'name_on_card': (str,),  # noqa: E501
            'number': (str,),  # noqa: E501
            'beneficiary_account_id': (str,),  # noqa: E501
            'token_data': (str,),  # noqa: E501
            'card_type': (str,),  # noqa: E501
            'account_number': (str,),  # noqa: E501
            'bank_entity_number': (str,),  # noqa: E501
            'bank_name': (str,),  # noqa: E501
            'bank_account_type': (str,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'is_primary': (bool,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'id': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'country': 'country',  # noqa: E501
        'type': 'type',  # noqa: E501
        'payment_token': 'paymentToken',  # noqa: E501
        'application': 'application',  # noqa: E501
        'account_id': 'accountId',  # noqa: E501
        'longitude': 'longitude',  # noqa: E501
        'latitude': 'latitude',  # noqa: E501
        'phone_number': 'phoneNumber',  # noqa: E501
        'zip_code': 'zipCode',  # noqa: E501
        'state': 'state',  # noqa: E501
        'city': 'city',  # noqa: E501
        'address2': 'address2',  # noqa: E501
        'address1': 'address1',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'external_id': 'externalId',  # noqa: E501
        'card_network': 'cardNetwork',  # noqa: E501
        'cardtype': 'cardtype',  # noqa: E501
        'security_code': 'securityCode',  # noqa: E501
        'expiration_month': 'expirationMonth',  # noqa: E501
        'expiration_year': 'expirationYear',  # noqa: E501
        'expiration_date': 'expirationDate',  # noqa: E501
        'name_on_card': 'nameOnCard',  # noqa: E501
        'number': 'number',  # noqa: E501
        'beneficiary_account_id': 'beneficiaryAccountId',  # noqa: E501
        'token_data': 'tokenData',  # noqa: E501
        'card_type': 'cardType',  # noqa: E501
        'account_number': 'accountNumber',  # noqa: E501
        'bank_entity_number': 'bankEntityNumber',  # noqa: E501
        'bank_name': 'bankName',  # noqa: E501
        'bank_account_type': 'bankAccountType',  # noqa: E501
        'updated_at': 'updatedAt',  # noqa: E501
        'created_at': 'createdAt',  # noqa: E501
        'is_primary': 'isPrimary',  # noqa: E501
        'name': 'name',  # noqa: E501
        'id': 'Id',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, country, type, *args, **kwargs):  # noqa: E501
        """RaaSPaymentMethod - a model defined in OpenAPI

        Args:
            country (str):
            type (AvailablePaymentMethods):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            payment_token (PaymentToken): [optional]  # noqa: E501
            application (str): [optional]  # noqa: E501
            account_id (str): [optional]  # noqa: E501
            longitude (float): [optional]  # noqa: E501
            latitude (float): [optional]  # noqa: E501
            phone_number (str): [optional]  # noqa: E501
            zip_code (str): [optional]  # noqa: E501
            state (str): [optional]  # noqa: E501
            city (str): [optional]  # noqa: E501
            address2 (str): [optional]  # noqa: E501
            address1 (str): [optional]  # noqa: E501
            currency (str): [optional]  # noqa: E501
            external_id (str): [optional]  # noqa: E501
            card_network (str): [optional]  # noqa: E501
            cardtype (str): [optional]  # noqa: E501
            security_code (str): [optional]  # noqa: E501
            expiration_month (str): [optional]  # noqa: E501
            expiration_year (str): [optional]  # noqa: E501
            expiration_date (str): [optional]  # noqa: E501
            name_on_card (str): [optional]  # noqa: E501
            number (str): [optional]  # noqa: E501
            beneficiary_account_id (str): [optional]  # noqa: E501
            token_data (str): [optional]  # noqa: E501
            card_type (str): [optional]  # noqa: E501
            account_number (str): [optional]  # noqa: E501
            bank_entity_number (str): [optional]  # noqa: E501
            bank_name (str): [optional]  # noqa: E501
            bank_account_type (str): [optional]  # noqa: E501
            updated_at (datetime): [optional]  # noqa: E501
            created_at (datetime): [optional]  # noqa: E501
            is_primary (bool): [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
            id (str): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.country = country
        self.type = type
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, country, type, *args, **kwargs):  # noqa: E501
        """RaaSPaymentMethod - a model defined in OpenAPI

        Args:
            country (str):
            type (AvailablePaymentMethods):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            payment_token (PaymentToken): [optional]  # noqa: E501
            application (str): [optional]  # noqa: E501
            account_id (str): [optional]  # noqa: E501
            longitude (float): [optional]  # noqa: E501
            latitude (float): [optional]  # noqa: E501
            phone_number (str): [optional]  # noqa: E501
            zip_code (str): [optional]  # noqa: E501
            state (str): [optional]  # noqa: E501
            city (str): [optional]  # noqa: E501
            address2 (str): [optional]  # noqa: E501
            address1 (str): [optional]  # noqa: E501
            currency (str): [optional]  # noqa: E501
            external_id (str): [optional]  # noqa: E501
            card_network (str): [optional]  # noqa: E501
            cardtype (str): [optional]  # noqa: E501
            security_code (str): [optional]  # noqa: E501
            expiration_month (str): [optional]  # noqa: E501
            expiration_year (str): [optional]  # noqa: E501
            expiration_date (str): [optional]  # noqa: E501
            name_on_card (str): [optional]  # noqa: E501
            number (str): [optional]  # noqa: E501
            beneficiary_account_id (str): [optional]  # noqa: E501
            token_data (str): [optional]  # noqa: E501
            card_type (str): [optional]  # noqa: E501
            account_number (str): [optional]  # noqa: E501
            bank_entity_number (str): [optional]  # noqa: E501
            bank_name (str): [optional]  # noqa: E501
            bank_account_type (str): [optional]  # noqa: E501
            updated_at (datetime): [optional]  # noqa: E501
            created_at (datetime): [optional]  # noqa: E501
            is_primary (bool): [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
            id (str): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.country = country
        self.type = type
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
