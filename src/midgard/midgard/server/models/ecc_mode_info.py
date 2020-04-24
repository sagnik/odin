# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from midgard.server.models.base_model_ import Model
from midgard.server import util


class ECCModeInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, current_ecc: str=None, pending_ecc: str=None):  # noqa: E501
        """ECCModeInfo - a model defined in Swagger

        :param current_ecc: The current_ecc of this ECCModeInfo.  # noqa: E501
        :type current_ecc: str
        :param pending_ecc: The pending_ecc of this ECCModeInfo.  # noqa: E501
        :type pending_ecc: str
        """
        self.swagger_types = {
            'current_ecc': str,
            'pending_ecc': str
        }

        self.attribute_map = {
            'current_ecc': 'currentEcc',
            'pending_ecc': 'pendingEcc'
        }
        self._current_ecc = current_ecc
        self._pending_ecc = pending_ecc

    @classmethod
    def from_dict(cls, dikt) -> 'ECCModeInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ECCModeInfo of this ECCModeInfo.  # noqa: E501
        :rtype: ECCModeInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def current_ecc(self) -> str:
        """Gets the current_ecc of this ECCModeInfo.


        :return: The current_ecc of this ECCModeInfo.
        :rtype: str
        """
        return self._current_ecc

    @current_ecc.setter
    def current_ecc(self, current_ecc: str):
        """Sets the current_ecc of this ECCModeInfo.


        :param current_ecc: The current_ecc of this ECCModeInfo.
        :type current_ecc: str
        """

        self._current_ecc = current_ecc

    @property
    def pending_ecc(self) -> str:
        """Gets the pending_ecc of this ECCModeInfo.


        :return: The pending_ecc of this ECCModeInfo.
        :rtype: str
        """
        return self._pending_ecc

    @pending_ecc.setter
    def pending_ecc(self, pending_ecc: str):
        """Sets the pending_ecc of this ECCModeInfo.


        :param pending_ecc: The pending_ecc of this ECCModeInfo.
        :type pending_ecc: str
        """

        self._pending_ecc = pending_ecc
