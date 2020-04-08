# project/__init__.py


from flask import Flask, jsonify, render_template
from flask_restx import Resource, Api


# instantiate the app
app = Flask(__name__)

api = Api(app)

#set config
app.config.from_object('project.config.DevelopmentConfig') 

#add the first end-point
class Ping(Resource):
    def get(self):
    	return {
    	'status': 'success',
    	'message': 'pong'
    	}

# def get_status_code(url):
#     """ This function returns the status code of the url."""
#     try:
#         status_code = requests.get(url, timeout=30).status_code
#         return status_code
#     except requests.ConnectionError:
#         return site_down
    

api.add_resource(Ping, '/pong')
#api.add_resource(get_status_code, 'status')

#return a 201 and modify one of the headers. This makes it easier to right a customer test. 
