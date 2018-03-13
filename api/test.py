#testing status code
import unittest
from app import app
from flask import json 
from models import Verification, Data_storage

test_item=Verification()

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
		self.review={
		'review':'review'
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

	def test_business_get(self):
		test=app.test_client('self')
		response=test.post('/api/businesses',data=json.dumps(self.business),headers=self.header)
		self.assertEqual(response.status_code,200)
	def test_update_business(self):
		test=app.test_client('self')
		response=test.post('/api/businesses',data=json.dumps(self.business),headers=self.header)
		self.assertEqual(response.status_code,200)

	def test_delete_business(self):
		test=app.test_client('self')
		response=test.delete('/api/businesses/0',data=json.dumps(self.business),headers=self.header)
		self.assertEqual(response.status_code,200)
	def test_review_business(self):
		test=app.test_client('self')
		response=test.post('/api/businesses/0/reviews',data=json.dumps(self.review),headers=self.header)
		self.assertEqual(response.status_code,200)
	def test_get_review_business(self):
		test=app.test_client('self')
		response=test.get('/api/businesses/0/reviews',data=json.dumps(self.review),headers=self.header)
		self.assertEqual(response.status_code,200)

	def test_email_exist(self):
		test=test_item.email_exist('kwame@gmail.com')
		self.assertFalse(test)

	def test_name_exist(self):
		test=test_item.name_exist('name')
		self.assertFalse(test)

	def test_email_check(self):
		test=test_item.email_check('name@gmail.com')
		self.assertTrue(test)

	def test_password_match(self):
		test=test_item.password_match('name','name')
		self.assertTrue(test)

	def test_email_verification(self):
		test=test_item.email_verification('name@gmail.com')
		self.assertTrue(test)

	def test_not_empty(self):
		test=test_item.email_verification('name@gmail.com')
		self.assertTrue(test)









if __name__=='__main__':
	unittest.main()