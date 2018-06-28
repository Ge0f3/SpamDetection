#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import json
from main import app


class TestMethods(unittest.TestCase):

    """docstring for TestMethods"""

    def setUp(self):
        test = app.test_client(self)
        response = test.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def post(self):
        test = app.test_client(self)
        response = test.post('/api', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test1(self):
        test = app.test_client(self)
        data = \
            json.dumps(['Congratulations ur awarded either \xc3\xa5\xc2\xa3500 of CD '
                       ])
        response = test.post('/test', data=data)
        result = json.loads(response.data)
        self.assertEqual(result['results'], 'spam')

    def test2(self):
        test = app.test_client(self)
        data = json.dumps(['Hi how are you '])
        response = test.post('/test', data=data)
        result = json.loads(response.data)
        self.assertEqual(result['results'], 'ham')

    def test3(self):
        test = app.test_client(self)
        data = json.dumps(['  '])
        response = test.post('/test', data=data)
        result = json.loads(response.data)
        self.assertEqual(result['results'], 'ham')


if __name__ == '__main__':
    unittest.main()
