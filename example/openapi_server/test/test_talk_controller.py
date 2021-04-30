# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.talk import Talk  # noqa: E501
from openapi_server.test import BaseTestCase


class TestTalkController(BaseTestCase):
    """TalkController integration test stubs"""

    def test_talks_get(self):
        """Test case for talks_get

        List all instances of Talk
        """
        query_string = [('label', 'label_example'),
                        ('page', 1),
                        ('per_page', 100)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/talks',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_talks_thingid_get(self):
        """Test case for talks_thingid_get

        Get a single Talk by its id
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/talks/{thingid}'.format(thingid='thingid_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
