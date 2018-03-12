from flask import Flask,request
from flask_restplus import Api,Resource,fields
from  werkzeug.security import generate_password_hash , check_password_hash
from models import Data_storage,Verification


app = Flask(__name__)
api = Api(app)
user_obj = Verification()

app.config.from_pyfile('config.py')

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




		
from views import *

if __name__ == '__main__':
	app.run()
