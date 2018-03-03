from flask import Flask
from flask_restful import Resource,Api,request

app=Flask(__name__)
api=Api(app)
todos = {"Name":"asiago"}
class helloWorld(Resource):
	def get(self, todo_id):
		return {"GET": todos["Name"]}
	def put(self, todo_id):
		todos[todo_id] = todo_id
		return {"PUT": todos[todo_id]}
	def post(self,todo_id):
		todos[todo_id]=todo_id
		return{"POST":todos[todo_id]}
	def delete(self,todo_id):
		todos["Name"]=""
		return{"DELETE":todos["Name"]}


api.add_resource(helloWorld,'/<string:todo_id>',endpoint="user")
if __name__=='__main__':
	app.run(debug=True)