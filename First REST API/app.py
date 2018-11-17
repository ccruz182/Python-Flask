from flask import Flask, jsonify

app = Flask(__name__) # Gives a unique name
stores = [
  {
	'name': 'MyStore',
    'items': [
      {
        'name': 'My Item',
        'price': 15.99
      }
    ]	
  }
]

"""
@app.route('/') # Route of the endpoint 'http://www.google.com/'
def home():
	return "Hello, world!"
"""

# POST /store. data: {name: }
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {'name': request_data['name'], 'items': []}
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    store = list(filter(lambda store: store['name'] == name, stores))
    if store == []:
        return jsonify({'message': 'store not found'})
    else:
        return jsonify(store)

# GET /store
@app.route('/store')
def get_stores():
	return jsonify({'stores': stores})

# POST /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    store = list(filter(lambda store: store['name'] == name, stores))
    new_item = {'name': request_data['name'], 'price': request_data['price']}
    if store == []
        return jsonify({'message': 'store not found'})

    store[0]['items'].append(new_item)
    return jsonify(new_item)


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    store = list(filter(lambda store: store['name'] == name, stores))
    
    if store == []:
        return jsonify({'message': 'store not found'})
    else:
        return jsonify({'items': store[0]['items']})


app.run(host= '0.0.0.0', port=5000)