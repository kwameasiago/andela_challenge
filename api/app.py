from flask import Flask,request
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
loginModel=api.model('loginModel',{
	"email":fields.String,
	"password":fields.String
	})
logoutModel=api.model('logoutModel',{
	"logout":fields.String
	})
passwordResetModel=api.model("passwordResetModel",{
	"oldPassword":fields.String,
	"newPassword":fields.String,
	"confirmPassword":fields.String
	})
registerBusinessModel=api.model("registerBusinessModel",{
	'title':fields.String,
	'description':fields.String,
	'author':fields.String,
	'businessId':fields.Integer
	})
updateBusinessModel=api.model('updateBusinessModel',{
	'title':fields.String,
	'description':fields.String,
	})
businessModel=api.model('businessModel',{
	'businessId':fields.Integer
	})
#end of api model


#user registration endpoint
@api.route('/api/auth/register')
class register(Resource):
	@api.expect(registerModel)
	def post(self):
		newUser=api.payload
		#email=str(request.data.get('email',''))
		#email = newUser['email']
		if newUser['password'] != newUser['confirmPassword']:
		 	return {"result":"password do not match"}
		elif userObj.findIn(userObj.users,newUser['email']) == True:
		 	return {"result":"email already exist"}
		elif userObj.emailCheck(newUser['email'])==False:
			return {"result":"mast be a valid email"}
		else:
		 	newUser['password']=generate_password_hash(newUser['password'],"sha256")
		 	del newUser['confirmPassword']
		 	userObj.users.append(newUser)
		 	return {"result":"added to database"}
	def get(self):
		return {'test':'123'}

#user login end point 
@api.route('/api/auth/login')
class login(Resource):
	@api.expect(loginModel)
	def post(self):
		pass


#user logout endpoint
@api.route('/api/auth/logout')
class logout(Resource):
	@api.expect(logoutModel)
	def post(self):
		pass


#user password reset
@api.route('/api/auth/reset-password')
class passwordReset(Resource):
	@api.expect(passwordResetModel)
	def post(self):
		pass


#register Business
@api.route('/api/businesses')
class registerBusiness(Resource):
	@api.expect(registerBusinessModel)
	def post(self):
		pass

#update a Business profile
@api.route('/api/businesses/<businessId>')
class updateBusiness(Resource):
	@api.expect(updateBusinessModel)
	def put(self,businessId):
		pass

#delete/view a business
@api.route('/api/businesses/<businessId>')
class Business(Resource):
	@api.expect(businessModel)
	def delete(self,businessId):
		pass
	def get(self):
		pass

#get all business
@api.route('/api/businesses')
class getAllBusiness(Resource):
	def get(self):
		pass


#add a review for a business
@api.route('/api/businesses/<businessId>/reviews')
class review(Resource):
	def post(self):
		pass
	def get(self):
		pass


"""-----------------------------------------------


--------------------------------------------------"""

if __name__ == '__main__':
	app.run(debug=True)