from app import *
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
		elif user_obj.password_length(new_user['password']) == False:
			return {'Error':'password is too short'}
		else:
			new_user['user_id']=len(user_obj.user_data)+1
			del new_user['confirm_password']
			user_obj.user_data.append(new_user)
			new_user['password']=generate_password_hash(new_user['password'],method='sha256')
			return {'result':'user added'}


@api.route('/api/auth/login')
class login(Resource):
	@api.expect(login_model)
	def post(self):
		login_info=request.get_json()
		if user_obj.email_verification(login_info['email']) == False:
			return {'Error':'Incorrect Email Syntax'}
		elif user_obj.is_empty(login_info['password']) == True:
			return {'Error': 'password cannot be empty'}
		elif user_obj.password_length(login_info['password']) == False:
			return {'Error': 'password too short'}
		else:
			i=0
			index=''
			users=user_obj.user_data
			while(i<len(users)):
				temp=users[i]
				if temp['email'] == login_info['email']:
					index=i
					break
				i=i+1
			if type(index) == str:
				return {'result':'Email or password invalid'}
			else:
				x=users[index]
				p1=login_info['password']
				p2=x['password']
				#y=generate_password_hash('x',method='sha256')
				if check_password_hash(p2,p1) == True:
					user_id=x['user_id']
					first_name=x['first_name']
					user_session={'id':user_id,'first_name':first_name}
					user_obj.temp_login.append(user_session)
					return {'result':'logged in'}
				else:
					return {'result':'Email or password invalid'}

#user logout endpoint
@api.route('/api/auth/logout')
class logout(Resource):
	@api.expect(logout_model)
	def post(self):
		logout_info=request.get_json()
		if user_obj.login_check() == False:
			return {'result':'Sorry you are not logged in'}
		else:
			if logout_info['confirm_logout'] == True:
				del user_obj.temp_login[:]
				return {'result':'you are logged out'}
			else:
				return {'result':'you are still logged in'}


#user password reset
@api.route('/api/auth/reset-password')
class passwordReset(Resource):
	@api.expect(password_reset)
	def post(self):
		reset_info=request.get_json()
		if user_obj.login_check() == False:
			return {'result':'sorry you are not logged in'}
		elif user_obj.is_empty(reset_info['old_password'])== True:
			return {'Error':'can not be empty'}
		elif user_obj.is_empty(reset_info['new_password']) == True:
			return {'Error':'can not be empty'}
		elif user_obj.password_match(reset_info['new_password'], reset_info['confirm_password']) == False:
			return {'Error':'passwords do not match'}
		else:
			data=user_obj.temp_login[0]
			user_data=user_obj.user_data[data['id']-1]
			if check_password_hash(user_data['password'],reset_info['old_password']):
				del reset_info['confirm_password']
				user_data['password']=generate_password_hash(reset_info['new_password'],method="sha256")
				return {'result':'password changed'}
			else:
				#return {'result':'password fo not match'}
				return {reset_info['old_password']:user_data['password']}


#register Business
@api.route('/api/businesses')
class registerBusiness(Resource):
	@api.expect(register_business_model)
	def post(self):
		business_info=request.get_json()
		if user_obj.login_check() == False:
			return {'result':'sorry you are not logged in'}
		elif user_obj.is_empty(business_info['business_name']) == True:
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
		if len(user_obj.business_data) == 0:
			return {'result':'no business found'}
		else:
			return user_obj.business_data

						

#update a Business profile
@api.route('/api/businesses/<int:businessId>')
class updateBusiness(Resource):
	@api.expect(register_business_model)
	def put(self,businessId):
		businessId=businessId-1
		new_update=request.get_json()
		if user_obj.login_check() == False:
			return {'result':'sorry you are not logged in'}
		elif user_obj.is_empty(new_update['business_name']) == True:
			return {"Error":'fields are required'}
		elif user_obj.is_empty(new_update['business_owner']) == True:
			return {"Error":'fields are required'}
		elif user_obj.is_empty(new_update['business_description']) == True:
			return {"Error":'fields are required'}
		elif user_obj.name_exist(new_update['business_name']) == True:
			return {'Error':'Business name exist pick another name'}		
		else:
			try:
				update_info = user_obj.business_data[businessId]
				update_info['business_name'] = new_update['business_name']
				update_info['business_owner']=new_update['business_owner']
				update_info['business_description'] = new_update['business_description']
				return {'Result':'Business updated'}
			except IndexError:
				return {'Result':'no business found'}


	def delete(self,businessId):
		businessId=businessId-1
		if user_obj.login_check() == False:
			return {'result':'sorry you are not logged in'}
		try:
			new_update=user_obj.business_data[businessId]
			user_obj.business_data.pop(businessId)
			return {'Result':'deleted'}
		except IndexError:
			return {'Result':'no business found'}

		return {'result':'deleted'}
	def get(self,businessId):
		businessId=businessId-1
		try:
			new_update=user_obj.business_data[businessId]
			return new_update
		except IndexError:
			return {'Result':'no business found'}


#add a review for a business
@api.route('/api/businesses/<businessId>/reviews')
class review(Resource):
	@api.expect(review_model)
	def post(self,businessId):
		if user_obj.login_check() == False:
			return {'result':'sorry you are not logged in'}
		elif user_obj.id_exist(int(businessId)) == True:
			return {'result':'invalid index'}
		elif user_obj.check_int(int(businessId)) == True:
			return {'result':'invalid index'}
		else:
			new=request.get_json()
			new['business_id']=businessId
			user_obj.review_data.append(new)
			return {'result':'review added'}
	def get(self,businessId):
		#return user_obj.review_data
		i=0
		review=[]
		if user_obj.id_exist(int(businessId)) == True:
			return {'result':'invalid index'}
		elif user_obj.check_int(int(businessId)) == True:
			return {'result':'invalid index'}
		else:
			while (i<len(user_obj.review_data)):
				#review.append({'test':'123'})
				item=user_obj.review_data[i]
				if item['business_id'] == businessId:
					review.append(item['review'])
				i=i+1
			if len(review) == 0:
				return {'result':'No reviews for this business'}
			else:
				return review
