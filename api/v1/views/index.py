#!/usr/bin/python3
""" creates a JSON response """
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def status():
    """creates a JSON response for status message"""
    return jsonify({"status": "OK"})
