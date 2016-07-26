# coding=utf-8

import unittest
import json

from context import app


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        print('Running set up')
        self.app = app.app.test_client()

    def test_empty_db(self):
        resp = self.app.get('/')
        data = json.loads(resp.data.decode('utf-8'))
        assert data["status"] == "on"

    def tearDown(self):
        print('Running tear down')

if __name__ == '__main__':
    unittest.main()
