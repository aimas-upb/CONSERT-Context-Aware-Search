# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Laboratory(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, has_recurrence=None, has_professor=None, has_host=None, has_end_time=None, description=None, has_location=None, id=None, label=None, type=None, has_start_time=None):  # noqa: E501
        """Laboratory - a model defined in OpenAPI

        :param has_recurrence: The has_recurrence of this Laboratory.  # noqa: E501
        :type has_recurrence: List[object]
        :param has_professor: The has_professor of this Laboratory.  # noqa: E501
        :type has_professor: List[object]
        :param has_host: The has_host of this Laboratory.  # noqa: E501
        :type has_host: List[object]
        :param has_end_time: The has_end_time of this Laboratory.  # noqa: E501
        :type has_end_time: List[str]
        :param description: The description of this Laboratory.  # noqa: E501
        :type description: List[str]
        :param has_location: The has_location of this Laboratory.  # noqa: E501
        :type has_location: List[object]
        :param id: The id of this Laboratory.  # noqa: E501
        :type id: str
        :param label: The label of this Laboratory.  # noqa: E501
        :type label: List[str]
        :param type: The type of this Laboratory.  # noqa: E501
        :type type: List[str]
        :param has_start_time: The has_start_time of this Laboratory.  # noqa: E501
        :type has_start_time: List[str]
        """
        self.openapi_types = {
            'has_recurrence': List[object],
            'has_professor': List[object],
            'has_host': List[object],
            'has_end_time': List[str],
            'description': List[str],
            'has_location': List[object],
            'id': str,
            'label': List[str],
            'type': List[str],
            'has_start_time': List[str]
        }

        self.attribute_map = {
            'has_recurrence': 'hasRecurrence',
            'has_professor': 'hasProfessor',
            'has_host': 'hasHost',
            'has_end_time': 'hasEndTime',
            'description': 'description',
            'has_location': 'hasLocation',
            'id': 'id',
            'label': 'label',
            'type': 'type',
            'has_start_time': 'hasStartTime'
        }

        self._has_recurrence = has_recurrence
        self._has_professor = has_professor
        self._has_host = has_host
        self._has_end_time = has_end_time
        self._description = description
        self._has_location = has_location
        self._id = id
        self._label = label
        self._type = type
        self._has_start_time = has_start_time

    @classmethod
    def from_dict(cls, dikt) -> 'Laboratory':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Laboratory of this Laboratory.  # noqa: E501
        :rtype: Laboratory
        """
        return util.deserialize_model(dikt, cls)

    @property
    def has_recurrence(self):
        """Gets the has_recurrence of this Laboratory.

        Description not available  # noqa: E501

        :return: The has_recurrence of this Laboratory.
        :rtype: List[object]
        """
        return self._has_recurrence

    @has_recurrence.setter
    def has_recurrence(self, has_recurrence):
        """Sets the has_recurrence of this Laboratory.

        Description not available  # noqa: E501

        :param has_recurrence: The has_recurrence of this Laboratory.
        :type has_recurrence: List[object]
        """

        self._has_recurrence = has_recurrence

    @property
    def has_professor(self):
        """Gets the has_professor of this Laboratory.

        Description not available  # noqa: E501

        :return: The has_professor of this Laboratory.
        :rtype: List[object]
        """
        return self._has_professor

    @has_professor.setter
    def has_professor(self, has_professor):
        """Sets the has_professor of this Laboratory.

        Description not available  # noqa: E501

        :param has_professor: The has_professor of this Laboratory.
        :type has_professor: List[object]
        """

        self._has_professor = has_professor

    @property
    def has_host(self):
        """Gets the has_host of this Laboratory.

        Description not available  # noqa: E501

        :return: The has_host of this Laboratory.
        :rtype: List[object]
        """
        return self._has_host

    @has_host.setter
    def has_host(self, has_host):
        """Sets the has_host of this Laboratory.

        Description not available  # noqa: E501

        :param has_host: The has_host of this Laboratory.
        :type has_host: List[object]
        """

        self._has_host = has_host

    @property
    def has_end_time(self):
        """Gets the has_end_time of this Laboratory.

        Description not available  # noqa: E501

        :return: The has_end_time of this Laboratory.
        :rtype: List[str]
        """
        return self._has_end_time

    @has_end_time.setter
    def has_end_time(self, has_end_time):
        """Sets the has_end_time of this Laboratory.

        Description not available  # noqa: E501

        :param has_end_time: The has_end_time of this Laboratory.
        :type has_end_time: List[str]
        """

        self._has_end_time = has_end_time

    @property
    def description(self):
        """Gets the description of this Laboratory.

        small description  # noqa: E501

        :return: The description of this Laboratory.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Laboratory.

        small description  # noqa: E501

        :param description: The description of this Laboratory.
        :type description: List[str]
        """

        self._description = description

    @property
    def has_location(self):
        """Gets the has_location of this Laboratory.

        Description not available  # noqa: E501

        :return: The has_location of this Laboratory.
        :rtype: List[object]
        """
        return self._has_location

    @has_location.setter
    def has_location(self, has_location):
        """Sets the has_location of this Laboratory.

        Description not available  # noqa: E501

        :param has_location: The has_location of this Laboratory.
        :type has_location: List[object]
        """

        self._has_location = has_location

    @property
    def id(self):
        """Gets the id of this Laboratory.

        identifier  # noqa: E501

        :return: The id of this Laboratory.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Laboratory.

        identifier  # noqa: E501

        :param id: The id of this Laboratory.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Laboratory.

        short description of the resource  # noqa: E501

        :return: The label of this Laboratory.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Laboratory.

        short description of the resource  # noqa: E501

        :param label: The label of this Laboratory.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Laboratory.

        type of the resource  # noqa: E501

        :return: The type of this Laboratory.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Laboratory.

        type of the resource  # noqa: E501

        :param type: The type of this Laboratory.
        :type type: List[str]
        """

        self._type = type

    @property
    def has_start_time(self):
        """Gets the has_start_time of this Laboratory.

        Description not available  # noqa: E501

        :return: The has_start_time of this Laboratory.
        :rtype: List[str]
        """
        return self._has_start_time

    @has_start_time.setter
    def has_start_time(self, has_start_time):
        """Sets the has_start_time of this Laboratory.

        Description not available  # noqa: E501

        :param has_start_time: The has_start_time of this Laboratory.
        :type has_start_time: List[str]
        """
        if has_start_time is not None and len(has_start_time) > 1:
            raise ValueError("Invalid value for `has_start_time`, number of items must be less than or equal to `1`")  # noqa: E501

        self._has_start_time = has_start_time
