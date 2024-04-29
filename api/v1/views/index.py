#!/usr/bin/python3
"""
This module defines the /status route on the app_views object
"""
from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """
    Route to return the status of the application.
    Returns a JSON response with the key 'status' and value 'OK'.
    """
    return jsonify({"status": "OK"})
