#!/usr/bin/python3
"""creating app_views which is an instance of Blueprint"""
from flask import Blueprint
from api.v1.views.states import *

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
