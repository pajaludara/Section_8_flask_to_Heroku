from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from flask_SQLAlchemy_section6.security import authenticate, identity
from flask_SQLAlchemy_section6.resources.user import UserRegister
from flask_SQLAlchemy_section6.resources.item import Item, ItemList
from flask_SQLAlchemy_section6.resources.store import Store, StoreList

from flask_SQLAlchemy_section6.db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "paki"
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)