from flask import Flask, request, jsonify
from marshmallow import Schema, fields, validate, ValidationError
from pymongo import MongoClient


def create_app(local=False):
	app = Flask(__name__)
	
	if local: # use local mongodb - loaded in command line using mongod
		mongoclient = MongoClient()
	else: # use mongodb from docker
		mongoclient = MongoClient("mongo:27017")


	@app.route('/')
	def hello():
		return "Hello World!"


	@app.route('/cache-me')
	def cache():
		return "nginx will cache this response"


	@app.route('/info')
	def info():

		resp = {
			'connecting_ip': request.headers['X-Real-IP'],
			'proxy_ip': request.headers['X-Forwarded-For'],
			'host': request.headers['Host'],
			'user-agent': request.headers['User-Agent']
		}

		return jsonify(resp)


	@app.route('/flask-health-check')
	def flask_health_check():
		try:
			mongoclient.admin.command('hello') #check mongo responds
		except:
			return "failure", 500
		return "success", 200


	class PostSchema(Schema):
		"""
		schema for post requests to the endpoint
		"""
		user_id = fields.Str(validate=validate.Length(5), required=True)
		latitude = fields.Float(validate=validate.Range(-90.0, 90.0), required=True)
		longitude = fields.Float(validate=validate.Range(-180.0, 180.0), required=True)
		time = fields.Int(validate=validate.Range(0), required=True)
		accuracy = fields.Float(validate=validate.Range(0.0), allow_nan=True, allow_none=True)
		speed = fields.Float(validate=validate.Range(0.0), allow_nan=True, allow_none=True)
		speed_accuracy = fields.Float(validate=validate.Range(0.0), allow_nan=True, allow_none=True)
		

	class GetSchema(Schema):
		"""
		schema for post requests to the endpoint
		"""
		from_time = fields.Int(validate=validate.Range(0), required=False)


	@app.route('/post-data', methods=['GET', 'POST'])
	def post_data():
		# validate post request
		try:
			request_data = PostSchema().load(request.get_json())
		except ValidationError as err:
			return jsonify(err.messages), 400
		
		db = mongoclient['main-database']
		posts = db.posts
		posts.insert_one(request_data)
		
		return "success'", 200
		

	@app.route('/get-data')
	def get_data():
		# validate get request
		request_data = request.get_json(silent=True)
		if request_data is None:
			from_time = 0
		else:
			try:
				request_data = GetSchema().load(request_data)
				from_time = request_data.get('from_time', 0)
			except ValidationError as err:
				return jsonify(err.messages), 400
			
		db = mongoclient['main-database']
		posts = db.posts
		output = {'data': [post for post in posts.find({"time": {"$gte": from_time}}) if post.pop('_id', None)]}
			
		return jsonify(output), 200

	return app
