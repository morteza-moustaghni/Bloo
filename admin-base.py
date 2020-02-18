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

class Draw(Resource):
	def get(self):
		return render_template("draw.html")

api.add_resource(Draw, '/draw')

if __name__ == '__main__':
	app.run(host='0.0.0.0')