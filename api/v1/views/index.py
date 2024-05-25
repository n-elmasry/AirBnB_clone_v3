#!/usr/bin/python3
"""create a route"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def show_status():
    """shows api status"""
    return jsonify(status='OK')
