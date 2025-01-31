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


class LicenseTemplateInfo(object):
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
        'body': 'str',
        'implementation': 'str',
        'key': 'str',
        'name': 'str',
        'url': 'str'
    }

    attribute_map = {
        'body': 'body',
        'implementation': 'implementation',
        'key': 'key',
        'name': 'name',
        'url': 'url'
    }

    def __init__(self, body=None, implementation=None, key=None, name=None, url=None, _configuration=None):  # noqa: E501
        """LicenseTemplateInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._body = None
        self._implementation = None
        self._key = None
        self._name = None
        self._url = None
        self.discriminator = None

        if body is not None:
            self.body = body
        if implementation is not None:
            self.implementation = implementation
        if key is not None:
            self.key = key
        if name is not None:
            self.name = name
        if url is not None:
            self.url = url

    @property
    def body(self):
        """Gets the body of this LicenseTemplateInfo.  # noqa: E501


        :return: The body of this LicenseTemplateInfo.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this LicenseTemplateInfo.


        :param body: The body of this LicenseTemplateInfo.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def implementation(self):
        """Gets the implementation of this LicenseTemplateInfo.  # noqa: E501


        :return: The implementation of this LicenseTemplateInfo.  # noqa: E501
        :rtype: str
        """
        return self._implementation

    @implementation.setter
    def implementation(self, implementation):
        """Sets the implementation of this LicenseTemplateInfo.


        :param implementation: The implementation of this LicenseTemplateInfo.  # noqa: E501
        :type: str
        """

        self._implementation = implementation

    @property
    def key(self):
        """Gets the key of this LicenseTemplateInfo.  # noqa: E501


        :return: The key of this LicenseTemplateInfo.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this LicenseTemplateInfo.


        :param key: The key of this LicenseTemplateInfo.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this LicenseTemplateInfo.  # noqa: E501


        :return: The name of this LicenseTemplateInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LicenseTemplateInfo.


        :param name: The name of this LicenseTemplateInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def url(self):
        """Gets the url of this LicenseTemplateInfo.  # noqa: E501


        :return: The url of this LicenseTemplateInfo.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this LicenseTemplateInfo.


        :param url: The url of this LicenseTemplateInfo.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(LicenseTemplateInfo, dict):
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
        if not isinstance(other, LicenseTemplateInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LicenseTemplateInfo):
            return True

        return self.to_dict() != other.to_dict()
