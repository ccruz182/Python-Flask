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

	def post(self, name):
		if Item.find_by_name(name):
			return {'message': 'Item already exists'}, 400 

		data = request.get_json()
		item = {'name': name, 'price': data['price']}
		
		# Write to db
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()

		query = "INSERT INTO items VALUES (?,?)"
		cursor.execute(query, (item['name'], item['price']))

		connection.commit()
		connection.close()

		return item, 201

	def delete(self, name):
		global items
		items = list(filter(lambda x: x['name'] != name, items))
		return {'message': 'Item deleted'}

	def put(self, name):
		parser = reqparse.RequestParser()
		parser.add_argument('price', type=float, required=True, help="This field can not be left blank!")
		
		item = filter(lambda item: item['name'] == name, items)
		
		data = parser.parse_args()
		# data = request.get_json()
		
		if item == []:
			itemC = {'name': name, 'price': data['price']}
			items.append(itemC)			
		else:
			item[0].update(data)

		return item


class Items(Resource):
	def get(self):
		return {'items': items}