# coding: utf-8

"""
    Artifacts API

     Artifacts is an API-based MMO game where you can manage 5 characters to explore, fight, gather resources, craft items and much more.  Website: https://artifactsmmo.com/  Documentation: https://docs.artifactsmmo.com/  OpenAPI Spec: https://api.artifactsmmo.com/openapi.json   # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DropRateSchema(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code': 'object',
        'rate': 'object',
        'min_quantity': 'object',
        'max_quantity': 'object'
    }

    attribute_map = {
        'code': 'code',
        'rate': 'rate',
        'min_quantity': 'min_quantity',
        'max_quantity': 'max_quantity'
    }

    def __init__(self, code=None, rate=None, min_quantity=None, max_quantity=None):  # noqa: E501
        """DropRateSchema - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._rate = None
        self._min_quantity = None
        self._max_quantity = None
        self.discriminator = None
        self.code = code
        self.rate = rate
        self.min_quantity = min_quantity
        self.max_quantity = max_quantity

    @property
    def code(self):
        """Gets the code of this DropRateSchema.  # noqa: E501

        Item code.  # noqa: E501

        :return: The code of this DropRateSchema.  # noqa: E501
        :rtype: object
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this DropRateSchema.

        Item code.  # noqa: E501

        :param code: The code of this DropRateSchema.  # noqa: E501
        :type: object
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def rate(self):
        """Gets the rate of this DropRateSchema.  # noqa: E501

        Chance rate.  # noqa: E501

        :return: The rate of this DropRateSchema.  # noqa: E501
        :rtype: object
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this DropRateSchema.

        Chance rate.  # noqa: E501

        :param rate: The rate of this DropRateSchema.  # noqa: E501
        :type: object
        """
        if rate is None:
            raise ValueError("Invalid value for `rate`, must not be `None`")  # noqa: E501

        self._rate = rate

    @property
    def min_quantity(self):
        """Gets the min_quantity of this DropRateSchema.  # noqa: E501

        Minimum quantity.  # noqa: E501

        :return: The min_quantity of this DropRateSchema.  # noqa: E501
        :rtype: object
        """
        return self._min_quantity

    @min_quantity.setter
    def min_quantity(self, min_quantity):
        """Sets the min_quantity of this DropRateSchema.

        Minimum quantity.  # noqa: E501

        :param min_quantity: The min_quantity of this DropRateSchema.  # noqa: E501
        :type: object
        """
        if min_quantity is None:
            raise ValueError("Invalid value for `min_quantity`, must not be `None`")  # noqa: E501

        self._min_quantity = min_quantity

    @property
    def max_quantity(self):
        """Gets the max_quantity of this DropRateSchema.  # noqa: E501

        Maximum quantity.  # noqa: E501

        :return: The max_quantity of this DropRateSchema.  # noqa: E501
        :rtype: object
        """
        return self._max_quantity

    @max_quantity.setter
    def max_quantity(self, max_quantity):
        """Sets the max_quantity of this DropRateSchema.

        Maximum quantity.  # noqa: E501

        :param max_quantity: The max_quantity of this DropRateSchema.  # noqa: E501
        :type: object
        """
        if max_quantity is None:
            raise ValueError("Invalid value for `max_quantity`, must not be `None`")  # noqa: E501

        self._max_quantity = max_quantity

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DropRateSchema, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DropRateSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
