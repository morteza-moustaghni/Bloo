from flask_admin.contrib.sqla import ModelView
from flask import Flask
from flask_admin import Admin
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


admin = Admin(app, name='digicom', template_mode='bootstrap3')

@app.route("/")
def home():
	return "HOME"	

class HelloWorld(Resource):
	def get(self):
		return{'hello', 'world'}

api.add_resource(HelloWorld, '/helloworld')

if __name__ == '__main__':
	app.run(host='0.0.0.0')