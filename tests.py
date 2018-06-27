import unittest
import json,requests
class TestMethods(unittest.TestCase):
	"""docstring for TestMethods"""
	def test(self):
		url= ' http://0.0.0.0:5000/test'
		data = json.dumps(['Congratulations ur awarded either å£500 of CD '])
		r=requests.post(url,data)
		result = r.json()
		self.assertEqual(result['results'],'spam')
	def test1(self):
		url= ' http://0.0.0.0:5000/test'
		data = json.dumps(['Hi how are you '])
		r=requests.post(url,data)
		result = r.json()
		self.assertEqual(result['results'],'ham')
	def test3(self):
		url= ' http://0.0.0.0:5000/test'
		data = json.dumps(['   '])
		r=requests.post(url,data)
		result = r.json()
		self.assertEqual(result['results'],'ham')
if __name__ == '__main__':
	unittest.main()
