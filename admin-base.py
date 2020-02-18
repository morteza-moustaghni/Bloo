from flask_admin.contrib.sqla import ModelView
from flask import *
from flask_admin import Admin
from flask_restful import *

app = Flask(__name__)
api = Api(app)


admin = Admin(app, name='digicom', template_mode='bootstrap3')

@app.route("/")
def home():
	return "HOME"	

class medi(Resource):
	def get(self):
		headers = {'Content-Type': 'text/html'}
		return make_response(render_template("index.html"), 200, headers)

api.add_resource(medi, '/medi')

if __name__ == '__main__':
	app.run(host='0.0.0.0')