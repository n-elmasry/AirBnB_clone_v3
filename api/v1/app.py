#!/usr/bin/python3
"""flask app"""
from flask import Flask
from models import storage
from api.v1.views import app_views
from flask import CORS
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


if __name__ == '__main__':
    app.run(host=host_var, port=port_var, threaded=True)
