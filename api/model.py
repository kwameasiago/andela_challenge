class users:
	users=[]
	def findin(self,item,email):
		result="test"
		for ls in item:
			if ls['email']==email:
				result=True
			else:
				result=False
		print result


lists=[]
lists.append({
	"lastName": "string",
  	"password": "string",
  	"confirmPassword": "string",
  	"email": "string",
  	"firstName": "string"
	})
lists.append({
	"lastName": "string",
  	"password": "string",
  	"confirmPassword": "string",
  	"email": "ask",
  	"firstName": "string"
	})
c=users()

c.findin(lists,"ask")
