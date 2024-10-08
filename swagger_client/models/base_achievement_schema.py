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

class BaseAchievementSchema(object):
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
        'name': 'object',
        'code': 'object',
        'description': 'object',
        'points': 'object',
        'type': 'object',
        'target': 'object',
        'total': 'object'
    }

    attribute_map = {
        'name': 'name',
        'code': 'code',
        'description': 'description',
        'points': 'points',
        'type': 'type',
        'target': 'target',
        'total': 'total'
    }

    def __init__(self, name=None, code=None, description=None, points=None, type=None, target=None, total=None):  # noqa: E501
        """BaseAchievementSchema - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._code = None
        self._description = None
        self._points = None
        self._type = None
        self._target = None
        self._total = None
        self.discriminator = None
        self.name = name
        self.code = code
        self.description = description
        self.points = points
        self.type = type
        self.target = target
        self.total = total

    @property
    def name(self):
        """Gets the name of this BaseAchievementSchema.  # noqa: E501

        Name of the achievement.  # noqa: E501

        :return: The name of this BaseAchievementSchema.  # noqa: E501
        :rtype: object
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BaseAchievementSchema.

        Name of the achievement.  # noqa: E501

        :param name: The name of this BaseAchievementSchema.  # noqa: E501
        :type: object
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def code(self):
        """Gets the code of this BaseAchievementSchema.  # noqa: E501

        Code of the achievement.   # noqa: E501

        :return: The code of this BaseAchievementSchema.  # noqa: E501
        :rtype: object
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this BaseAchievementSchema.

        Code of the achievement.   # noqa: E501

        :param code: The code of this BaseAchievementSchema.  # noqa: E501
        :type: object
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def description(self):
        """Gets the description of this BaseAchievementSchema.  # noqa: E501

        Description of the achievement.  # noqa: E501

        :return: The description of this BaseAchievementSchema.  # noqa: E501
        :rtype: object
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BaseAchievementSchema.

        Description of the achievement.  # noqa: E501

        :param description: The description of this BaseAchievementSchema.  # noqa: E501
        :type: object
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def points(self):
        """Gets the points of this BaseAchievementSchema.  # noqa: E501

        Points of the achievement. Used for the leaderboard.  # noqa: E501

        :return: The points of this BaseAchievementSchema.  # noqa: E501
        :rtype: object
        """
        return self._points

    @points.setter
    def points(self, points):
        """Sets the points of this BaseAchievementSchema.

        Points of the achievement. Used for the leaderboard.  # noqa: E501

        :param points: The points of this BaseAchievementSchema.  # noqa: E501
        :type: object
        """
        if points is None:
            raise ValueError("Invalid value for `points`, must not be `None`")  # noqa: E501

        self._points = points

    @property
    def type(self):
        """Gets the type of this BaseAchievementSchema.  # noqa: E501

        Type of achievement.  # noqa: E501

        :return: The type of this BaseAchievementSchema.  # noqa: E501
        :rtype: object
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BaseAchievementSchema.

        Type of achievement.  # noqa: E501

        :param type: The type of this BaseAchievementSchema.  # noqa: E501
        :type: object
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def target(self):
        """Gets the target of this BaseAchievementSchema.  # noqa: E501

        Target of the achievement.  # noqa: E501

        :return: The target of this BaseAchievementSchema.  # noqa: E501
        :rtype: object
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this BaseAchievementSchema.

        Target of the achievement.  # noqa: E501

        :param target: The target of this BaseAchievementSchema.  # noqa: E501
        :type: object
        """
        if target is None:
            raise ValueError("Invalid value for `target`, must not be `None`")  # noqa: E501

        self._target = target

    @property
    def total(self):
        """Gets the total of this BaseAchievementSchema.  # noqa: E501

        Total to do.  # noqa: E501

        :return: The total of this BaseAchievementSchema.  # noqa: E501
        :rtype: object
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this BaseAchievementSchema.

        Total to do.  # noqa: E501

        :param total: The total of this BaseAchievementSchema.  # noqa: E501
        :type: object
        """
        if total is None:
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

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
        if issubclass(BaseAchievementSchema, dict):
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
        if not isinstance(other, BaseAchievementSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
