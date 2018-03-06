class user:
	users = []
	def findin(self,item,email):
		result = ""
		for ls in item:
			if ls['email'] == email:
				result = True
			else:
				result = False
		return result
