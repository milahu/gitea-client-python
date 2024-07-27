# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: {{AppVer | JSEscape}}
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

from gitea_client.configuration import Configuration


class IssueMeta(object):
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
        'index': 'int',
        'owner': 'str',
        'repo': 'str'
    }

    attribute_map = {
        'index': 'index',
        'owner': 'owner',
        'repo': 'repo'
    }

    def __init__(self, index=None, owner=None, repo=None, _configuration=None):  # noqa: E501
        """IssueMeta - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._index = None
        self._owner = None
        self._repo = None
        self.discriminator = None

        if index is not None:
            self.index = index
        if owner is not None:
            self.owner = owner
        if repo is not None:
            self.repo = repo

    @property
    def index(self):
        """Gets the index of this IssueMeta.  # noqa: E501


        :return: The index of this IssueMeta.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this IssueMeta.


        :param index: The index of this IssueMeta.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def owner(self):
        """Gets the owner of this IssueMeta.  # noqa: E501


        :return: The owner of this IssueMeta.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this IssueMeta.


        :param owner: The owner of this IssueMeta.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def repo(self):
        """Gets the repo of this IssueMeta.  # noqa: E501


        :return: The repo of this IssueMeta.  # noqa: E501
        :rtype: str
        """
        return self._repo

    @repo.setter
    def repo(self, repo):
        """Sets the repo of this IssueMeta.


        :param repo: The repo of this IssueMeta.  # noqa: E501
        :type: str
        """

        self._repo = repo

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
        if issubclass(IssueMeta, dict):
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
        if not isinstance(other, IssueMeta):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IssueMeta):
            return True

        return self.to_dict() != other.to_dict()
