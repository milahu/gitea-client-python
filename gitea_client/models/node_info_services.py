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


class NodeInfoServices(object):
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
        'inbound': 'list[str]',
        'outbound': 'list[str]'
    }

    attribute_map = {
        'inbound': 'inbound',
        'outbound': 'outbound'
    }

    def __init__(self, inbound=None, outbound=None, _configuration=None):  # noqa: E501
        """NodeInfoServices - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._inbound = None
        self._outbound = None
        self.discriminator = None

        if inbound is not None:
            self.inbound = inbound
        if outbound is not None:
            self.outbound = outbound

    @property
    def inbound(self):
        """Gets the inbound of this NodeInfoServices.  # noqa: E501


        :return: The inbound of this NodeInfoServices.  # noqa: E501
        :rtype: list[str]
        """
        return self._inbound

    @inbound.setter
    def inbound(self, inbound):
        """Sets the inbound of this NodeInfoServices.


        :param inbound: The inbound of this NodeInfoServices.  # noqa: E501
        :type: list[str]
        """

        self._inbound = inbound

    @property
    def outbound(self):
        """Gets the outbound of this NodeInfoServices.  # noqa: E501


        :return: The outbound of this NodeInfoServices.  # noqa: E501
        :rtype: list[str]
        """
        return self._outbound

    @outbound.setter
    def outbound(self, outbound):
        """Sets the outbound of this NodeInfoServices.


        :param outbound: The outbound of this NodeInfoServices.  # noqa: E501
        :type: list[str]
        """

        self._outbound = outbound

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
        if issubclass(NodeInfoServices, dict):
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
        if not isinstance(other, NodeInfoServices):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NodeInfoServices):
            return True

        return self.to_dict() != other.to_dict()
