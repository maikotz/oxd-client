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


class UmaRpGetRptParams(object):
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
        'ticket': 'str',
        'claim_token': 'str',
        'claim_token_format': 'str',
        'pct': 'str',
        'rpt': 'str',
        'scope': 'list[str]',
        'state': 'str',
        'params': 'dict(str, str)'
    }

    attribute_map = {
        'oxd_id': 'oxd_id',
        'ticket': 'ticket',
        'claim_token': 'claim_token',
        'claim_token_format': 'claim_token_format',
        'pct': 'pct',
        'rpt': 'rpt',
        'scope': 'scope',
        'state': 'state',
        'params': 'params'
    }

    def __init__(self, oxd_id=None, ticket=None, claim_token=None, claim_token_format=None, pct=None, rpt=None, scope=None, state=None, params=None):  # noqa: E501
        """UmaRpGetRptParams - a model defined in Swagger"""  # noqa: E501
        self._oxd_id = None
        self._ticket = None
        self._claim_token = None
        self._claim_token_format = None
        self._pct = None
        self._rpt = None
        self._scope = None
        self._state = None
        self._params = None
        self.discriminator = None
        self.oxd_id = oxd_id
        self.ticket = ticket
        if claim_token is not None:
            self.claim_token = claim_token
        if claim_token_format is not None:
            self.claim_token_format = claim_token_format
        if pct is not None:
            self.pct = pct
        if rpt is not None:
            self.rpt = rpt
        if scope is not None:
            self.scope = scope
        if state is not None:
            self.state = state
        if params is not None:
            self.params = params

    @property
    def oxd_id(self):
        """Gets the oxd_id of this UmaRpGetRptParams.  # noqa: E501


        :return: The oxd_id of this UmaRpGetRptParams.  # noqa: E501
        :rtype: str
        """
        return self._oxd_id

    @oxd_id.setter
    def oxd_id(self, oxd_id):
        """Sets the oxd_id of this UmaRpGetRptParams.


        :param oxd_id: The oxd_id of this UmaRpGetRptParams.  # noqa: E501
        :type: str
        """
        if oxd_id is None:
            raise ValueError("Invalid value for `oxd_id`, must not be `None`")  # noqa: E501

        self._oxd_id = oxd_id

    @property
    def ticket(self):
        """Gets the ticket of this UmaRpGetRptParams.  # noqa: E501


        :return: The ticket of this UmaRpGetRptParams.  # noqa: E501
        :rtype: str
        """
        return self._ticket

    @ticket.setter
    def ticket(self, ticket):
        """Sets the ticket of this UmaRpGetRptParams.


        :param ticket: The ticket of this UmaRpGetRptParams.  # noqa: E501
        :type: str
        """
        if ticket is None:
            raise ValueError("Invalid value for `ticket`, must not be `None`")  # noqa: E501

        self._ticket = ticket

    @property
    def claim_token(self):
        """Gets the claim_token of this UmaRpGetRptParams.  # noqa: E501


        :return: The claim_token of this UmaRpGetRptParams.  # noqa: E501
        :rtype: str
        """
        return self._claim_token

    @claim_token.setter
    def claim_token(self, claim_token):
        """Sets the claim_token of this UmaRpGetRptParams.


        :param claim_token: The claim_token of this UmaRpGetRptParams.  # noqa: E501
        :type: str
        """

        self._claim_token = claim_token

    @property
    def claim_token_format(self):
        """Gets the claim_token_format of this UmaRpGetRptParams.  # noqa: E501


        :return: The claim_token_format of this UmaRpGetRptParams.  # noqa: E501
        :rtype: str
        """
        return self._claim_token_format

    @claim_token_format.setter
    def claim_token_format(self, claim_token_format):
        """Sets the claim_token_format of this UmaRpGetRptParams.


        :param claim_token_format: The claim_token_format of this UmaRpGetRptParams.  # noqa: E501
        :type: str
        """

        self._claim_token_format = claim_token_format

    @property
    def pct(self):
        """Gets the pct of this UmaRpGetRptParams.  # noqa: E501


        :return: The pct of this UmaRpGetRptParams.  # noqa: E501
        :rtype: str
        """
        return self._pct

    @pct.setter
    def pct(self, pct):
        """Sets the pct of this UmaRpGetRptParams.


        :param pct: The pct of this UmaRpGetRptParams.  # noqa: E501
        :type: str
        """

        self._pct = pct

    @property
    def rpt(self):
        """Gets the rpt of this UmaRpGetRptParams.  # noqa: E501


        :return: The rpt of this UmaRpGetRptParams.  # noqa: E501
        :rtype: str
        """
        return self._rpt

    @rpt.setter
    def rpt(self, rpt):
        """Sets the rpt of this UmaRpGetRptParams.


        :param rpt: The rpt of this UmaRpGetRptParams.  # noqa: E501
        :type: str
        """

        self._rpt = rpt

    @property
    def scope(self):
        """Gets the scope of this UmaRpGetRptParams.  # noqa: E501


        :return: The scope of this UmaRpGetRptParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this UmaRpGetRptParams.


        :param scope: The scope of this UmaRpGetRptParams.  # noqa: E501
        :type: list[str]
        """

        self._scope = scope

    @property
    def state(self):
        """Gets the state of this UmaRpGetRptParams.  # noqa: E501


        :return: The state of this UmaRpGetRptParams.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this UmaRpGetRptParams.


        :param state: The state of this UmaRpGetRptParams.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def params(self):
        """Gets the params of this UmaRpGetRptParams.  # noqa: E501


        :return: The params of this UmaRpGetRptParams.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this UmaRpGetRptParams.


        :param params: The params of this UmaRpGetRptParams.  # noqa: E501
        :type: dict(str, str)
        """

        self._params = params

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
        if issubclass(UmaRpGetRptParams, dict):
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
        if not isinstance(other, UmaRpGetRptParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
