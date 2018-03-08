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
	'confirm_logout':fields.Boolean
})
password_reset=api.model('password_reset',{
	'old_password':fields.String,
	'new_password':fields.String,
	'confirm_password':fields.String
})
register_business_model=api.model('register_business',{
	'business_name':fields.String,
	'business_description':fields.String,
	'business_owner':fields.String
})
review_model=api.model('review_model',{
	'review':fields.String,
	'business_id':fields.Integer
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
		elif user_obj.is_empty(new_user['first_name']) == True:
			return {'Error':'first name can not be empty'}
		elif user_obj.is_empty(new_user['last_name']) == True:
			return {'Error':'last name can not be empty'}			
		elif user_obj.is_empty(new_user['password']) == True:
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
		elif user_obj.is_empty(login_info['password']) == True:
			return {'Error': 'password cannot be empty'}
		else:
			return login_info
		

#user logout endpoint
@api.route('/api/auth/logout')
class logout(Resource):
	@api.expect(logout_model)
	def post(self):
		logout_info=request.get_json()
		login_status = True
		if login_status == False:
			return {'Error:':'not logged in'}
		elif logout_info['confirm_logout'] == True:
			return {'logout':'logged out'}
		elif logout_info['confirm_logout'] == False:
			return {'logout': 'not logged out'}
		else:
			return {'Error':'invalid input'}


#user password reset
@api.route('/api/auth/reset-password')
class passwordReset(Resource):
	@api.expect(password_reset)
	def post(self):
		reset_info=request.get_json()
		if user_obj.is_empty(reset_info['old_password'])== True:
			return {'Error':'can not be empty'}
		elif user_obj.is_empty(reset_info['new_password']) == True:
			return {'Error':'can not be empty'}
		elif user_obj.password_match(reset_info['new_password'], reset_info['confirm_password']) == False:
			return {'Error':'passwords do not match'}
		else:
			return reset_info


#register Business
@api.route('/api/businesses')
class registerBusiness(Resource):
	@api.expect(register_business_model)
	def post(self):
		business_info=request.get_json()
		if user_obj.is_empty(business_info['business_name']) == True:
			return {"Error":'fields are required'}
		elif user_obj.is_empty(business_info['business_owner']) == True:
			return {"Error":'fields are required'}
		elif user_obj.is_empty(business_info['business_description']) == True:
			return {"Error":'fields are required'}
		elif user_obj.name_exist(business_info['business_name']) == True:
			return {'Error':'Business name exist pick another name'}
		else:
			business_info['id']=len(user_obj.business_data)+1
			user_obj.business_data.append(business_info)
			return {'result':'business added'}
	def get(self):
		return user_obj.business_data

						

#update a Business profile
@api.route('/api/businesses/<int:businessId>')
class updateBusiness(Resource):
	@api.expect(register_business_model)
	def put(self,businessId):
		businessId=businessId-1
		update_info = user_obj.business_data[businessId]
		new_update=request.get_json()
		if user_obj.is_empty(new_update['business_name']) == True:
			return {"Error":'fields are required'}
		elif user_obj.is_empty(new_update['business_owner']) == True:
			return {"Error":'fields are required'}
		elif user_obj.is_empty(new_update['business_description']) == True:
			return {"Error":'fields are required'}
		else:
			update_info['business_name'] = new_update['business_name']
			update_info['business_owner']=new_update['business_owner']
			update_info['business_description'] = new_update['business_description']
			return new_update

	def delete(self,businessId):
		businessId=businessId-1
		new_update=user_obj.business_data[businessId]
		user_obj.business_data.pop(businessId)
		return {'result':'deleted'}
	def get(self,businessId):
		businessId=businessId-1
		new_update=user_obj.business_data[businessId]
		return new_update


#add a review for a business
@api.route('/api/businesses/<businessId>/reviews')
class review(Resource):
	@api.expect(review_model)
	def post(self,businessId):
		new_review=request.get_json()
		new_review['business_id']=businessId
		new_review['review_id']=len(user_obj.review_data)+1
		user_obj.review_data.append(new_review)
		return user_obj.review_data
	def get(self,businessId):
		#return user_obj.review_data
		i=0
		review=[]
		while (i<len(user_obj.review_data)):
			#review.append({'test':'123'})
			item=user_obj.review_data[i]
			if item['business_id'] == businessId:
				review.append(item['review'])
			i=i+1
		return review



		


if __name__ == '__main__':
	app.run(debug=True)
