import sqlite3
from flask_restful import Resource, reqparse

class User:
	def __init__(self, _id, username, password):
		self.id = _id
		self.username = username
		self.password = password

	@classmethod
	def find_by_username(cls, username):
		# Initialize connection
		connection = sqlite3.connect('data.db')

		# Initialize cursor
		cursor = connection.cursor()
		
		# Query to be executed
		query = "SELECT * FROM users WHERE username=?"

		# Execute query and fetch only one result
		result = cursor.execute(query, (username,))
		row = result.fetchone()

		# Checking if there is a record with that username
		if row:
			user = cls(*row) # Positional arguments
		else:
			user = None

		connection.close()

		return user

	@classmethod
	def find_by_id(cls, _id):
		# Initialize connection
		connection = sqlite3.connect('data.db')

		# Initialize cursor
		cursor = connection.cursor()
		
		# Query to be executed
		query = "SELECT * FROM users WHERE id=?"

		# Execute query and fetch only one result
		result = cursor.execute(query, (_id,))
		row = result.fetchone()

		# Checking if there is a record with that username
		if row:
			user = cls(*row) # Positional arguments
		else:
			user = None

		connection.close()

		return user

class UserRegister(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('username',
		type=str,
		required=True,
		help="This field cannot be blank")
	parser.add_argument('password',
		type=str,
		required=True,
		help="This field cannot be blank")

	def post(self):
		data = UserRegister.parser.parse_args()
				
		if User.find_by_username(data['username']):
			return {"message": "User already exists"}, 400		

		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()

		query = "INSERT INTO users VALUES (NULL, ?, ?)"
		cursor.execute(query, (data['username'], data['password']))

		connection.commit()
		connection.close()

		return {"message": "User created successfully"}, 201