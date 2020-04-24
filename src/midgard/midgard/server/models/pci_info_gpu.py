# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from midgard.server.models.base_model_ import Model
from midgard.server import util


class PCIInfoGPU(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, pci_bus_id: str=None):  # noqa: E501
        """PCIInfoGPU - a model defined in Swagger

        :param pci_bus_id: The pci_bus_id of this PCIInfoGPU.  # noqa: E501
        :type pci_bus_id: str
        """
        self.swagger_types = {
            'pci_bus_id': str
        }

        self.attribute_map = {
            'pci_bus_id': 'pciBusId'
        }
        self._pci_bus_id = pci_bus_id

    @classmethod
    def from_dict(cls, dikt) -> 'PCIInfoGPU':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PCIInfoGPU of this PCIInfoGPU.  # noqa: E501
        :rtype: PCIInfoGPU
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pci_bus_id(self) -> str:
        """Gets the pci_bus_id of this PCIInfoGPU.


        :return: The pci_bus_id of this PCIInfoGPU.
        :rtype: str
        """
        return self._pci_bus_id

    @pci_bus_id.setter
    def pci_bus_id(self, pci_bus_id: str):
        """Sets the pci_bus_id of this PCIInfoGPU.


        :param pci_bus_id: The pci_bus_id of this PCIInfoGPU.
        :type pci_bus_id: str
        """

        self._pci_bus_id = pci_bus_id
