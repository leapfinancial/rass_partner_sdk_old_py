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



class RaasQuoteTransactionResponse(ModelNormal):
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
    }

    validations = {
    }

    additional_properties_type = None

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
        return {
            'source_currency': (str,),  # noqa: E501
            'destination_currency': (str,),  # noqa: E501
            'reason': (str,),  # noqa: E501
            'reason_detail': (dict,),  # noqa: E501
            'source_amount': (float,),  # noqa: E501
            'amount': (float,),  # noqa: E501
            'destination_amount': (float,),  # noqa: E501
            'exchange_rate': (float,),  # noqa: E501
            'tax': (float,),  # noqa: E501
            'source_fee': (float,),  # noqa: E501
            'destination_fee': (float,),  # noqa: E501
            'transaction_fee': (float,),  # noqa: E501
            'sender_charge_back': (float,),  # noqa: E501
            'recipient_charge_back': (float,),  # noqa: E501
            'is_executable': (bool,),  # noqa: E501
            'valid_time_in_minutes': (float,),  # noqa: E501
            'tenant_fee': (float,),  # noqa: E501
            'id': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'source_currency': 'sourceCurrency',  # noqa: E501
        'destination_currency': 'destinationCurrency',  # noqa: E501
        'reason': 'reason',  # noqa: E501
        'reason_detail': 'reasonDetail',  # noqa: E501
        'source_amount': 'sourceAmount',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'destination_amount': 'destinationAmount',  # noqa: E501
        'exchange_rate': 'exchangeRate',  # noqa: E501
        'tax': 'tax',  # noqa: E501
        'source_fee': 'sourceFee',  # noqa: E501
        'destination_fee': 'destinationFee',  # noqa: E501
        'transaction_fee': 'transactionFee',  # noqa: E501
        'sender_charge_back': 'senderChargeBack',  # noqa: E501
        'recipient_charge_back': 'recipientChargeBack',  # noqa: E501
        'is_executable': 'isExecutable',  # noqa: E501
        'valid_time_in_minutes': 'validTimeInMinutes',  # noqa: E501
        'tenant_fee': 'tenantFee',  # noqa: E501
        'id': 'id',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, source_currency, destination_currency, reason, reason_detail, source_amount, amount, destination_amount, exchange_rate, tax, source_fee, destination_fee, transaction_fee, sender_charge_back, recipient_charge_back, is_executable, valid_time_in_minutes, tenant_fee, *args, **kwargs):  # noqa: E501
        """RaasQuoteTransactionResponse - a model defined in OpenAPI

        Args:
            source_currency (str):
            destination_currency (str):
            reason (str):
            reason_detail (dict):
            source_amount (float):
            amount (float):
            destination_amount (float):
            exchange_rate (float):
            tax (float):
            source_fee (float):
            destination_fee (float):
            transaction_fee (float):
            sender_charge_back (float):
            recipient_charge_back (float):
            is_executable (bool):
            valid_time_in_minutes (float):
            tenant_fee (float):

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

        self.source_currency = source_currency
        self.destination_currency = destination_currency
        self.reason = reason
        self.reason_detail = reason_detail
        self.source_amount = source_amount
        self.amount = amount
        self.destination_amount = destination_amount
        self.exchange_rate = exchange_rate
        self.tax = tax
        self.source_fee = source_fee
        self.destination_fee = destination_fee
        self.transaction_fee = transaction_fee
        self.sender_charge_back = sender_charge_back
        self.recipient_charge_back = recipient_charge_back
        self.is_executable = is_executable
        self.valid_time_in_minutes = valid_time_in_minutes
        self.tenant_fee = tenant_fee
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
    def __init__(self, source_currency, destination_currency, reason, reason_detail, source_amount, amount, destination_amount, exchange_rate, tax, source_fee, destination_fee, transaction_fee, sender_charge_back, recipient_charge_back, is_executable, valid_time_in_minutes, tenant_fee, *args, **kwargs):  # noqa: E501
        """RaasQuoteTransactionResponse - a model defined in OpenAPI

        Args:
            source_currency (str):
            destination_currency (str):
            reason (str):
            reason_detail (dict):
            source_amount (float):
            amount (float):
            destination_amount (float):
            exchange_rate (float):
            tax (float):
            source_fee (float):
            destination_fee (float):
            transaction_fee (float):
            sender_charge_back (float):
            recipient_charge_back (float):
            is_executable (bool):
            valid_time_in_minutes (float):
            tenant_fee (float):

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

        self.source_currency = source_currency
        self.destination_currency = destination_currency
        self.reason = reason
        self.reason_detail = reason_detail
        self.source_amount = source_amount
        self.amount = amount
        self.destination_amount = destination_amount
        self.exchange_rate = exchange_rate
        self.tax = tax
        self.source_fee = source_fee
        self.destination_fee = destination_fee
        self.transaction_fee = transaction_fee
        self.sender_charge_back = sender_charge_back
        self.recipient_charge_back = recipient_charge_back
        self.is_executable = is_executable
        self.valid_time_in_minutes = valid_time_in_minutes
        self.tenant_fee = tenant_fee
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
