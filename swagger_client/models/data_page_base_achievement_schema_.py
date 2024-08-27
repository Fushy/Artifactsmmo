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

class DataPageBaseAchievementSchema_(object):
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
        'data': 'object',
        'total': 'object',
        'page': 'object',
        'size': 'object',
        'pages': 'object'
    }

    attribute_map = {
        'data': 'data',
        'total': 'total',
        'page': 'page',
        'size': 'size',
        'pages': 'pages'
    }

    def __init__(self, data=None, total=None, page=None, size=None, pages=None):  # noqa: E501
        """DataPageBaseAchievementSchema_ - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self._total = None
        self._page = None
        self._size = None
        self._pages = None
        self.discriminator = None
        self.data = data
        self.total = total
        self.page = page
        self.size = size
        if pages is not None:
            self.pages = pages

    @property
    def data(self):
        """Gets the data of this DataPageBaseAchievementSchema_.  # noqa: E501


        :return: The data of this DataPageBaseAchievementSchema_.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this DataPageBaseAchievementSchema_.


        :param data: The data of this DataPageBaseAchievementSchema_.  # noqa: E501
        :type: object
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def total(self):
        """Gets the total of this DataPageBaseAchievementSchema_.  # noqa: E501


        :return: The total of this DataPageBaseAchievementSchema_.  # noqa: E501
        :rtype: object
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this DataPageBaseAchievementSchema_.


        :param total: The total of this DataPageBaseAchievementSchema_.  # noqa: E501
        :type: object
        """
        if total is None:
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    @property
    def page(self):
        """Gets the page of this DataPageBaseAchievementSchema_.  # noqa: E501


        :return: The page of this DataPageBaseAchievementSchema_.  # noqa: E501
        :rtype: object
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this DataPageBaseAchievementSchema_.


        :param page: The page of this DataPageBaseAchievementSchema_.  # noqa: E501
        :type: object
        """
        if page is None:
            raise ValueError("Invalid value for `page`, must not be `None`")  # noqa: E501

        self._page = page

    @property
    def size(self):
        """Gets the size of this DataPageBaseAchievementSchema_.  # noqa: E501


        :return: The size of this DataPageBaseAchievementSchema_.  # noqa: E501
        :rtype: object
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this DataPageBaseAchievementSchema_.


        :param size: The size of this DataPageBaseAchievementSchema_.  # noqa: E501
        :type: object
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def pages(self):
        """Gets the pages of this DataPageBaseAchievementSchema_.  # noqa: E501


        :return: The pages of this DataPageBaseAchievementSchema_.  # noqa: E501
        :rtype: object
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this DataPageBaseAchievementSchema_.


        :param pages: The pages of this DataPageBaseAchievementSchema_.  # noqa: E501
        :type: object
        """

        self._pages = pages

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
        if issubclass(DataPageBaseAchievementSchema_, dict):
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
        if not isinstance(other, DataPageBaseAchievementSchema_):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
