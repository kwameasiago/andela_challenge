#testing status code
import unittest
from app import app
from flask import json


class registerTest(unittest.TestCase):
	def setUp(self):
		self.newInfo={
		"first_name" : "kwame",
		"last_name" : "asiago",
		"email" : "kwame@gmail.com",
		"password" : "1234",
		"confirm_password" : "1234"
		}
		self.logInfo={
		'email':'kwameasiago@gmail.com',
		'password':'1234'
		}
		self.logout={'confirm_logout':'yes'}
		self.password_reset={
		'old_password':'1234',
		'new_password':'asd',
		'confirm_password':'asd'

		}
		self.business={
		'business_owner':'kwame',
		'business_name':'sela danti',
		'business_description':'sell designs'
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
	def test_logout(self):
		test=app.test_client('self')
		response = test.post('/api/auth/logout', data=json.dumps(self.logout),headers=self.header)
		self.assertEqual(response.status_code,200)
	def test_password_reset(self):
		test=app.test_client('self')
		response=test.post('/api/auth/reset-password',data=json.dumps(self.password_reset),headers=self.header)
		self.assertEqual(response.status_code,200)
	def test_business_update(self):
		test=app.test_client('self')
		response=test.put('/api/businesses/0',data=json.dumps(self.business),headers=self.header)
		self.assertEqual(response.status_code,200)





if __name__=='__main__':
	unittest.main()