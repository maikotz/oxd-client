# coding: utf-8

"""
    oxd-server

    oxd-server  # noqa: E501

    OpenAPI spec version: 4.2
    Contact: yuriyz@gluu.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class UmaRsModifyParams(object):
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
        'oxd_id': 'str',
        'path': 'str',
        'http_method': 'str',
        'scopes': 'list[str]',
        'scope_expression': 'str'
    }

    attribute_map = {
        'oxd_id': 'oxd_id',
        'path': 'path',
        'http_method': 'http_method',
        'scopes': 'scopes',
        'scope_expression': 'scope_expression'
    }

    def __init__(self, oxd_id=None, path=None, http_method=None, scopes=None, scope_expression=None):  # noqa: E501
        """UmaRsModifyParams - a model defined in Swagger"""  # noqa: E501
        self._oxd_id = None
        self._path = None
        self._http_method = None
        self._scopes = None
        self._scope_expression = None
        self.discriminator = None
        self.oxd_id = oxd_id
        self.path = path
        self.http_method = http_method
        if scopes is not None:
            self.scopes = scopes
        if scope_expression is not None:
            self.scope_expression = scope_expression

    @property
    def oxd_id(self):
        """Gets the oxd_id of this UmaRsModifyParams.  # noqa: E501


        :return: The oxd_id of this UmaRsModifyParams.  # noqa: E501
        :rtype: str
        """
        return self._oxd_id

    @oxd_id.setter
    def oxd_id(self, oxd_id):
        """Sets the oxd_id of this UmaRsModifyParams.


        :param oxd_id: The oxd_id of this UmaRsModifyParams.  # noqa: E501
        :type: str
        """
        if oxd_id is None:
            raise ValueError("Invalid value for `oxd_id`, must not be `None`")  # noqa: E501

        self._oxd_id = oxd_id

    @property
    def path(self):
        """Gets the path of this UmaRsModifyParams.  # noqa: E501


        :return: The path of this UmaRsModifyParams.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this UmaRsModifyParams.


        :param path: The path of this UmaRsModifyParams.  # noqa: E501
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def http_method(self):
        """Gets the http_method of this UmaRsModifyParams.  # noqa: E501


        :return: The http_method of this UmaRsModifyParams.  # noqa: E501
        :rtype: str
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        """Sets the http_method of this UmaRsModifyParams.


        :param http_method: The http_method of this UmaRsModifyParams.  # noqa: E501
        :type: str
        """
        if http_method is None:
            raise ValueError("Invalid value for `http_method`, must not be `None`")  # noqa: E501

        self._http_method = http_method

    @property
    def scopes(self):
        """Gets the scopes of this UmaRsModifyParams.  # noqa: E501


        :return: The scopes of this UmaRsModifyParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this UmaRsModifyParams.


        :param scopes: The scopes of this UmaRsModifyParams.  # noqa: E501
        :type: list[str]
        """

        self._scopes = scopes

    @property
    def scope_expression(self):
        """Gets the scope_expression of this UmaRsModifyParams.  # noqa: E501


        :return: The scope_expression of this UmaRsModifyParams.  # noqa: E501
        :rtype: str
        """
        return self._scope_expression

    @scope_expression.setter
    def scope_expression(self, scope_expression):
        """Sets the scope_expression of this UmaRsModifyParams.


        :param scope_expression: The scope_expression of this UmaRsModifyParams.  # noqa: E501
        :type: str
        """

        self._scope_expression = scope_expression

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
        if issubclass(UmaRsModifyParams, dict):
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
        if not isinstance(other, UmaRsModifyParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other