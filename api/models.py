class user:
	users = []
	#check if email exist
	def findIn(self,item,email):
		result = ""
		for ls in item:
			if ls['email'] == email:
				result = True
			else:
				result = False
		return result
	def emailCheck(self,email):
		result=""
		if "@" in email and "." in email:
			result=True
		else:
			result=False
		return result
