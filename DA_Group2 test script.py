# Import libraries for unit testing, requests and responses
import unittest

import requests
import responses

# Create a test class for general scaffolding to test the functions
class TestCase(unittest.TestCase):
# Mock the requests module
# Left of the colon are requests and right of the colon are responses
  @responses.activate
  def testExample(self):
    responses.add(**{
      'method'         : responses.GET,
      'url'            : 'https://brickset.com/sets/year-1999',
      'body'           : '{"error": "reason"}',
      'status'         : 200,
    })
# The get() method sends a GET request to the specified url.
    response = requests.get('https://brickset.com/sets/year-1999')
# self.assertEqual forms a test assertion which is used to continue the execute if the given condition evaluates to True
    self.assertEqual({'error': 'reason'}, response.json())
    self.assertEqual(200, response.status_code)
