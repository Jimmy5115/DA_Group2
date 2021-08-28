import unittest

import requests
import responses


class TestCase(unittest.TestCase):

  @responses.activate
  def testExample(self):
    responses.add(**{
      'method'         : responses.GET,
      'url'            : 'https://brickset.com/sets/year-1999',
      'body'           : '{"error": "reason"}',
      'status'         : 200,
      'content_type'   : 'application/json',
      'adding_headers' : {'X-Foo': 'Bar'}
    })

    response = requests.get('https://brickset.com/sets/year-1999')

    self.assertEqual({'error': 'reason'}, response.json())
    self.assertEqual(200, response.status_code)
