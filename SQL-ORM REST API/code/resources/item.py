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
		item = ItemModel(name, data['price'], data['store_id'])
		
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
		parser.add_argument('store_id', type=int, required=True, help="This field can not be left blank!")
				
		data = parser.parse_args()

		item = ItemModel.find_by_name(name)
				
		if item is None:
			item = ItemModel(name, data['price'], data['store_id'])
		else:
			item.price = data['price']
			item.store_id = data['store_id']

		item.save_to_db()

		return item.json()

class Items(Resource):
	def get(self):
		return {'items': [item.json for item in ItemModel.query.all()]}