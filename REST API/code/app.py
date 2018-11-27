from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = 'cesar'
api = Api(app) # Allows to add Resources

items = []

class Item(Resource):
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

class Items(Resource):
	def get(self):
		return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')

app.run(host="0.0.0.0", port=5000, debug=True)