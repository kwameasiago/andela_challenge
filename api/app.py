from flask import Flask,request
import json
from flask_restplus import Api,Resource,fields
from  werkzeug.security import generate_password_hash , check_password_hash
from models import Data_storage,Verification


app = Flask(__name__)
api = Api(app)
user_obj = Verification()



#api model
register_model = api.model('registerModel',{
	"first_name" : fields.String,
	"last_name" : fields.String,
	"email" : fields.String('kwame@gmail.com'),
	"password" : fields.String,
	"confirm_password" : fields.String
})
login_model = api.model('login_info',{
	'email':fields.String,
	'password':fields.String
})
logout_model=api.model('logout_model',{
	'confirm_logout':fields.String('no')
})
password_reset=api.model('password_reset',{
	'old_password':fields.String,
	'new_password':fields.String,
	'confirm_password':fields.String
	})

#user registration endpoint
@api.route('/api/auth/register')
class Register(Resource):
	@api.expect(register_model)
	def post(self):
		new_user = request.get_json()
		password_match=user_obj.password_match(
			new_user['password'],new_user['confirm_password']
		)

		if password_match == False:
			return {'Error':'passwords do not match'}
		elif user_obj.email_exist(new_user['email']) == True:
			return {'Error':'email aready exists'}
		elif user_obj.email_verification(new_user['email']) == False:
			return {'Error':'Incorrect Email syntax'}
		elif user_obj.not_empty(new_user['first_name']) == True:
			return {'Error':'first name can not be empty'}
		elif user_obj.not_empty(new_user['last_name']) == True:
			return {'Error':'last name can not be empty'}			
		elif user_obj.not_empty(new_user['password']) == True:
			return {'Error':'password can not be empty'}			
		else:
			new_user['user_id']=len(user_obj.user_data)+1
			del new_user['confirm_password']
			user_obj.user_data.append(new_user)
			new_user['password']=generate_password_hash(new_user['password'],'sha256')
			return new_user


@api.route('/api/auth/login')
class login(Resource):
	@api.expect(login_model)
	def post(self):
		login_info=request.get_json()
		if user_obj.email_verification(login_info['email']) == False:
			return {'Error':'Incorrect Email Syntax'}
		else:
			return login_info
		

#user logout endpoint
@api.route('/api/auth/logout')
class logout(Resource):
	@api.expect(logout_model)
	def post(self):
		logout_info=request.get_json()
		if logout_info['confirm_logout'] == 'yes':
			return {'Logged out' : True}
		elif logout_info['confirm_logout'] == 'yes':
			return {'log out':False}
		else:
			return {'Error':'invalid input'}


#user password reset
@api.route('/api/auth/reset-password')
class passwordReset(Resource):
	@api.expect(password_reset)
	def post(self):
		reset_info=request.get_json()
		if user_obj.not_empty(reset_info['old_password'])== True:
			return {'Error':'can not be empty'}
		elif user_obj.not_empty(reset_info['new_password']) == True:
			return {'Error':'can not be empty'}
		elif user_obj.password_match(reset_info['new_password'], reset_info['confirm_password']) == False:
			return {'Error':'passwords do not match'}
		else:
			return reset_info


#register Business
@api.route('/api/businesses')
class registerBusiness(Resource):
	@api.expect()
	def post(self):
		pass

#update a Business profile
@api.route('/api/businesses/<businessId>')
class updateBusiness(Resource):
	@api.expect()
	def put(self,businessId):
		pass

#delete/view a business
@api.route('/api/businesses/<businessId>')
class Business(Resource):
	@api.expect()
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