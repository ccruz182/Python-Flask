from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'cesar'
api = Api(app) # Allows to add Resources

jwt = JWT(app, authenticate, identity) # /auth

items = []

class Item(Resource):
	@jwt_required()
	def get(self, name):
		item = filter(lambda item: item['name'] == name, items)
		if item == []:
			return {'item': None}, 404
		else:
			return {'item': item}, 200

	def post(self, name):
		item = filter(lambda item: item['name'] == name, items)
		if item == []:
			data = request.get_json()
			itemC = {'name': name, 'price': data['price']}
			items.append(itemC)
			return itemC, 201
		else:
			return {'message': 'Item already exists'}, 400 

	def delete(self, name):
		global items
		items = list(filter(lambda x: x['name'] != name, items))
		return {'message': 'Item deleted'}

	def put(self, name):
		item = filter(lambda item: item['name'] == name, items)
		data = request.get_json()
		
		if item == []:
			itemC = {'name': name, 'price': data['price']}
			items.append(itemC)			
		else:
			item[0].update(data)

		return item


class Items(Resource):
	def get(self):
		return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')

app.run(host="0.0.0.0", port=5000, debug=True)