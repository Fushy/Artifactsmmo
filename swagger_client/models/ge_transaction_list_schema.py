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

class GETransactionListSchema(object):
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
        'cooldown': 'object',
        'transaction': 'object',
        'character': 'object'
    }

    attribute_map = {
        'cooldown': 'cooldown',
        'transaction': 'transaction',
        'character': 'character'
    }

    def __init__(self, cooldown=None, transaction=None, character=None):  # noqa: E501
        """GETransactionListSchema - a model defined in Swagger"""  # noqa: E501
        self._cooldown = None
        self._transaction = None
        self._character = None
        self.discriminator = None
        self.cooldown = cooldown
        self.transaction = transaction
        self.character = character

    @property
    def cooldown(self):
        """Gets the cooldown of this GETransactionListSchema.  # noqa: E501

        Cooldown details.  # noqa: E501

        :return: The cooldown of this GETransactionListSchema.  # noqa: E501
        :rtype: object
        """
        return self._cooldown

    @cooldown.setter
    def cooldown(self, cooldown):
        """Sets the cooldown of this GETransactionListSchema.

        Cooldown details.  # noqa: E501

        :param cooldown: The cooldown of this GETransactionListSchema.  # noqa: E501
        :type: object
        """
        if cooldown is None:
            raise ValueError("Invalid value for `cooldown`, must not be `None`")  # noqa: E501

        self._cooldown = cooldown

    @property
    def transaction(self):
        """Gets the transaction of this GETransactionListSchema.  # noqa: E501

        Transaction details.  # noqa: E501

        :return: The transaction of this GETransactionListSchema.  # noqa: E501
        :rtype: object
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this GETransactionListSchema.

        Transaction details.  # noqa: E501

        :param transaction: The transaction of this GETransactionListSchema.  # noqa: E501
        :type: object
        """
        if transaction is None:
            raise ValueError("Invalid value for `transaction`, must not be `None`")  # noqa: E501

        self._transaction = transaction

    @property
    def character(self):
        """Gets the character of this GETransactionListSchema.  # noqa: E501

        Character details.  # noqa: E501

        :return: The character of this GETransactionListSchema.  # noqa: E501
        :rtype: object
        """
        return self._character

    @character.setter
    def character(self, character):
        """Sets the character of this GETransactionListSchema.

        Character details.  # noqa: E501

        :param character: The character of this GETransactionListSchema.  # noqa: E501
        :type: object
        """
        if character is None:
            raise ValueError("Invalid value for `character`, must not be `None`")  # noqa: E501

        self._character = character

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
        if issubclass(GETransactionListSchema, dict):
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
        if not isinstance(other, GETransactionListSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
