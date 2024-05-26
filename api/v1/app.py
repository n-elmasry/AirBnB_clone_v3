#!/usr/bin/python3
"""flask app"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from flask_cors import CORS
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)

CORS(app, origins="0.0.0.0")
host_var = getenv('HBNB_API_HOST')
port_var = getenv('HBNB_API_PORT')


@app.teardown_appcontext
def teardown_appcontext(self):
    """calls close"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    return jsonify(error='Not found'), 404


if __name__ == '__main__':
    host_var = getenv('HBNB_API_HOST', '0.0.0.0')
    port_var = getenv('HBNB_API_PORT', '5000')
    app.run(host=host_var, port=int(port_var), threaded=True)
