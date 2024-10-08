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

class LogSchema(object):
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
        'character': 'object',
        'account': 'object',
        'type': 'object',
        'description': 'object',
        'content': 'object',
        'cooldown': 'object',
        'cooldown_expiration': 'object',
        'created_at': 'object'
    }

    attribute_map = {
        'character': 'character',
        'account': 'account',
        'type': 'type',
        'description': 'description',
        'content': 'content',
        'cooldown': 'cooldown',
        'cooldown_expiration': 'cooldown_expiration',
        'created_at': 'created_at'
    }

    def __init__(self, character=None, account=None, type=None, description=None, content=None, cooldown=None, cooldown_expiration=None, created_at=None):  # noqa: E501
        """LogSchema - a model defined in Swagger"""  # noqa: E501
        self._character = None
        self._account = None
        self._type = None
        self._description = None
        self._content = None
        self._cooldown = None
        self._cooldown_expiration = None
        self._created_at = None
        self.discriminator = None
        self.character = character
        self.account = account
        self.type = type
        self.description = description
        self.content = content
        self.cooldown = cooldown
        self.cooldown_expiration = cooldown_expiration
        self.created_at = created_at

    @property
    def character(self):
        """Gets the character of this LogSchema.  # noqa: E501

        Character name.  # noqa: E501

        :return: The character of this LogSchema.  # noqa: E501
        :rtype: object
        """
        return self._character

    @character.setter
    def character(self, character):
        """Sets the character of this LogSchema.

        Character name.  # noqa: E501

        :param character: The character of this LogSchema.  # noqa: E501
        :type: object
        """
        if character is None:
            raise ValueError("Invalid value for `character`, must not be `None`")  # noqa: E501

        self._character = character

    @property
    def account(self):
        """Gets the account of this LogSchema.  # noqa: E501

        Account character.  # noqa: E501

        :return: The account of this LogSchema.  # noqa: E501
        :rtype: object
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this LogSchema.

        Account character.  # noqa: E501

        :param account: The account of this LogSchema.  # noqa: E501
        :type: object
        """
        if account is None:
            raise ValueError("Invalid value for `account`, must not be `None`")  # noqa: E501

        self._account = account

    @property
    def type(self):
        """Gets the type of this LogSchema.  # noqa: E501

        Type of action.  # noqa: E501

        :return: The type of this LogSchema.  # noqa: E501
        :rtype: object
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LogSchema.

        Type of action.  # noqa: E501

        :param type: The type of this LogSchema.  # noqa: E501
        :type: object
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def description(self):
        """Gets the description of this LogSchema.  # noqa: E501

        Description of action.  # noqa: E501

        :return: The description of this LogSchema.  # noqa: E501
        :rtype: object
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LogSchema.

        Description of action.  # noqa: E501

        :param description: The description of this LogSchema.  # noqa: E501
        :type: object
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def content(self):
        """Gets the content of this LogSchema.  # noqa: E501

        Content of action.  # noqa: E501

        :return: The content of this LogSchema.  # noqa: E501
        :rtype: object
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this LogSchema.

        Content of action.  # noqa: E501

        :param content: The content of this LogSchema.  # noqa: E501
        :type: object
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def cooldown(self):
        """Gets the cooldown of this LogSchema.  # noqa: E501

        Cooldown in seconds.  # noqa: E501

        :return: The cooldown of this LogSchema.  # noqa: E501
        :rtype: object
        """
        return self._cooldown

    @cooldown.setter
    def cooldown(self, cooldown):
        """Sets the cooldown of this LogSchema.

        Cooldown in seconds.  # noqa: E501

        :param cooldown: The cooldown of this LogSchema.  # noqa: E501
        :type: object
        """
        if cooldown is None:
            raise ValueError("Invalid value for `cooldown`, must not be `None`")  # noqa: E501

        self._cooldown = cooldown

    @property
    def cooldown_expiration(self):
        """Gets the cooldown_expiration of this LogSchema.  # noqa: E501

        Datetime of cooldown expiration.  # noqa: E501

        :return: The cooldown_expiration of this LogSchema.  # noqa: E501
        :rtype: object
        """
        return self._cooldown_expiration

    @cooldown_expiration.setter
    def cooldown_expiration(self, cooldown_expiration):
        """Sets the cooldown_expiration of this LogSchema.

        Datetime of cooldown expiration.  # noqa: E501

        :param cooldown_expiration: The cooldown_expiration of this LogSchema.  # noqa: E501
        :type: object
        """
        if cooldown_expiration is None:
            raise ValueError("Invalid value for `cooldown_expiration`, must not be `None`")  # noqa: E501

        self._cooldown_expiration = cooldown_expiration

    @property
    def created_at(self):
        """Gets the created_at of this LogSchema.  # noqa: E501

        Datetime of creation.  # noqa: E501

        :return: The created_at of this LogSchema.  # noqa: E501
        :rtype: object
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this LogSchema.

        Datetime of creation.  # noqa: E501

        :param created_at: The created_at of this LogSchema.  # noqa: E501
        :type: object
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

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
        if issubclass(LogSchema, dict):
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
        if not isinstance(other, LogSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
