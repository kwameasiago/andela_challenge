from flask import Flask,request
from flask_restplus import Api,Resource,fields
from  werkzeug.security import generate_password_hash , check_password_hash
from models import Data_storage,Verification


app = Flask(__name__)
api = Api(app)
user_obj = Verification()

app.config.from_pyfile('config.py')

		
from views import *

if __name__ == '__main__':
	app.run()