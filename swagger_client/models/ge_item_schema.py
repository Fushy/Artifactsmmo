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

class GEItemSchema(object):
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
        'stock': 'object',
        'sell_price': 'object',
        'buy_price': 'object',
        'max_quantity': 'object'
    }

    attribute_map = {
        'code': 'code',
        'stock': 'stock',
        'sell_price': 'sell_price',
        'buy_price': 'buy_price',
        'max_quantity': 'max_quantity'
    }

    def __init__(self, code=None, stock=None, sell_price=None, buy_price=None, max_quantity=None):  # noqa: E501
        """GEItemSchema - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._stock = None
        self._sell_price = None
        self._buy_price = None
        self._max_quantity = None
        self.discriminator = None
        self.code = code
        self.stock = stock
        if sell_price is not None:
            self.sell_price = sell_price
        if buy_price is not None:
            self.buy_price = buy_price
        self.max_quantity = max_quantity

    @property
    def code(self):
        """Gets the code of this GEItemSchema.  # noqa: E501

        Item code.  # noqa: E501

        :return: The code of this GEItemSchema.  # noqa: E501
        :rtype: object
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this GEItemSchema.

        Item code.  # noqa: E501

        :param code: The code of this GEItemSchema.  # noqa: E501
        :type: object
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def stock(self):
        """Gets the stock of this GEItemSchema.  # noqa: E501

        Item stock.  # noqa: E501

        :return: The stock of this GEItemSchema.  # noqa: E501
        :rtype: object
        """
        return self._stock

    @stock.setter
    def stock(self, stock):
        """Sets the stock of this GEItemSchema.

        Item stock.  # noqa: E501

        :param stock: The stock of this GEItemSchema.  # noqa: E501
        :type: object
        """
        if stock is None:
            raise ValueError("Invalid value for `stock`, must not be `None`")  # noqa: E501

        self._stock = stock

    @property
    def sell_price(self):
        """Gets the sell_price of this GEItemSchema.  # noqa: E501

        The item's selling price.  # noqa: E501

        :return: The sell_price of this GEItemSchema.  # noqa: E501
        :rtype: object
        """
        return self._sell_price

    @sell_price.setter
    def sell_price(self, sell_price):
        """Sets the sell_price of this GEItemSchema.

        The item's selling price.  # noqa: E501

        :param sell_price: The sell_price of this GEItemSchema.  # noqa: E501
        :type: object
        """

        self._sell_price = sell_price

    @property
    def buy_price(self):
        """Gets the buy_price of this GEItemSchema.  # noqa: E501

        The item's buying price.  # noqa: E501

        :return: The buy_price of this GEItemSchema.  # noqa: E501
        :rtype: object
        """
        return self._buy_price

    @buy_price.setter
    def buy_price(self, buy_price):
        """Sets the buy_price of this GEItemSchema.

        The item's buying price.  # noqa: E501

        :param buy_price: The buy_price of this GEItemSchema.  # noqa: E501
        :type: object
        """

        self._buy_price = buy_price

    @property
    def max_quantity(self):
        """Gets the max_quantity of this GEItemSchema.  # noqa: E501

        The number of items you can buy or sell at the same time.  # noqa: E501

        :return: The max_quantity of this GEItemSchema.  # noqa: E501
        :rtype: object
        """
        return self._max_quantity

    @max_quantity.setter
    def max_quantity(self, max_quantity):
        """Sets the max_quantity of this GEItemSchema.

        The number of items you can buy or sell at the same time.  # noqa: E501

        :param max_quantity: The max_quantity of this GEItemSchema.  # noqa: E501
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
        if issubclass(GEItemSchema, dict):
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
        if not isinstance(other, GEItemSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
