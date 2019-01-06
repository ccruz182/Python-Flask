import sqlite3
from flask_restful import Resource, reqparse, request
from flask_jwt import JWT, jwt_required
from models.item import ItemModel

class Item(Resource):
	@jwt_required()
	def get(self, name):
		item = ItemModel.find_by_name(name)

		if item:
			return item.json()
		
		return {'message': 'Item not found'}, 404
	
	def post(self, name):
		if ItemModel.find_by_name(name):
			return {'message': 'Item already exists'}, 400 

		data = request.get_json()
		item = ItemModel(name, data['price'])
		
		try:
			item.save_to_db()
		except:
			return {"message": "An error occured inserting the item"}, 500 # Internal server error

		return item.json(), 201

	def delete(self, name):
		item = Item.find_by_name(name)

		if item:
			item.delete_from_db()

		return {'message': 'Item deleted'}

	def put(self, name):
		parser = reqparse.RequestParser()
		parser.add_argument('price', type=float, required=True, help="This field can not be left blank!")
				
		data = parser.parse_args()

		item = ItemModel.find_by_name(name)
				
		if item is None:
			item = ItemModel(name, data['price'])
		else:
			item.price = data['price']

		item.save_to_db()

		return item.json()

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