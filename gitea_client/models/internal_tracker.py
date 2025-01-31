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


class InternalTracker(object):
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
        'allow_only_contributors_to_track_time': 'bool',
        'enable_issue_dependencies': 'bool',
        'enable_time_tracker': 'bool'
    }

    attribute_map = {
        'allow_only_contributors_to_track_time': 'allow_only_contributors_to_track_time',
        'enable_issue_dependencies': 'enable_issue_dependencies',
        'enable_time_tracker': 'enable_time_tracker'
    }

    def __init__(self, allow_only_contributors_to_track_time=None, enable_issue_dependencies=None, enable_time_tracker=None, _configuration=None):  # noqa: E501
        """InternalTracker - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allow_only_contributors_to_track_time = None
        self._enable_issue_dependencies = None
        self._enable_time_tracker = None
        self.discriminator = None

        if allow_only_contributors_to_track_time is not None:
            self.allow_only_contributors_to_track_time = allow_only_contributors_to_track_time
        if enable_issue_dependencies is not None:
            self.enable_issue_dependencies = enable_issue_dependencies
        if enable_time_tracker is not None:
            self.enable_time_tracker = enable_time_tracker

    @property
    def allow_only_contributors_to_track_time(self):
        """Gets the allow_only_contributors_to_track_time of this InternalTracker.  # noqa: E501

        Let only contributors track time (Built-in issue tracker)  # noqa: E501

        :return: The allow_only_contributors_to_track_time of this InternalTracker.  # noqa: E501
        :rtype: bool
        """
        return self._allow_only_contributors_to_track_time

    @allow_only_contributors_to_track_time.setter
    def allow_only_contributors_to_track_time(self, allow_only_contributors_to_track_time):
        """Sets the allow_only_contributors_to_track_time of this InternalTracker.

        Let only contributors track time (Built-in issue tracker)  # noqa: E501

        :param allow_only_contributors_to_track_time: The allow_only_contributors_to_track_time of this InternalTracker.  # noqa: E501
        :type: bool
        """

        self._allow_only_contributors_to_track_time = allow_only_contributors_to_track_time

    @property
    def enable_issue_dependencies(self):
        """Gets the enable_issue_dependencies of this InternalTracker.  # noqa: E501

        Enable dependencies for issues and pull requests (Built-in issue tracker)  # noqa: E501

        :return: The enable_issue_dependencies of this InternalTracker.  # noqa: E501
        :rtype: bool
        """
        return self._enable_issue_dependencies

    @enable_issue_dependencies.setter
    def enable_issue_dependencies(self, enable_issue_dependencies):
        """Sets the enable_issue_dependencies of this InternalTracker.

        Enable dependencies for issues and pull requests (Built-in issue tracker)  # noqa: E501

        :param enable_issue_dependencies: The enable_issue_dependencies of this InternalTracker.  # noqa: E501
        :type: bool
        """

        self._enable_issue_dependencies = enable_issue_dependencies

    @property
    def enable_time_tracker(self):
        """Gets the enable_time_tracker of this InternalTracker.  # noqa: E501

        Enable time tracking (Built-in issue tracker)  # noqa: E501

        :return: The enable_time_tracker of this InternalTracker.  # noqa: E501
        :rtype: bool
        """
        return self._enable_time_tracker

    @enable_time_tracker.setter
    def enable_time_tracker(self, enable_time_tracker):
        """Sets the enable_time_tracker of this InternalTracker.

        Enable time tracking (Built-in issue tracker)  # noqa: E501

        :param enable_time_tracker: The enable_time_tracker of this InternalTracker.  # noqa: E501
        :type: bool
        """

        self._enable_time_tracker = enable_time_tracker

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
        if issubclass(InternalTracker, dict):
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
        if not isinstance(other, InternalTracker):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InternalTracker):
            return True

        return self.to_dict() != other.to_dict()
