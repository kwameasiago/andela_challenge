from flask import Flask,request
import json
from flask_restplus import Api,Resource,fields
from  werkzeug.security import generate_password_hash , check_password_hash
from models import User


app = Flask(__name__)
api = Api(app)
user_obj = User()



#api model
register_model = api.model('registerModel',{
	"first_name" : fields.String,
	"last_name" : fields.String,
	"email" : fields.String,
	"password" : fields.String,
	"confirm_password" : fields.String
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
		else:
			return {'ok':''}


@api.route('/api/auth/login')
class login(Resource):
	@api.expect()
	def post(self):
		pass
		

#user logout endpoint
@api.route('/api/auth/logout')
class logout(Resource):
	@api.expect()
	def post(self):
		pass


#user password reset
@api.route('/api/auth/reset-password')
class passwordReset(Resource):
	@api.expect()
	def post(self):
		pass


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