import re

class Data_storage:
	def __init__(self):
		self.business_data=[]
		self.user_data=[]
		self.review_data=[]
		self.temp_login=[]


class Verification(Data_storage):
	def email_exist(self,email):
		result = ""
		item=self.user_data
		for ls in item:
			if ls['email'] == email:
				result = True
			else:
				result = False
		return result

	def name_exist(self,name):
		result = ""
		item=self.business_data
		for ls in item:
			if ls['business_name'] == name:
				result = True
			else:
				result = False
		return result	

	def email_check(self,email):
		result = ''
		if '@' in email and '.' in email:
			result = True
		else:
			result = False
		return result

	def password_match(self,password,confirm_password):		
		result=''
		if password != confirm_password:
			result = False
		else:
			result = True
		return result

	def email_verification(self,email):
		result=''
		match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
		if match == None:
			result=False
		else:
			result=True
		return result
		
	def is_empty(self,item):
		result=''
		if len(item) == 0:
			result = True
		else:
			result =False
		return result

	def password_length(self,password):
		result=''
		if len(password)<6:
			result=False
		else:
			result=True
		return result

	def id_exist(self,business_id):
		result=''
		data=len(self.business_data)
		if business_id<=data:
			result = False
		elif data == 0:
			result = True
		else:
			result = True
		return result
	def check_int(self,numb):
		if numb<0:
			return True
		else:
			return False

	def login_check(self):
		if len(self.temp_login)<1:
			return False


