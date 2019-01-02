from flask_restful import Resource, reqparse
from flask_jwt_extended import (jwt_required,get_jwt_claims,get_jwt_identity,jwt_optional,fresh_jwt_required)

from models.restaurant import RestaurantModel
from scripts.placessearch import retrieve_query

class RestaurantList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "name", type=float, required=True, help="This field cannot be left blank!"
    )
    parser.add_argument(
        "rating", type=int, required=True, help="Every Restaurant needs a rating."
    )

    def get(self, city, query):
        restaurant = retrieve_query(query, city)
        if restaurant:
            return restaurant, 200
        return {"message": "Item not found."}, 404
