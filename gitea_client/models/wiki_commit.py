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


class WikiCommit(object):
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
        'author': 'CommitUser',
        'commiter': 'CommitUser',
        'message': 'str',
        'sha': 'str'
    }

    attribute_map = {
        'author': 'author',
        'commiter': 'commiter',
        'message': 'message',
        'sha': 'sha'
    }

    def __init__(self, author=None, commiter=None, message=None, sha=None, _configuration=None):  # noqa: E501
        """WikiCommit - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._author = None
        self._commiter = None
        self._message = None
        self._sha = None
        self.discriminator = None

        if author is not None:
            self.author = author
        if commiter is not None:
            self.commiter = commiter
        if message is not None:
            self.message = message
        if sha is not None:
            self.sha = sha

    @property
    def author(self):
        """Gets the author of this WikiCommit.  # noqa: E501


        :return: The author of this WikiCommit.  # noqa: E501
        :rtype: CommitUser
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this WikiCommit.


        :param author: The author of this WikiCommit.  # noqa: E501
        :type: CommitUser
        """

        self._author = author

    @property
    def commiter(self):
        """Gets the commiter of this WikiCommit.  # noqa: E501


        :return: The commiter of this WikiCommit.  # noqa: E501
        :rtype: CommitUser
        """
        return self._commiter

    @commiter.setter
    def commiter(self, commiter):
        """Sets the commiter of this WikiCommit.


        :param commiter: The commiter of this WikiCommit.  # noqa: E501
        :type: CommitUser
        """

        self._commiter = commiter

    @property
    def message(self):
        """Gets the message of this WikiCommit.  # noqa: E501


        :return: The message of this WikiCommit.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this WikiCommit.


        :param message: The message of this WikiCommit.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def sha(self):
        """Gets the sha of this WikiCommit.  # noqa: E501


        :return: The sha of this WikiCommit.  # noqa: E501
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """Sets the sha of this WikiCommit.


        :param sha: The sha of this WikiCommit.  # noqa: E501
        :type: str
        """

        self._sha = sha

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
        if issubclass(WikiCommit, dict):
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
        if not isinstance(other, WikiCommit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WikiCommit):
            return True

        return self.to_dict() != other.to_dict()
