from flask import Flask
from flask_restplus import Api
app=Flask(__name__)
api=Api(app)

@app.route('/')
def index():
	return "Flask is set up"

if __name__=='__main__':
	app.run(debug=True)