from flask import Flask
from flask_restplus import Api,Resource,fields
from  werkzeug.security import generate_password_hash , check_password_hash
from models import user


app = Flask(__name__)
api = Api(app)
userObj = user()



#start of api model
registerModel = api.model('registerModel',{
	"firstName":fields.String,
	"lastName":fields.String,
	"email":fields.String,
	"password":fields.String,
	"confirmPassword":fields.String,
	})
#end of api model

@api.route('/api/auth/register')
class register(Resource):
	@api.expect(registerModel)
	def post(self):
		newUser = api.payload
		email = newUser['email']
		if newUser['password'] != newUser['confirmPassword']:
			return {"result":"password do not match"}
		elif userObj.findIn(userObj.users,email) == True:
			return {"result":"email already exist"}
		elif userObj.emailCheck(email)==False:
			return {"result":"mast be a valid email"}
		else:
			newUser['password']=generate_password_hash(newUser['password'],"sha256")
			userObj.users.append(newUser)
			return {"result":"added to database"}
	def get(self):
		return userObj.users


if __name__ == '__main__':
	app.run(debug=True)