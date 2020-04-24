# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from midgard.server.models.base_model_ import Model
from midgard.server import util


class GPUClockInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, mem_clock: float=None, unit: str=None):  # noqa: E501
        """GPUClockInfo - a model defined in Swagger

        :param mem_clock: The mem_clock of this GPUClockInfo.  # noqa: E501
        :type mem_clock: float
        :param unit: The unit of this GPUClockInfo.  # noqa: E501
        :type unit: str
        """
        self.swagger_types = {
            'mem_clock': float,
            'unit': str
        }

        self.attribute_map = {
            'mem_clock': 'memClock',
            'unit': 'unit'
        }
        self._mem_clock = mem_clock
        self._unit = unit

    @classmethod
    def from_dict(cls, dikt) -> 'GPUClockInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GPUClockInfo of this GPUClockInfo.  # noqa: E501
        :rtype: GPUClockInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def mem_clock(self) -> float:
        """Gets the mem_clock of this GPUClockInfo.


        :return: The mem_clock of this GPUClockInfo.
        :rtype: float
        """
        return self._mem_clock

    @mem_clock.setter
    def mem_clock(self, mem_clock: float):
        """Sets the mem_clock of this GPUClockInfo.


        :param mem_clock: The mem_clock of this GPUClockInfo.
        :type mem_clock: float
        """

        self._mem_clock = mem_clock

    @property
    def unit(self) -> str:
        """Gets the unit of this GPUClockInfo.


        :return: The unit of this GPUClockInfo.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit: str):
        """Sets the unit of this GPUClockInfo.


        :param unit: The unit of this GPUClockInfo.
        :type unit: str
        """

        self._unit = unit
