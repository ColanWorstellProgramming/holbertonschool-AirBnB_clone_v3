#!/usr/bin/python3
"""creating app_views which is an instance of Blueprint"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
