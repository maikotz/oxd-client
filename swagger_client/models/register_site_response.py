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


class RegisterSiteResponse(object):
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
        'op_host': 'str',
        'client_id': 'str',
        'client_name': 'str',
        'client_secret': 'str',
        'client_registration_access_token': 'str',
        'client_registration_client_uri': 'str',
        'client_id_issued_at': 'int',
        'client_secret_expires_at': 'int'
    }

    attribute_map = {
        'oxd_id': 'oxd_id',
        'op_host': 'op_host',
        'client_id': 'client_id',
        'client_name': 'client_name',
        'client_secret': 'client_secret',
        'client_registration_access_token': 'client_registration_access_token',
        'client_registration_client_uri': 'client_registration_client_uri',
        'client_id_issued_at': 'client_id_issued_at',
        'client_secret_expires_at': 'client_secret_expires_at'
    }

    def __init__(self, oxd_id=None, op_host=None, client_id=None, client_name=None, client_secret=None, client_registration_access_token=None, client_registration_client_uri=None, client_id_issued_at=None, client_secret_expires_at=None):  # noqa: E501
        """RegisterSiteResponse - a model defined in Swagger"""  # noqa: E501
        self._oxd_id = None
        self._op_host = None
        self._client_id = None
        self._client_name = None
        self._client_secret = None
        self._client_registration_access_token = None
        self._client_registration_client_uri = None
        self._client_id_issued_at = None
        self._client_secret_expires_at = None
        self.discriminator = None
        self.oxd_id = oxd_id
        self.op_host = op_host
        if client_id is not None:
            self.client_id = client_id
        if client_name is not None:
            self.client_name = client_name
        if client_secret is not None:
            self.client_secret = client_secret
        if client_registration_access_token is not None:
            self.client_registration_access_token = client_registration_access_token
        if client_registration_client_uri is not None:
            self.client_registration_client_uri = client_registration_client_uri
        if client_id_issued_at is not None:
            self.client_id_issued_at = client_id_issued_at
        if client_secret_expires_at is not None:
            self.client_secret_expires_at = client_secret_expires_at

    @property
    def oxd_id(self):
        """Gets the oxd_id of this RegisterSiteResponse.  # noqa: E501


        :return: The oxd_id of this RegisterSiteResponse.  # noqa: E501
        :rtype: str
        """
        return self._oxd_id

    @oxd_id.setter
    def oxd_id(self, oxd_id):
        """Sets the oxd_id of this RegisterSiteResponse.


        :param oxd_id: The oxd_id of this RegisterSiteResponse.  # noqa: E501
        :type: str
        """
        if oxd_id is None:
            raise ValueError("Invalid value for `oxd_id`, must not be `None`")  # noqa: E501

        self._oxd_id = oxd_id

    @property
    def op_host(self):
        """Gets the op_host of this RegisterSiteResponse.  # noqa: E501


        :return: The op_host of this RegisterSiteResponse.  # noqa: E501
        :rtype: str
        """
        return self._op_host

    @op_host.setter
    def op_host(self, op_host):
        """Sets the op_host of this RegisterSiteResponse.


        :param op_host: The op_host of this RegisterSiteResponse.  # noqa: E501
        :type: str
        """
        if op_host is None:
            raise ValueError("Invalid value for `op_host`, must not be `None`")  # noqa: E501

        self._op_host = op_host

    @property
    def client_id(self):
        """Gets the client_id of this RegisterSiteResponse.  # noqa: E501


        :return: The client_id of this RegisterSiteResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this RegisterSiteResponse.


        :param client_id: The client_id of this RegisterSiteResponse.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def client_name(self):
        """Gets the client_name of this RegisterSiteResponse.  # noqa: E501


        :return: The client_name of this RegisterSiteResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """Sets the client_name of this RegisterSiteResponse.


        :param client_name: The client_name of this RegisterSiteResponse.  # noqa: E501
        :type: str
        """

        self._client_name = client_name

    @property
    def client_secret(self):
        """Gets the client_secret of this RegisterSiteResponse.  # noqa: E501


        :return: The client_secret of this RegisterSiteResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this RegisterSiteResponse.


        :param client_secret: The client_secret of this RegisterSiteResponse.  # noqa: E501
        :type: str
        """

        self._client_secret = client_secret

    @property
    def client_registration_access_token(self):
        """Gets the client_registration_access_token of this RegisterSiteResponse.  # noqa: E501


        :return: The client_registration_access_token of this RegisterSiteResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_registration_access_token

    @client_registration_access_token.setter
    def client_registration_access_token(self, client_registration_access_token):
        """Sets the client_registration_access_token of this RegisterSiteResponse.


        :param client_registration_access_token: The client_registration_access_token of this RegisterSiteResponse.  # noqa: E501
        :type: str
        """

        self._client_registration_access_token = client_registration_access_token

    @property
    def client_registration_client_uri(self):
        """Gets the client_registration_client_uri of this RegisterSiteResponse.  # noqa: E501


        :return: The client_registration_client_uri of this RegisterSiteResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_registration_client_uri

    @client_registration_client_uri.setter
    def client_registration_client_uri(self, client_registration_client_uri):
        """Sets the client_registration_client_uri of this RegisterSiteResponse.


        :param client_registration_client_uri: The client_registration_client_uri of this RegisterSiteResponse.  # noqa: E501
        :type: str
        """

        self._client_registration_client_uri = client_registration_client_uri

    @property
    def client_id_issued_at(self):
        """Gets the client_id_issued_at of this RegisterSiteResponse.  # noqa: E501


        :return: The client_id_issued_at of this RegisterSiteResponse.  # noqa: E501
        :rtype: int
        """
        return self._client_id_issued_at

    @client_id_issued_at.setter
    def client_id_issued_at(self, client_id_issued_at):
        """Sets the client_id_issued_at of this RegisterSiteResponse.


        :param client_id_issued_at: The client_id_issued_at of this RegisterSiteResponse.  # noqa: E501
        :type: int
        """

        self._client_id_issued_at = client_id_issued_at

    @property
    def client_secret_expires_at(self):
        """Gets the client_secret_expires_at of this RegisterSiteResponse.  # noqa: E501


        :return: The client_secret_expires_at of this RegisterSiteResponse.  # noqa: E501
        :rtype: int
        """
        return self._client_secret_expires_at

    @client_secret_expires_at.setter
    def client_secret_expires_at(self, client_secret_expires_at):
        """Sets the client_secret_expires_at of this RegisterSiteResponse.


        :param client_secret_expires_at: The client_secret_expires_at of this RegisterSiteResponse.  # noqa: E501
        :type: int
        """

        self._client_secret_expires_at = client_secret_expires_at

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
        if issubclass(RegisterSiteResponse, dict):
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
        if not isinstance(other, RegisterSiteResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other