# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.config_definition import ConfigDefinition  # noqa: F401,E501
from swagger_server.models.task_definition import TaskDefinition  # noqa: F401,E501
from swagger_server import util


class JobDefinition(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, name: str=None, location: str=None, creation_time: datetime=None, tasks: List[TaskDefinition]=None, configs: List[ConfigDefinition]=None):  # noqa: E501
        """JobDefinition - a model defined in Swagger

        :param id: The id of this JobDefinition.  # noqa: E501
        :type id: str
        :param name: The name of this JobDefinition.  # noqa: E501
        :type name: str
        :param location: The location of this JobDefinition.  # noqa: E501
        :type location: str
        :param creation_time: The creation_time of this JobDefinition.  # noqa: E501
        :type creation_time: datetime
        :param tasks: The tasks of this JobDefinition.  # noqa: E501
        :type tasks: List[TaskDefinition]
        :param configs: The configs of this JobDefinition.  # noqa: E501
        :type configs: List[ConfigDefinition]
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'location': str,
            'creation_time': datetime,
            'tasks': List[TaskDefinition],
            'configs': List[ConfigDefinition]
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'location': 'location',
            'creation_time': 'creationTime',
            'tasks': 'tasks',
            'configs': 'configs'
        }
        self._id = id
        self._name = name
        self._location = location
        self._creation_time = creation_time
        self._tasks = tasks
        self._configs = configs

    @classmethod
    def from_dict(cls, dikt) -> 'JobDefinition':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The JobDefinition of this JobDefinition.  # noqa: E501
        :rtype: JobDefinition
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this JobDefinition.


        :return: The id of this JobDefinition.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this JobDefinition.


        :param id: The id of this JobDefinition.
        :type id: str
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this JobDefinition.


        :return: The name of this JobDefinition.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this JobDefinition.


        :param name: The name of this JobDefinition.
        :type name: str
        """

        self._name = name

    @property
    def location(self) -> str:
        """Gets the location of this JobDefinition.


        :return: The location of this JobDefinition.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location: str):
        """Sets the location of this JobDefinition.


        :param location: The location of this JobDefinition.
        :type location: str
        """

        self._location = location

    @property
    def creation_time(self) -> datetime:
        """Gets the creation_time of this JobDefinition.


        :return: The creation_time of this JobDefinition.
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time: datetime):
        """Sets the creation_time of this JobDefinition.


        :param creation_time: The creation_time of this JobDefinition.
        :type creation_time: datetime
        """

        self._creation_time = creation_time

    @property
    def tasks(self) -> List[TaskDefinition]:
        """Gets the tasks of this JobDefinition.


        :return: The tasks of this JobDefinition.
        :rtype: List[TaskDefinition]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks: List[TaskDefinition]):
        """Sets the tasks of this JobDefinition.


        :param tasks: The tasks of this JobDefinition.
        :type tasks: List[TaskDefinition]
        """

        self._tasks = tasks

    @property
    def configs(self) -> List[ConfigDefinition]:
        """Gets the configs of this JobDefinition.


        :return: The configs of this JobDefinition.
        :rtype: List[ConfigDefinition]
        """
        return self._configs

    @configs.setter
    def configs(self, configs: List[ConfigDefinition]):
        """Sets the configs of this JobDefinition.


        :param configs: The configs of this JobDefinition.
        :type configs: List[ConfigDefinition]
        """

        self._configs = configs
