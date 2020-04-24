# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from midgard.server.models.base_model_ import Model
from midgard.server import util


class GPUUtilizationInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, gpu_util: float=None, memory_util: float=None, unit: str=None):  # noqa: E501
        """GPUUtilizationInfo - a model defined in Swagger

        :param gpu_util: The gpu_util of this GPUUtilizationInfo.  # noqa: E501
        :type gpu_util: float
        :param memory_util: The memory_util of this GPUUtilizationInfo.  # noqa: E501
        :type memory_util: float
        :param unit: The unit of this GPUUtilizationInfo.  # noqa: E501
        :type unit: str
        """
        self.swagger_types = {
            'gpu_util': float,
            'memory_util': float,
            'unit': str
        }

        self.attribute_map = {
            'gpu_util': 'gpuUtil',
            'memory_util': 'memoryUtil',
            'unit': 'unit'
        }
        self._gpu_util = gpu_util
        self._memory_util = memory_util
        self._unit = unit

    @classmethod
    def from_dict(cls, dikt) -> 'GPUUtilizationInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GPUUtilizationInfo of this GPUUtilizationInfo.  # noqa: E501
        :rtype: GPUUtilizationInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def gpu_util(self) -> float:
        """Gets the gpu_util of this GPUUtilizationInfo.


        :return: The gpu_util of this GPUUtilizationInfo.
        :rtype: float
        """
        return self._gpu_util

    @gpu_util.setter
    def gpu_util(self, gpu_util: float):
        """Sets the gpu_util of this GPUUtilizationInfo.


        :param gpu_util: The gpu_util of this GPUUtilizationInfo.
        :type gpu_util: float
        """

        self._gpu_util = gpu_util

    @property
    def memory_util(self) -> float:
        """Gets the memory_util of this GPUUtilizationInfo.


        :return: The memory_util of this GPUUtilizationInfo.
        :rtype: float
        """
        return self._memory_util

    @memory_util.setter
    def memory_util(self, memory_util: float):
        """Sets the memory_util of this GPUUtilizationInfo.


        :param memory_util: The memory_util of this GPUUtilizationInfo.
        :type memory_util: float
        """

        self._memory_util = memory_util

    @property
    def unit(self) -> str:
        """Gets the unit of this GPUUtilizationInfo.


        :return: The unit of this GPUUtilizationInfo.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit: str):
        """Sets the unit of this GPUUtilizationInfo.


        :param unit: The unit of this GPUUtilizationInfo.
        :type unit: str
        """

        self._unit = unit
