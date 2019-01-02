from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager

app = Flask(__name__)

from db import db
from resources.restaurant import RestaurantList

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["JWT_BLACKLIST_ENABLED"] = True  # enable blacklist feature
app.config["JWT_BLACKLIST_TOKEN_CHECKS"] = [
    "access",
    "refresh",
]  # allow blacklisting for access and refresh tokens

app.secret_key = "jose"  # could do app.config['JWT_SECRET_KEY'] if we prefer
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWTManager(app)

#api.add_resource(Restaurant, "/restaurant/<string:name>")
#api.add_resource(RestaurantSearch, "/restaurant/search")
api.add_resource(RestaurantList, "/restaurants/<string:city>/<string:query>")

if __name__ == "__main__":
    db.init_app(app)
    app.run(host='0.0.0.0', port=5000, debug=True)
