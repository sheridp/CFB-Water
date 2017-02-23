from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

class Usage(Resource):
	decorators = [auth.login_required]
    def get(self, start_range, end_range):
    	#TODO: implement user data lookup
        return None

class Pricing(Resource):
	def get(self):
		#TODO: Get actual pricing data from Boulder
		return jsonify({1000: 0.29, 5000: 0.59, 10000:1.09})

class Neighbors(Resource):
	def get(self):
		#TODO: return actual neighbor data
		return jsonify({})

api.add_resource(Usage, '/usage/<int:start_range>/<int:end_range>')
api.add_resource(Pricing, '/pricing')
api.add_resource(Neighbors, '/neigbors')

if __name__ == '__main__':
    app.run(debug=True)