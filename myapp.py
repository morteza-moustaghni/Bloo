from flask_admin.contrib.sqla import ModelView
from flask import *
from flask_admin import Admin
from flask_restful import *

app = Flask(__name__, template_folder="medi", static_folder="medi", static_url_path="")
api = Api(app)


admin = Admin(app, name='digicom', template_mode='bootstrap3')

@app.route("/")
def home():
	return "HOME"	

class medi(Resource):
	def get(self):
		return app.send_static_file('index.html')

api.add_resource(medi, '/medi')

if __name__ == '__main__':
	app.run(host='0.0.0.0')