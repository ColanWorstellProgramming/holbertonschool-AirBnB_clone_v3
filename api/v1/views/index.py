#!/usr/bin/python3
""" creates a JSON response """
from flask import jsonify


@app_views.route('/status')
def status():
    """creates a JSON response for status message"""
    from api.v1.views import app_views
    return jsonify({"status": "OK"})
