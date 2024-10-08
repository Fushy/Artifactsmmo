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

class EquipSchema(object):
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
        'slot': 'object',
        'quantity': 'object'
    }

    attribute_map = {
        'code': 'code',
        'slot': 'slot',
        'quantity': 'quantity'
    }

    def __init__(self, code=None, slot=None, quantity=None):  # noqa: E501
        """EquipSchema - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._slot = None
        self._quantity = None
        self.discriminator = None
        self.code = code
        self.slot = slot
        if quantity is not None:
            self.quantity = quantity

    @property
    def code(self):
        """Gets the code of this EquipSchema.  # noqa: E501

        Item code.  # noqa: E501

        :return: The code of this EquipSchema.  # noqa: E501
        :rtype: object
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this EquipSchema.

        Item code.  # noqa: E501

        :param code: The code of this EquipSchema.  # noqa: E501
        :type: object
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def slot(self):
        """Gets the slot of this EquipSchema.  # noqa: E501

        Item slot.  # noqa: E501

        :return: The slot of this EquipSchema.  # noqa: E501
        :rtype: object
        """
        return self._slot

    @slot.setter
    def slot(self, slot):
        """Sets the slot of this EquipSchema.

        Item slot.  # noqa: E501

        :param slot: The slot of this EquipSchema.  # noqa: E501
        :type: object
        """
        if slot is None:
            raise ValueError("Invalid value for `slot`, must not be `None`")  # noqa: E501

        self._slot = slot

    @property
    def quantity(self):
        """Gets the quantity of this EquipSchema.  # noqa: E501

        Item quantity. Applicable to consumables only.  # noqa: E501

        :return: The quantity of this EquipSchema.  # noqa: E501
        :rtype: object
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this EquipSchema.

        Item quantity. Applicable to consumables only.  # noqa: E501

        :param quantity: The quantity of this EquipSchema.  # noqa: E501
        :type: object
        """

        self._quantity = quantity

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
        if issubclass(EquipSchema, dict):
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
        if not isinstance(other, EquipSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
