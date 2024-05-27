#!/usr/bin/python3

"""Handles endpoints"""

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route("/status")
def get_status():
    """Returns the status of the API service."""
    return jsonify({"status": "OK"})


@app_views.route("/stats")
def get_stats():
    """Retrieves the number of objects by their type"""
    return jsonify(
        {
            "amenities": storage.count('Amenity'),
            "cities": storage.count('City'),
            "places": storage.count('Place'),
            "reviews": storage.count('Review'),
            "states": storage.count('State'),
            "users": storage.count('User')
        }
    )
