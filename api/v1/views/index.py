#!/usr/bin/python3
"""
    This is the index module
"""


from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
""" Defines the import modules and packages """


@app_views.route("/status", methods=["GET"])
def status():
    """
        Returns a JSON response with status: OK
    """
    return jsonify(status="OK")


@app_views.route("/stats", methods=["GET"])
def get_stats():
    """
    Retrieves the number of each object type.
    Returns:
        A JSON response with the count of each object type.
    """
    stats = {
            "amenities": storage.count(Amenity),
            "cities": storage.count(City),
            "places": storage.count(Place),
            "reviews": storage.count(Review),
            "states": storage.count(State),
            "users": storage.count(User)
            }

    return jsonify(stats)
