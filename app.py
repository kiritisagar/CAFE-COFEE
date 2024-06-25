from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# MongoDB configuration
app.config["MONGO_URI"] = "mongodb://mongo:27017/cafe_app"
mongo = PyMongo(app)

# Routes
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Cafe App Backend"

@app.route('/menu', methods=['GET'])
def get_menu():
    menu_items = mongo.db.menu.find()
    result = []
    for item in menu_items:
        result.append({
            '_id': str(item['_id']),
            'name': item['name'],
            'price': item['price'],
            'description': item['description']
        })
    return jsonify(result)

@app.route('/menu', methods=['POST'])
def add_menu_item():
    data = request.get_json()
    new_item = {
        'name': data['name'],
        'price': data['price'],
        'description': data['description']
    }
    result = mongo.db.menu.insert_one(new_item)
    return jsonify({'_id': str(result.inserted_id)}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
