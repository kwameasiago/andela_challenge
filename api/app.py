from flask import Flask
from flask_restplus import Api,Resource,fields
from model import users


app=Flask(__name__)
api=Api(app)
userObj=users()
#start of api model
registerModel=api.model('registerModel',{
	"firstName":fields.String,
	"lastName":fields.String,
	"email":fields.String,
	"password":fields.String,
	"confirmPassword":fields.String,
	})
#end of api model

@api.route('/register')
class register(Resource):
	@api.expect(registerModel)
	def post(self):
		newUser = api.payload
		email=newUser['email']
		if newUser['password'] != newUser['confirmPassword']:
			return {"result":"password do not match"}
		elif userObj.findin(userObj.users,email)==True
			return {"result":"email already exist"}
		else:
			userObj.users.append(newUser)
			return {"result":"post added"}

	def get(self):
		return userObj.users
		


if __name__=='__main__':
	app.run(debug=True)