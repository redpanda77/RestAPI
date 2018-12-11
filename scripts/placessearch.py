import googlemaps
from datetime import datetime
from pprint import pprint
import os

API_KEY = os.environ['API_KEY']



def json(place):
    return {
        "name": place['name'],
        "location": place['geometry']['location'],
        "address": place['formatted_address'],
        "rating": place['rating'],
        "google_id": place['id'],
    }


def retrieve_query(query, city):

    restaurantsList = list()

    gmaps = googlemaps.Client(key=API_KEY)
    city = gmaps.geocode(city)

    lat = city[0]['geometry']['location']['lat']
    long = city[0]['geometry']['location']['lng']
    print(lat, long)

    places_result = gmaps.places(query, location=(lat,long))

    for place in places_result['results']:
        restaurantsList.append(json(place))

    return restaurantsList
