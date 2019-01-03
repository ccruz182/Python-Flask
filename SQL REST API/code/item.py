import sqlite3
from flask_restful import Resource, reqparse, request
from flask_jwt import JWT, jwt_required

class Item(Resource):
	@jwt_required()
	def get(self, name):
		item = self.find_by_name(name)

		if item:
			return item
		
		return {'message': 'Item not found'}, 404

	@classmethod
	def find_by_name(cls, name):
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()

		query = "SELECT * FROM items WHERE name=?"
		result = cursor.execute(query, (name,))
		row = result.fetchone()

		connection.close()

		if row:
			return {"item": {'name': row[0], 'price': row[1]}}

	@classmethod
	def insert(cls, item):
		# Write to db
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()

		query = "INSERT INTO items VALUES (?,?)"
		cursor.execute(query, (item['name'], item['price']))

		connection.commit()
		connection.close()


	def post(self, name):
		if Item.find_by_name(name):
			return {'message': 'Item already exists'}, 400 

		data = request.get_json()
		item = {'name': name, 'price': data['price']}
		
		try:
			self.insert(item)
		except:
			return {"message": "An error occured inserting the item"}, 500 # Internal server error

		return item, 201

	def delete(self, name):
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()

		query = "DELETE FROM items WHERE name=?"
		cursor.execute(query, (name,))

		connection.commit()
		connection.close()

		return {'message': 'Item deleted'}

	def put(self, name):
		parser = reqparse.RequestParser()
		parser.add_argument('price', type=float, required=True, help="This field can not be left blank!")
				
		data = parser.parse_args()

		item = self.find_by_name(name)
		updated_item = {'name': name, 'price': data['price']}

				
		if item is None:
			try:
				self.insert(updated_item)
				return updated_item	
			except:
				return {"message": "An error occured inserting the item"}, 500
		else:
			try:
				self.update(updated_item)
				return updated_item	
			except:	
				return {"message": "An error occured updating the item"}, 500

	@classmethod
	def update(cls, item):
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()

		query = "UPDATE items SET price=? WHERE name=?"
		cursor.execute(query, (item['price'], item['name']))

		connection.commit()
		connection.close()

		return {'message': 'Item updated'}


class Items(Resource):
	def get(self):
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()

		query = "SELECT * FROM items"
		result = cursor.execute(query)
		items = []

		for row in result:
			items.append({"name": row[0], "price": row[1]})

		connection.commit()
		connection.close()

		return {'items': items}