# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.lecture import Lecture  # noqa: E501
from openapi_server.test import BaseTestCase


class TestLectureController(BaseTestCase):
    """LectureController integration test stubs"""

    def test_lectures_get(self):
        """Test case for lectures_get

        List all instances of Lecture
        """
        query_string = [('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/lectures',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_lectures_thingid_get(self):
        """Test case for lectures_thingid_get

        Get a single Lecture by its id
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/lectures/{thingid}'.format(thingid='thingid_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
