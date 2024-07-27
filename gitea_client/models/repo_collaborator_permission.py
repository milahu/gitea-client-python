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


class RepoCollaboratorPermission(object):
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
        'permission': 'str',
        'role_name': 'str',
        'user': 'User'
    }

    attribute_map = {
        'permission': 'permission',
        'role_name': 'role_name',
        'user': 'user'
    }

    def __init__(self, permission=None, role_name=None, user=None, _configuration=None):  # noqa: E501
        """RepoCollaboratorPermission - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._permission = None
        self._role_name = None
        self._user = None
        self.discriminator = None

        if permission is not None:
            self.permission = permission
        if role_name is not None:
            self.role_name = role_name
        if user is not None:
            self.user = user

    @property
    def permission(self):
        """Gets the permission of this RepoCollaboratorPermission.  # noqa: E501


        :return: The permission of this RepoCollaboratorPermission.  # noqa: E501
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this RepoCollaboratorPermission.


        :param permission: The permission of this RepoCollaboratorPermission.  # noqa: E501
        :type: str
        """

        self._permission = permission

    @property
    def role_name(self):
        """Gets the role_name of this RepoCollaboratorPermission.  # noqa: E501


        :return: The role_name of this RepoCollaboratorPermission.  # noqa: E501
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this RepoCollaboratorPermission.


        :param role_name: The role_name of this RepoCollaboratorPermission.  # noqa: E501
        :type: str
        """

        self._role_name = role_name

    @property
    def user(self):
        """Gets the user of this RepoCollaboratorPermission.  # noqa: E501


        :return: The user of this RepoCollaboratorPermission.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this RepoCollaboratorPermission.


        :param user: The user of this RepoCollaboratorPermission.  # noqa: E501
        :type: User
        """

        self._user = user

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
        if issubclass(RepoCollaboratorPermission, dict):
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
        if not isinstance(other, RepoCollaboratorPermission):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RepoCollaboratorPermission):
            return True

        return self.to_dict() != other.to_dict()
