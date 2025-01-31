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


class UserSettings(object):
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
        'description': 'str',
        'diff_view_style': 'str',
        'full_name': 'str',
        'hide_activity': 'bool',
        'hide_email': 'bool',
        'language': 'str',
        'location': 'str',
        'theme': 'str',
        'website': 'str'
    }

    attribute_map = {
        'description': 'description',
        'diff_view_style': 'diff_view_style',
        'full_name': 'full_name',
        'hide_activity': 'hide_activity',
        'hide_email': 'hide_email',
        'language': 'language',
        'location': 'location',
        'theme': 'theme',
        'website': 'website'
    }

    def __init__(self, description=None, diff_view_style=None, full_name=None, hide_activity=None, hide_email=None, language=None, location=None, theme=None, website=None, _configuration=None):  # noqa: E501
        """UserSettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._diff_view_style = None
        self._full_name = None
        self._hide_activity = None
        self._hide_email = None
        self._language = None
        self._location = None
        self._theme = None
        self._website = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if diff_view_style is not None:
            self.diff_view_style = diff_view_style
        if full_name is not None:
            self.full_name = full_name
        if hide_activity is not None:
            self.hide_activity = hide_activity
        if hide_email is not None:
            self.hide_email = hide_email
        if language is not None:
            self.language = language
        if location is not None:
            self.location = location
        if theme is not None:
            self.theme = theme
        if website is not None:
            self.website = website

    @property
    def description(self):
        """Gets the description of this UserSettings.  # noqa: E501


        :return: The description of this UserSettings.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UserSettings.


        :param description: The description of this UserSettings.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def diff_view_style(self):
        """Gets the diff_view_style of this UserSettings.  # noqa: E501


        :return: The diff_view_style of this UserSettings.  # noqa: E501
        :rtype: str
        """
        return self._diff_view_style

    @diff_view_style.setter
    def diff_view_style(self, diff_view_style):
        """Sets the diff_view_style of this UserSettings.


        :param diff_view_style: The diff_view_style of this UserSettings.  # noqa: E501
        :type: str
        """

        self._diff_view_style = diff_view_style

    @property
    def full_name(self):
        """Gets the full_name of this UserSettings.  # noqa: E501


        :return: The full_name of this UserSettings.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this UserSettings.


        :param full_name: The full_name of this UserSettings.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def hide_activity(self):
        """Gets the hide_activity of this UserSettings.  # noqa: E501


        :return: The hide_activity of this UserSettings.  # noqa: E501
        :rtype: bool
        """
        return self._hide_activity

    @hide_activity.setter
    def hide_activity(self, hide_activity):
        """Sets the hide_activity of this UserSettings.


        :param hide_activity: The hide_activity of this UserSettings.  # noqa: E501
        :type: bool
        """

        self._hide_activity = hide_activity

    @property
    def hide_email(self):
        """Gets the hide_email of this UserSettings.  # noqa: E501

        Privacy  # noqa: E501

        :return: The hide_email of this UserSettings.  # noqa: E501
        :rtype: bool
        """
        return self._hide_email

    @hide_email.setter
    def hide_email(self, hide_email):
        """Sets the hide_email of this UserSettings.

        Privacy  # noqa: E501

        :param hide_email: The hide_email of this UserSettings.  # noqa: E501
        :type: bool
        """

        self._hide_email = hide_email

    @property
    def language(self):
        """Gets the language of this UserSettings.  # noqa: E501


        :return: The language of this UserSettings.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this UserSettings.


        :param language: The language of this UserSettings.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def location(self):
        """Gets the location of this UserSettings.  # noqa: E501


        :return: The location of this UserSettings.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this UserSettings.


        :param location: The location of this UserSettings.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def theme(self):
        """Gets the theme of this UserSettings.  # noqa: E501


        :return: The theme of this UserSettings.  # noqa: E501
        :rtype: str
        """
        return self._theme

    @theme.setter
    def theme(self, theme):
        """Sets the theme of this UserSettings.


        :param theme: The theme of this UserSettings.  # noqa: E501
        :type: str
        """

        self._theme = theme

    @property
    def website(self):
        """Gets the website of this UserSettings.  # noqa: E501


        :return: The website of this UserSettings.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this UserSettings.


        :param website: The website of this UserSettings.  # noqa: E501
        :type: str
        """

        self._website = website

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
        if issubclass(UserSettings, dict):
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
        if not isinstance(other, UserSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserSettings):
            return True

        return self.to_dict() != other.to_dict()
