from flask_restful import Resource, reqparse, request
from flask_jwt import JWT, jwt_required
from models.store import StoreModel

class Store(Resource):
	@jwt_required()
	def get(self, name):
		store = StoreModel.find_by_name(name)

		if store:
			return store.json()
		
		return {'message': 'Store not found'}, 404
	
	def post(self, name):
		if StoreModel.find_by_name(name):
			return {'message': 'Store already exists'}, 400 

		data = request.get_json()
		store = StoreModel(name)
		
		try:
			store.save_to_db()
		except:
			return {"message": "An error occured inserting the item"}, 500 # Internal server error

		return store.json(), 201

	def delete(self, name):
		store = StoreModel.find_by_name(name)

		if store:
			store.delete_from_db()

		return {'message': 'Store deleted'}

class StoreList(Resource):
	def get(self):
		return {'stores': [store.json for store in StoreModel.query.all()]}