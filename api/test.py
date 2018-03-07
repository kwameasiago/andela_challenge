#testing status code
import unittest
from app import app
from flask import json
class registerTest(unittest.TestCase):
	def setUp(self):
		self.newInfo={
		"firstName" : "kwame",
		"lastName" : "asiago",
		"email" : "kwame@gmail.com",
		"password" : "1234",
		"confirmPassword" : "1234"
		}
		self.logInfo={
		'email':'kwameasiago@gmail.com',
		'password':'1234'
		}
		self.header={'Content-type': 'application/json'}
	def test_register_new(self):
		test = app.test_client('self')
		response = test.post('/api/auth/register' ,data=json.dumps(self.newInfo),headers=self.header)
		self.assertEqual(response.status_code, 200)
		
	def test_login(self):
		test = app.test_client('self')
		response = test.post('/api/auth/login',data=json.dumps(self.newInfo),headers=self.header)
		self.assertTrue(response.status_code==200)






if __name__=='__main__':
	unittest.main()