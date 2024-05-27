#!/usr/bin/python3

"""This module contains routes for the app."""

import os
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)

# add cors support
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def close(_):
    """Handles session teardown operation."""
    storage.close()


@app.errorhandler(404)
def page_not_found(_):
    """Returns an error 404 for page not found errors."""
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(400)
def bad_request(error):
    """
    Handles the 400 Bad Request error.

    Args:
        error (Exception): The error object representing the 400 Bad Request.

    Returns:
        tuple: A tuple containing the error message and the HTTP status code
        400.
    """
    return str(error), 400


if __name__ == "__main__":
    app.run(
        host=os.getenv('HBNB_API_HOST', default='0.0.0.0'),
        port=int(os.getenv('HBNB_API_PORT', default='5000')),
        threaded=True, debug=True
    )
