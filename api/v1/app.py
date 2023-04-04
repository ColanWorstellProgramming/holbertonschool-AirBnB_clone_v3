#!/usr/bin/python3
""" Creating an instance of Flask """
from flask import Flask
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import getenv as env


app = Flask(__name__)
CORS(app, resources={"/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """method closes storage session"""
    storage.close()


def start_flask():
    """ start flask """
    app.run(host=env('HBNB_API_HOST'),
            port=env('HBNB_API_PORT'),
            threaded=True)


if __name__ == "__main__":
    start_flask()
