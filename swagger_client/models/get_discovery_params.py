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


class GetDiscoveryParams(object):
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
        'op_configuration_endpoint': 'str',
        'op_host': 'str',
        'op_discovery_path': 'str'
    }

    attribute_map = {
        'op_configuration_endpoint': 'op_configuration_endpoint',
        'op_host': 'op_host',
        'op_discovery_path': 'op_discovery_path'
    }

    def __init__(self, op_configuration_endpoint=None, op_host=None, op_discovery_path=None):  # noqa: E501
        """GetDiscoveryParams - a model defined in Swagger"""  # noqa: E501
        self._op_configuration_endpoint = None
        self._op_host = None
        self._op_discovery_path = None
        self.discriminator = None
        self.op_configuration_endpoint = op_configuration_endpoint
        if op_host is not None:
            self.op_host = op_host
        if op_discovery_path is not None:
            self.op_discovery_path = op_discovery_path

    @property
    def op_configuration_endpoint(self):
        """Gets the op_configuration_endpoint of this GetDiscoveryParams.  # noqa: E501

        The openid configuration endpoint URL. If missing, then `op_host` must be defined.  # noqa: E501

        :return: The op_configuration_endpoint of this GetDiscoveryParams.  # noqa: E501
        :rtype: str
        """
        return self._op_configuration_endpoint

    @op_configuration_endpoint.setter
    def op_configuration_endpoint(self, op_configuration_endpoint):
        """Sets the op_configuration_endpoint of this GetDiscoveryParams.

        The openid configuration endpoint URL. If missing, then `op_host` must be defined.  # noqa: E501

        :param op_configuration_endpoint: The op_configuration_endpoint of this GetDiscoveryParams.  # noqa: E501
        :type: str
        """
        if op_configuration_endpoint is None:
            raise ValueError("Invalid value for `op_configuration_endpoint`, must not be `None`")  # noqa: E501

        self._op_configuration_endpoint = op_configuration_endpoint

    @property
    def op_host(self):
        """Gets the op_host of this GetDiscoveryParams.  # noqa: E501

        Deprecated in favor of `op_configuration_endpoint`. It will be removed in future version(s). Provide the URL of OpenID Provider (OP) in this field. If missing, then `op_configuration_endpoint` must be defined.  # noqa: E501

        :return: The op_host of this GetDiscoveryParams.  # noqa: E501
        :rtype: str
        """
        return self._op_host

    @op_host.setter
    def op_host(self, op_host):
        """Sets the op_host of this GetDiscoveryParams.

        Deprecated in favor of `op_configuration_endpoint`. It will be removed in future version(s). Provide the URL of OpenID Provider (OP) in this field. If missing, then `op_configuration_endpoint` must be defined.  # noqa: E501

        :param op_host: The op_host of this GetDiscoveryParams.  # noqa: E501
        :type: str
        """

        self._op_host = op_host

    @property
    def op_discovery_path(self):
        """Gets the op_discovery_path of this GetDiscoveryParams.  # noqa: E501

        Deprecated in favor of `op_configuration_endpoint`. It will be removed in future version(s). Provide path to the OpenID Connect Provider's discovery document in this field. For example, if it is 'https://example.com/.well-known/openid-configuration' then the path is blank. But if it is 'https://example.com/oxauth/.well-known/openid-configuration' then the path is '/oxauth'  # noqa: E501

        :return: The op_discovery_path of this GetDiscoveryParams.  # noqa: E501
        :rtype: str
        """
        return self._op_discovery_path

    @op_discovery_path.setter
    def op_discovery_path(self, op_discovery_path):
        """Sets the op_discovery_path of this GetDiscoveryParams.

        Deprecated in favor of `op_configuration_endpoint`. It will be removed in future version(s). Provide path to the OpenID Connect Provider's discovery document in this field. For example, if it is 'https://example.com/.well-known/openid-configuration' then the path is blank. But if it is 'https://example.com/oxauth/.well-known/openid-configuration' then the path is '/oxauth'  # noqa: E501

        :param op_discovery_path: The op_discovery_path of this GetDiscoveryParams.  # noqa: E501
        :type: str
        """

        self._op_discovery_path = op_discovery_path

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
        if issubclass(GetDiscoveryParams, dict):
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
        if not isinstance(other, GetDiscoveryParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other