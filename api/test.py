#testing status code
import unittest
from app import app



class dataTest(unittest.TestCase):
	def setUp(self):
		self.app=app.test_client()
	def test_status_registerGET(self):
		response=self.app.get('/register')
		self.assertEqual(200,response.status_code)
	def test_status_registerPOST(self):
		response=self.app.post('/register',data={
  			"lastName": "string",
  			"password": "string",
  			"confirmPassword": "string",
  			"email": "string",
  			"firstName": "string"
		})
		self.assertEqual(200,response.status_code)

if __name__=='__main__':
	unittest.main()