# imports
import requests
import unittest
import sys

# unit test class
'''setup'''
class TestHelloWorld(unittest.TestCase):
	server_address = ''

	def setUp(self):
		self.server_address = "localhost:5000"

	def test_HelloWorld(self):
		url_template = 'http://%s'
		url = url_template %(self.server_address)

		# verify url
		print url 

		# make the request
		resp = requests.get(url)

		# import pdb; pdb.set_trace()

		# assert response
		self.assertEqual(resp.status_code, 200)
		# assert text coming back
		self.assertEqual(resp.text, u'Hello World!')
		
if __name__ == '__main__':
    unittest.main()		
