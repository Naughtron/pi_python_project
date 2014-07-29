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

# unit test for /mod2
class TestModTwoPageContents(unittest.TestCase):
	server_address = ''

	def setUp(self):
		self.server_address = "localhost:5000"

	def test_mod2(self):
		url_template = 'http://%s/mod2'
		url = url_template %(self.server_address)

		print url

		resp = requests.get(url)
		#import pdb; pdb.set_trace()

		self.assertEqual(resp.status_code, 200)
		self.assertEqual(resp.text, u'<!--this is the first template \n<html>\n <head>\n \t<title>Home - microblog</title>\n </head>\n <body>\n \t<h1>Hello, Naughtron!</h1>\n </body>\n</html> -->\n\n<!-- user Jinja to set control statements in a template-->\n<!--<html>\n <head>\n \t \n \t<title>Home - microblog</title>\n \t\n </head>\n <body>\n \t<h1>Greetings, Naughtron!</h1>\n \t \n \t<p>Jeff says: <b>Be the bomb you throw!</b></p> \n \t \n \t<p>Connor says: <b>I am a real life lore nerd</b></p> \n \t \n </body>\n</html>-->\n\n<!--inherit from the base template-->\n<!--this is the base template that allows other templates to inherit core features-->\n<!-- the index.html will inherit from this template-->\n<html>\n <head>\n \t\n \t<title>Home - microblog</title>\n \t\n </head>\n <body>\n \t<div>Microblog: <a href="/index">Home</a></div>\n \t<hr>\n \t\n<h1>Greetings, Naughtron!</h1>\n\n<div><p>Jeff says: <b>Be the bomb you throw!</b></p></div>\n\n<div><p>Connor says: <b>I am a real life lore nerd</b></p></div>\n\n\n </body>\n</html>')

		
if __name__ == '__main__':
    unittest.main()		
